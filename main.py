import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from utils.ingest import IngestPipeline

SYSTEM_PROMPT_AGENT = """Vous êtes un agent IA chargé d'analyser les transcriptions de tout type de contenu (PDF, Audio, Vidéo, Images, Presentations, Archives, URLs, etc.). 
Pour chaque contenu traité, vous devez générer une fiche Markdown individuelle respectant strictement le modèle ci-dessous.

## ⚙️ Directives de Rédaction

1. **Niveau de détail (Moyen) :** Rédigez des explications concises et claires. Évitez les développements trop longs ou encyclopédiques, mais ne vous limitez pas non plus à de simples mots-clés.
2. **Pas de contenu artificiel ou "paracheté" :** Ne conservez que les sous-sections qui contiennent réellement de l'information (ex: s'il n'y a pas de chiffres ou de contradictions dans un chapitre, retirez simplement ces puces, ne les laissez pas vides).
3. **Champs non spécifiés :** Si une information générale (ex: lieu, présentateur) est absente du texte, indiquez simplement `Non précisé`.

---

# 📄 Fiche Synthèse : [Titre du contenu / de la vidéo]

---

## ℹ️ Informations Générales

* **Source :** [URL de la vidéo / Nom du fichier audio ou vidéo]
* **Thème de la présentation :** [Domaine général, ex: Intelligence Artificielle, Économie, Santé...]
* **Sujet principal :** [Le sujet précis abordé dans la vidéo]
* **Lieu / Cadre :** [Ex: Conférence Tech, Studio TV, Podcast, Distanciel, Non précisé...]
* **Présentateur / Hôte :** [Nom et rôle du présentateur ou "Non précisé"]
* **Liste des invités / Intervenants :**
  * **[Nom Intervenant 1]** — [Titre / Entreprise / Rôle]
  * **[Nom Intervenant 2]** — [Titre / Entreprise / Rôle]

---

## 🎯 Aperçu et Résumé Global
[Un résumé synthétique de 3 à 5 phrases présentant le sujet, l'objectif central et les conclusions principales de la vidéo.]

---

## 📌 Sujets Discutés (Résumé Moyen)

### 1. [Titre du 1er grand thème]
* **Développement de l'idée :** Synthèse équilibrée de l'argument ou du concept présenté (3 à 5 lignes concises).
* **Chiffres & Données clés :** *(À inclure uniquement si présent dans la vidéo)*
  * 📈 **[Chiffre/Statistique]** [Description courte]
* **Citation / Point marquant :** *(À inclure uniquement si une phrase clé ressort)*
  > *"Citation pertinente de l'intervenant."*

### 2. [Titre du 2ème grand thème]
* **Développement de l'idée :** Explication claire et directe des arguments clés abordés.
* **Chiffres & Données clés :** *(À inclure uniquement si présent)*
  * 📊 **[Chiffre/Statistique]** [Description courte]

*(Ajoutez d'autres chapitres uniquement si le contenu le nécessite)*

---

## 🔑 Points Principaux à Retenir (Takeaways)

* 🔹 **Point 1 :** [Enseignement ou conclusion majeure n°1]
* 🔹 **Point 2 :** [Enseignement ou conclusion majeure n°2]
* 🔹 **Point 3 :** [Recommandation ou perspective finale]

---

## 📜 Transcription Textuelle (Intégrale)

<details>
<summary>Cliquez ici pour dérouler le texte intégral extrait du fichier</summary>

[Insérer ici la transcription complète brute ou horodatée]

</details>
"""


