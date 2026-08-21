import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests
from dotenv import load_dotenv

load_dotenv(override=True)


class WikiQueryEngine:
    # --- PATTERNS REGEX GLOBAUX ---

    PAT_ROLE_PREFIX = re.compile(
        r"^\s*[\*\-]*\s*\**\s*("
        r"Présentateur\s*/\s*Hôte\s*/\s*invités\s*/\s*Intervenants|"
        r"Présentateur\s*/\s*Hôte\s*/\s*invités|"
        r"Présentateur\s*/\s*Hôte|Intervenants|Présentateur|Hôte|Speaker|Present\s+Dns|"
        r"Présentateur\s*/\s*Expert"
        r")\s*\**\s*:\s*\**",
        flags=re.IGNORECASE,
    )

    PAT_TITRES_A_IGNORER = re.compile(
        r"(#+\s*)?(🎯\s*)?(aperçu\s+et\s+résumé\s+global|aperçu\s+global|résumé\s+global|aperçu|résumé|fiche\s+(de\s+)?synthèse)\s*:?",
        flags=re.IGNORECASE,
    )

    PAT_TITRE_ACAD = re.compile(
        r"^\s*(dr\-ing|dr\.|dr|prof\.|prof|pr\.|pr|mr\.|mr|mme|ms|mrs)\s+",
        flags=re.IGNORECASE,
    )

    def __init__(
        self,
        wiki_dir: str = "wiki",
        db_dir: str = "chroma_db",
        pipeline: Optional[Any] = None,
        **kwargs,
    ):
        self.wiki_dir = Path(wiki_dir)
        self.db_dir = db_dir
        self.pipeline = pipeline

        raw_key = os.getenv("GROQ_API_KEY", "")
        self.groq_api_key = raw_key.strip().strip("'").strip('"')

    def index_wiki(self) -> bool:
        """Méthode de compatibilité pour Streamlit."""
        print("ℹ️ Moteur de recherche prêt.")
        return True

    # --- NETTOYAGE ET PARSING DE TEXTE ---

    def _nettoyer_chaine(self, texte: str) -> str:
        """Supprime le balisage parasite, émojis, parenthèses orphelines et espaces superflus."""
        if not texte:
            return ""

        texte = re.sub(r"[📄ℹ️🎯#]", "", texte)
        texte = re.sub(r"^[\*\-\s]+", "", texte)
        texte = re.sub(r"[\*\-\s]+$", "", texte)
        texte = texte.replace("**", "").replace("`", "").strip()

        # Correction des parenthèses déséquilibrées/orphelines
        if texte.count(")") > texte.count("("):
            texte = texte.replace(")", "")
        elif texte.count("(") > texte.count(")"):
            texte = texte.replace("(", "")

        return texte.strip()

    def _nettoyer_prefixe_role(self, texte: str) -> str:
        """Supprime rigoureusement tous les préfixes de rôles et étiquettes parasites."""
        if not texte:
            return ""

        cleaned = self.PAT_ROLE_PREFIX.sub("", texte).strip()
        cleaned = self.PAT_ROLE_PREFIX.sub("", cleaned).strip()

        if " — " in cleaned:
            parties = cleaned.split(" — ")
            parties_propres = [
                p
                for p in parties
                if not re.search(
                    r"Présentateur|Hôte|Intervenants|Speaker", p, re.IGNORECASE
                )
            ]
            if parties_propres:
                cleaned = " — ".join(parties_propres)

        return re.sub(r"^[\*\-\s:]+", "", cleaned).strip()

    def _nettoyer_titre_academique(self, nom: str) -> str:
        return self.PAT_TITRE_ACAD.sub("", nom).strip()

    def _est_nom_personne_valide(self, nom: str) -> bool:
        if not nom or len(nom) < 3:
            return False

        nom_lower = nom.lower().strip()

        mots_parasites = [
           "nom du fichier",
            "source :",
            "webinaire.url",
            "http",
            ".url",
            ".md",
            "www.",
            ".com",
            "bnewdeb",
            "09-fgb",
            "15/221",
            "ueny",
            "chaîne youtube",
            "chaine youtube",
            "youtube",
            "information à récupérer",
            "west africa",
            "levant",
            "dell technologies",
            "temps forts",
            "temps fort",
        ]
        if any(w in nom_lower for w in mots_parasites):
            return False

        if re.search(r"\d{2,}[\/\-_]\d+|\b[A-Z0-9]{3,}\b.*?\d+", nom):
            return False

        mots_interdits = [
            "citation",
            "point marquant",
            "liste des",
            "intervenants",
            "équipe",
            "equipe",
            "résumé",
            "aperçu",
            "synthèse",
            "introduction",
            "conclusion",
            "description",
            "pas préparé",
            "peu préparé",
            "modérément",
            "simulation",
            "optimisation",
            "résolution",
            "cryptographie",
            "nécessité",
            "besoin",
            "les machines",
            "le quantique",
            "rôle",
            "role",
            "fonction",
            "organisation",
            "entrées",
            "sorties",
            "objectif",
            "statut",
            "points clés",
            "présentateur",
            "presentateur",
            "hôte",
            "hote",
            "expert",
            "chimie",
            "physique",
        ]
        if any(m in nom_lower for m in mots_interdits):
            return False

        if re.search(r"\d+[\s%]|^\d+$", nom_lower) or len(nom.split()) > 8:
            return False

        return True

    def _normaliser_date(self, texte_date: str) -> str:
        m = re.search(
            r"(\d{1,2})[\/\-_\s]+(\d{1,2})[\/\-_\s]+(\d{2,4})", texte_date
        )
        if m:
            j, m_num, a = m.groups()
            return f"{int(j):02d}[/\\-_\\s]+{int(m_num):02d}[/\\-_\\s]+{a}"
        return texte_date

    def _extraire_section_apercu(self, texte_md: str) -> str:
        lignes = texte_md.splitlines()
        capturer = False
        bloc_contenu = []

        for line in lignes:
            line_str = line.strip()

            if re.search(
                r"aperçu\s+et\s+résumé\s+global|aperçu\s+global|résumé\s+global|aperçu|résumé",
                line_str,
                re.IGNORECASE,
            ):
                capturer = True
                if ":" in line_str:
                    suite = line_str.split(":", 1)[1]
                    clean_suite = self._nettoyer_chaine(suite)
                    if len(clean_suite) > 10:
                        bloc_contenu.append(clean_suite)
                continue

            if capturer:
                if (
                    line_str.startswith("## ")
                    or line_str.startswith("# ")
                    or line_str.startswith("---")
                ) and bloc_contenu:
                    break

                if (
                    line_str
                    and not line_str.startswith("|")
                    and not re.search(
                        r"présentateur|hôte|intervenant|speaker",
                        line_str,
                        re.IGNORECASE,
                    )
                ):
                    clean_l = self._nettoyer_chaine(line_str)
                    if clean_l:
                        bloc_contenu.append(clean_l)

        if bloc_contenu:
            return " ".join(bloc_contenu)

        paragraphes = [
            self._nettoyer_chaine(p)
            for p in texte_md.split("\n\n")
            if len(self._nettoyer_chaine(p)) > 40 and not p.startswith("|")
        ]
        return " ".join(paragraphes[:2]) if paragraphes else texte_md

    def _extraire_presentateur_par_balise(self, texte_md: str) -> Optional[str]:
        pattern = re.compile(
            r"\*\*\s*(Présentateur\s*/\s*Hôte(?:\s*/\s*invités\s*/\s*Intervenants)?)\s*:\s*\*\*\s*(.+)",
            re.IGNORECASE,
        )

        for line in texte_md.splitlines():
            line_clean = line.strip()
            match = pattern.search(line_clean)
            if match:
                valeur = match.group(2).strip()
                valeur_propre = self._nettoyer_prefixe_role(valeur)
                valeur_propre = self._nettoyer_chaine(valeur_propre)
                if valeur_propre:
                    return valeur_propre
        return None

    def _extraire_depuis_tableau_markdown(
        self, ligne: str
    ) -> Optional[List[Dict[str, str]]]:
        colonnes = [c.strip() for c in ligne.split("|")]
        if len(colonnes) >= 5:
            nom = colonnes[2] if len(colonnes) > 2 else ""
            institution = colonnes[3] if len(colonnes) > 3 else ""
            fonction = colonnes[4] if len(colonnes) > 4 else ""
            email = colonnes[5] if len(colonnes) > 5 else "—"

            nom_clean = self._nettoyer_chaine(nom)

            if (
                not nom_clean
                or "NOM" in nom_clean.upper()
                or "---" in nom_clean
                or nom_clean == "—"
            ):
                return None

            nom_sans_titre = self._nettoyer_titre_academique(nom_clean)

            if not self._est_nom_personne_valide(nom_sans_titre):
                return None

            return [{
                "nom": nom_sans_titre,
                "institution": (
                    self._nettoyer_chaine(institution)
                    if institution and institution != "—"
                    else "Non précisée"
                ),
                "fonction": (
                    self._nettoyer_chaine(fonction)
                    if fonction and fonction != "—"
                    else "Non précisée"
                ),
                "email": (
                    email.strip() if email and email != "—" else "Non précisé"
                ),
            }]
        return None

    def _analyser_ligne_personne(self, texte: str) -> List[Dict[str, str]]:
        clean = self._nettoyer_chaine(texte)
        clean = self._nettoyer_prefixe_role(clean)

        if not clean or "non précisé" in clean.lower():
            return []

        resultats = []
        
        # 1. Découpage explicite par slash / pour séparer chaque intervenant
        segments_personnes = [s.strip() for s in clean.split("/") if s.strip()]

        for segment_brut in segments_personnes:
            # 2. Découpage sur chevauchement complexe de personnes agglomérées
            segments = re.split(
                r"(?<=\))\s*(?=[A-Z])|(?<=\b[a-z])\s+(?=[A-Z][a-z]+\s+[—–-])",
                segment_brut,
            )

            for segment in segments:
                segment_clean = self._nettoyer_chaine(segment)
                if not segment_clean:
                    continue

                nom, fonction, institution = (
                    segment_clean,
                    "Non précisée",
                    "Non précisée",
                )

                # Extraction du nom et du rôle/institution séparés par tiret
                parts = re.split(r"\s*[—–-]\s*", segment_clean, maxsplit=1)

                if len(parts) == 2:
                    nom = self._nettoyer_chaine(parts[0])
                    reste = parts[1].strip()

                    # Détection Organisme / Fonction (ex: "chez", "at", virgule)
                    if " chez " in reste.lower():
                        f_parts = re.split(
                            r"\bchez\b", reste, flags=re.IGNORECASE, maxsplit=1
                        )
                        fonction = self._nettoyer_chaine(f_parts[0])
                        institution = self._nettoyer_chaine(f_parts[1])
                    elif " at " in reste.lower():
                        f_parts = re.split(
                            r"\bat\b", reste, flags=re.IGNORECASE, maxsplit=1
                        )
                        fonction = self._nettoyer_chaine(f_parts[0])
                        institution = self._nettoyer_chaine(f_parts[1])
                    elif "," in reste:
                        f_parts = reste.split(",", 1)
                        fonction = self._nettoyer_chaine(f_parts[0])
                        institution = self._nettoyer_chaine(f_parts[1])
                    else:
                        fonction = self._nettoyer_chaine(reste)

                nom_clean = self._nettoyer_titre_academique(nom)

                if self._est_nom_personne_valide(nom_clean):
                    resultats.append({
                        "nom": nom_clean,
                        "institution": (
                            institution if institution else "Non précisée"
                        ),
                        "fonction": fonction if fonction else "Non précisée",
                        "email": "Non précisé",
                    })

        return resultats

    def _extraire_invites(
        self,
        filtre_date: Optional[str] = None,
        inclure_email: bool = False,
    ) -> tuple[str, List[str]]:
        if not self.wiki_dir.exists():
            return "", []

        fiches = sorted(list(self.wiki_dir.glob("*.md")))
        sources, liste_personnes = [], []

        pattern_date = (
            self._normaliser_date(filtre_date) if filtre_date else None
        )
        mots_cles = [
            "présentateur",
            "hôte",
            "hote",
            "intervenant",
            "invité",
            "invite",
            "speaker",
        ]

        for md_file in fiches:
            if md_file.name in ["index.md", "log.md"]:
                continue
            try:
                content = md_file.read_text(encoding="utf-8").strip()
                if not content:
                    continue

                if (
                    pattern_date
                    and not re.search(pattern_date, content, re.IGNORECASE)
                    and not re.search(
                        pattern_date, md_file.name, re.IGNORECASE
                    )
                ):
                    continue

                lignes = content.splitlines()
                moteur_sous_liste = False

                for line in lignes:
                    line_str = line.strip()

                    if line_str.startswith("|"):
                        moteur_sous_liste = False
                        res_tab_list = self._extraire_depuis_tableau_markdown(
                            line_str
                        )
                        if res_tab_list:
                            for res_tab in res_tab_list:
                                if res_tab and res_tab["nom"] and not any(
                                    p["nom"].lower() == res_tab["nom"].lower()
                                    for p in liste_personnes
                                ):
                                    liste_personnes.append(res_tab)
                                    if md_file.name not in sources:
                                        sources.append(md_file.name)
                        continue

                    line_lower = line_str.lower()

                    if any(kw in line_lower for kw in mots_cles):
                        moteur_sous_liste = True
                        if ":" in line_str:
                            valeur = line_str.split(":", 1)[1].strip()
                            if valeur and "non précisé" not in valeur.lower():
                                personnes = self._analyser_ligne_personne(
                                    line_str
                                )
                                for p in personnes:
                                    if p and not any(
                                        e["nom"].lower() == p["nom"].lower()
                                        for e in liste_personnes
                                    ):
                                        liste_personnes.append(p)
                                        if md_file.name not in sources:
                                            sources.append(md_file.name)
                        continue

                    if moteur_sous_liste:
                        if line_str.startswith(
                            ("*", "-")
                        ) or line.startswith("   *"):
                            personnes = self._analyser_ligne_personne(line_str)
                            for p in personnes:
                                if p and not any(
                                    e["nom"].lower() == p["nom"].lower()
                                    for e in liste_personnes
                                ):
                                    liste_personnes.append(p)
                                    if md_file.name not in sources:
                                        sources.append(md_file.name)
                        elif line_str.startswith("##") or line_str.startswith(
                            "---"
                        ):
                            moteur_sous_liste = False

            except Exception:
                continue

        if not liste_personnes:
            return "", []

        if inclure_email:
            lignes_tab = [
                "| N° | NOM & PRENOM | INSTITUTION | FONCTION | EMAIL |",
                "| --- | --- | --- | --- | --- |",
            ]
            for idx, p in enumerate(liste_personnes, start=1):
                lignes_tab.append(
                    f"| {idx} | {p['nom']} | {p['institution']} | {p['fonction']} | {p['email']} |"
                )
        else:
            lignes_tab = [
                "| N° | NOM & PRENOM | INSTITUTION | FONCTION |",
                "| --- | --- | --- | --- |",
            ]
            for idx, p in enumerate(liste_personnes, start=1):
                lignes_tab.append(
                    f"| {idx} | {p['nom']} | {p['institution']} | {p['fonction']} |"
                )

        return "\n".join(lignes_tab), sources

    def _analyser_intention(self, question: str) -> Dict[str, Any]:
        q_lower = question.lower()

        mots_cles_liste = [
            "invite",
            "invité",
            "invites",
            "invités",
            "intervenant",
            "intervenants",
            "présentateur",
            "presentateur",
            "participants",
            "participant",
            "qui participe",
            "présence",
            "presence",
            "présences",
            "presences",
            "présents",
            "presents",
            "liste",
        ]
        est_demande_liste = any(kw in q_lower for kw in mots_cles_liste)

        est_qui_presente = any(
            kw in q_lower
            for kw in [
                "qui présente",
                "qui presente",
                "qui anime",
                "qui est le présentateur",
                "qui est le presentateur",
                "présenté par",
                "presente par",
            ]
        )
        est_qui = (
            q_lower.startswith("qui")
            and not est_qui_presente
            and not est_demande_liste
        )

        est_sujet = any(
            kw in q_lower
            for kw in [
                "de quoi parle",
                "de quoi traite",
                "sujet",
                "thème",
                "theme",
                "parle de",
                "parle du",
                "résumé",
                "aperçu",
                "a propos de",
            ]
        )

        match_date = re.search(
            r"\b\d{1,2}[\/\-_\s]+\d{1,2}[\/\-_\s]+\d{2,4}\b", question
        )
        filtre_date = match_date.group(0) if match_date else None

        return {
            "est_demande_liste": est_demande_liste,
            "est_qui_presente": est_qui_presente,
            "est_qui": est_qui,
            "est_sujet": est_sujet,
            "filtre_date": filtre_date,
            "inclure_email": any(
                e in q_lower
                for e in ["email", "e-mail", "mail", "mails", "courriel"]
            ),
        }

    def _generer_reponse_personne(self, nom_recherche: str, texte: str) -> str:
        """Isole spécifiquement la personne recherchée et sa fonction/institution."""
        mots_nom = [
            m.lower()
            for m in re.findall(r"\w+", nom_recherche)
            if len(m) > 1
        ]
        info_personne = ""
        sujets = []

        for line in texte.splitlines():
            line_clean = self._nettoyer_chaine(line)
            line_lower = line_clean.lower()

            if mots_nom and all(m in line_lower for m in mots_nom):
                personnes_extraites = self._analyser_ligne_personne(line_clean)
                for p in personnes_extraites:
                    if all(m in p["nom"].lower() for m in mots_nom):
                        inst = (
                            f" chez {p['institution']}"
                            if p["institution"] != "Non précisée"
                            else ""
                        )
                        info_personne = (
                            f"{p['nom']} — {p['fonction']}{inst}".strip()
                        )
                        break

                if not info_personne:
                    info_personne = self._nettoyer_prefixe_role(line_clean)

            elif any(
                k in line_lower for k in ["thème", "theme", "sujet", "titre"]
            ):
                clean_l = self._nettoyer_chaine(line)
                clean_l = re.sub(
                    r"^(thème de la présentation|sujet principal|sujet|titre)\s*:\s*",
                    "",
                    clean_l,
                    flags=re.IGNORECASE,
                )
                if (
                    clean_l
                    and len(clean_l) > 5
                    and "informations générales" not in clean_l.lower()
                ):
                    sujets.append(clean_l)

        if info_personne:
            res = f"{info_personne}\n"
        else:
            res = f"{nom_recherche.title()}\n"

        if sujets:
            res += f"\nPrésente les thématiques suivantes : {', '.join(sujets[:2])}."

        return res

    def _appeler_groq_api(self, prompt: str) -> str:
        if not self.groq_api_key:
            raise ValueError("La clé GROQ_API_KEY est introuvable.")

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.groq_api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Tu es un assistant de synthèse direct et concis.\n"
                        "Règles strictes :\n"
                        "1. Interdiction ABSOLUE de mettre des mots comme 'Présentateur :', 'Hôte :', 'Intervenants :' ou 'Présentateur / Hôte / invités / Intervenants :'.\n"
                        "2. Commence directement par le nom ou l'information demandée."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.1,
            "max_tokens": 500,
        }

        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.ok:
            return response.json()["choices"][0]["message"]["content"]

        raise RuntimeError(f"Erreur API Groq : {response.status_code}")

    def query(
        self,
        question: str,
        llm_model: Optional[str] = None,
        pipeline: Optional[Any] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Méthode principale de traitement."""
        intention = self._analyser_intention(question)

        if intention["est_demande_liste"]:
            tableau_md, sources = self._extraire_invites(
                filtre_date=intention["filtre_date"],
                inclure_email=intention["inclure_email"],
            )
            if tableau_md:
                return {
                    "answer": tableau_md,
                    "stream": tableau_md,
                    "sources": sources,
                }
            msg = f"Aucun invité trouvé{' pour la date du ' + intention['filtre_date'] if intention['filtre_date'] else ''}."
            return {"answer": msg, "stream": msg, "sources": []}

        mots_a_ignorer = {
            "qui",
            "presente",
            "présente",
            "present",
            "est",
            "que",
            "pour",
            "dans",
            "avec",
            "sur",
            "quel",
            "quelle",
            "parle",
            "cette",
            "cet",
            "de",
            "du",
            "des",
            "le",
            "la",
            "les",
            "ce",
            "sujet",
            "thème",
            "theme",
            "présentation",
            "presentation",
            "overview",
        }

        mots_cles_q = [
            m.lower()
            for m in re.findall(r"\w+", question.lower())
            if len(m) > 1 and m.lower() not in mots_a_ignorer
        ]

        fiches_pertinentes = []

        if self.wiki_dir.exists():
            for md_file in sorted(list(self.wiki_dir.glob("*.md"))):
                if md_file.name in ["index.md", "log.md"]:
                    continue
                try:
                    text = md_file.read_text(encoding="utf-8", errors="ignore").strip()
                    text_lower = text.lower()
                    score = 0

                    for m in mots_cles_q:
                        if m in text_lower:
                            score += 2

                    if mots_cles_q and all(m in text_lower for m in mots_cles_q):
                        score += 10

                    if any(m in md_file.name.lower() for m in mots_cles_q):
                        score += 5

                    if score > 0:
                        fiches_pertinentes.append((score, md_file.name, text))
                except Exception:
                    continue

        fiches_pertinentes.sort(key=lambda x: x[0], reverse=True)

        if not fiches_pertinentes:
            msg = "Aucune information précise n'a été trouvée dans les fiches du Wiki."
            return {"answer": msg, "stream": msg, "sources": []}

        extraits = [item[2] for item in fiches_pertinentes[:2]]
        sources = [item[1] for item in fiches_pertinentes[:2]]
        terme_recherche = " ".join(mots_cles_q).title()

        if intention["est_sujet"]:
            apercu_section = self._extraire_section_apercu(extraits[0])
            return {
                "answer": apercu_section,
                "stream": apercu_section,
                "sources": sources,
            }

        elif intention["est_qui"]:
            reponse_propre = self._generer_reponse_personne(
                terme_recherche, extraits[0]
            )
            return {
                "answer": reponse_propre,
                "stream": reponse_propre,
                "sources": sources,
            }

        elif intention["est_qui_presente"]:
            presentateur = self._extraire_presentateur_par_balise(extraits[0])
            if presentateur:
                return {
                    "answer": presentateur,
                    "stream": presentateur,
                    "sources": sources,
                }
            contexte = "\n\n---\n\n".join(extraits)
            prompt = (
                f"Identifie qui présente la session sur '{terme_recherche}'.\n"
                f"Donne uniquement 'Nom Prénom — Fonction et Organisme'. Ne mets AUCUN intitulé du type 'Présentateur :' ou 'Hôte :'.\n\n"
                f"Contexte :\n{contexte[:4000]}"
            )
        else:
            contexte = "\n\n---\n\n".join(extraits)
            prompt = f"Réponds à la question : {question}\n\nContexte :\n{contexte[:4000]}"

        try:
            reponse = self._appeler_groq_api(prompt)
        except Exception:
            reponse = self._extraire_section_apercu(extraits[0])

        reponse_propre = self._nettoyer_prefixe_role(reponse)
        reponse_propre = self._nettoyer_chaine(reponse_propre)

        return {
            "answer": reponse_propre,
            "stream": reponse_propre,
            "sources": sources,
        }