def log_ingestion_event(file_name: str, target_wiki: str, details: str = ""):
    """Ajoute une entrée d'historique structurée dans wiki/log.md."""
    wiki_dir = Path("wiki")
    wiki_dir.mkdir(exist_ok=True)
    log_file = wiki_dir / "log.md"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- `{file_name}` {details} ➔ [[{target_wiki}]]\n"

    if not log_file.exists():
        log_file.write_text(f"## Passage Ingest - {now_str}\n{entry}", encoding="utf-8")
        return

    content = log_file.read_text(encoding="utf-8")
    header = f"## Passage Ingest - {now_str}"
    
    if header in content:
        content += entry
    else:
        content += f"\n\n{header}\n{entry}"

    log_file.write_text(content, encoding="utf-8")


def process_file(file_path: Path, pipeline: IngestPipeline):
    output_dir = Path("wiki")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{file_path.stem}.md"

    if output_file.exists():
        print(f"⏩ Fichier déjà traité (ignoré) : {file_path.name}")
        return

    print(f"\n🎯 Traitement du fichier : {file_path.name}")

    parent_folder = file_path.parent.name
    context_tag = parent_folder if parent_folder.lower() != "raw" else "Général"

    # 1. Extraction du texte
    raw_text = pipeline.process_any_file(file_path, context_tag)

    if not raw_text or not raw_text.strip():
        print(f"⚠️ Aucun texte exploitable extrait du fichier : {file_path.name}")
        return

    # 2. Vérification sécurisée de la feuille de présence
    is_attendance = (
        hasattr(pipeline, "_is_attendance_sheet") 
        and pipeline._is_attendance_sheet(raw_text, file_path.name)
    )

    if is_attendance and hasattr(pipeline, "_post_correct_markdown"):
        final_markdown = pipeline._post_correct_markdown(raw_text, context_tag, file_path.name)
        log_details = "(VLM (Scan/Manuscrit))"
    else:
        print("[AGENT IA] Génération de la Fiche Synthèse via Groq (Llama 3)...")
        user_prompt = f"""Nom du fichier / Source : {file_path.name}
Contexte / Événement : {context_tag}

Voici le texte intégral extrait à synthétiser :
------------------------------------
{raw_text}
------------------------------------

Consigne finale : Génère la Fiche Synthèse complète selon le modèle strict fourni. Remplace le bloc '[Insérer ici la transcription complète brute ou horodatée]' à la fin par l'intégralité du texte extrait ci-dessus."""

        prompt_complet = f"{SYSTEM_PROMPT_AGENT}\n\n{user_prompt}"
        final_markdown = pipeline._call_mistral_chat(prompt_complet)
        log_details = f"({file_path.suffix.upper()})"

    # 3. Sauvegarde et journalisation
    output_file.write_text(final_markdown, encoding="utf-8")
    log_ingestion_event(file_path.name, output_file.stem, log_details)
    print(f"✅ Fiche Synthèse générée avec succès : {output_file}")


if __name__ == "__main__":
    pipeline = IngestPipeline()

    if len(sys.argv) >= 2:
        input_argument = sys.argv[1]
        target_path = Path(input_argument)

        if not target_path.exists():
            raw_path = Path("raw") / input_argument
            if raw_path.exists():
                target_path = raw_path
            else:
                print(f"❌ Introuvable : '{input_argument}' ni dans ./ ni dans ./raw/")
                sys.exit(1)

        if target_path.is_file():
            process_file(target_path, pipeline)
        elif target_path.is_dir():
            print(f"🔍 Traitement du dossier : {target_path} ...")
            for file in target_path.rglob("*"):
                if file.is_file():
                    try:
                        process_file(file, pipeline)
                    except Exception as e:
                        print(f"❌ Erreur sur {file.name} : {e}")
    else:
        raw_dir = Path("raw")
        if not raw_dir.exists() or not any(raw_dir.iterdir()):
            print("⚠️ Le dossier 'raw' est vide ou introuvable.")
            sys.exit(0)

        print("🔍 Exploration récursive du dossier ./raw/ ...")
        for file in raw_dir.rglob("*"):
            if file.is_file():
                try:
                    process_file(file, pipeline)
                except Exception as e:
                    print(f"❌ Erreur sur {file.name} : {e}")