import os
import re
from datetime import datetime

def lint_wiki(wiki_dir: str = "wiki") -> dict:
    """Analyse la structure du wiki en lecture seule."""
    if not os.path.exists(wiki_dir):
        return {"orphans": [], "broken_links": [], "total_pages": 0}

    # Liste uniquement les fichiers .md (en excluant log.md et index.md de l'analyse)
    files = [f for f in os.listdir(wiki_dir) if f.endswith(".md")]
    
    page_names = {os.path.splitext(f)[0] for f in files}
    page_names_lower = {p.lower(): p for p in page_names}
    
    incoming_links = {page: 0 for page in page_names}
    broken_links = []

    # Termes génériques ou fiches spéciales à ignorer
    IGNORE_TARGETS = {"index", "log", "wikilinks", "liste_des_invites"}

    for filename in files:
        filepath = os.path.join(wiki_dir, filename)
        
        # LECTURE SEULE : aucun fichier existant n'est modifié
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        # Recherche des [[Wikilinks]]
        links = re.findall(r"!?\[\[(.*?)\]\]", content)
        for link in links:
            target = link.split("|")[0].strip()  # Extraction de la cible avant '|'
            
            # Nettoyage de l'extension .md
            if target.lower().endswith(".md"):
                target = target[:-3]

            target_lower = target.lower()

            # Vérification de la validité du lien
            if target_lower in page_names_lower:
                real_page_name = page_names_lower[target_lower]
                incoming_links[real_page_name] += 1
            elif target_lower not in IGNORE_TARGETS and target != "":
                broken_links.append({"source": filename, "target": target})

    # Détection des fiches orphelines (sans aucun lien entrant)
    orphans = [
        page for page, count in incoming_links.items() 
        if count == 0 and page.lower() not in IGNORE_TARGETS
    ]

    return {
        "orphans": orphans,
        "broken_links": broken_links,
        "total_pages": len(files)
    }


def append_lint_result_to_log(results: dict, wiki_dir: str = "wiki"):
    """
    Ajoute uniquement le résultat à la fin de wiki/log.md
    sans toucher aux autres fiches du dossier.
    """
    log_path = os.path.join(wiki_dir, "log.md")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Mise en forme du bloc de résultat
    entry = [
        f"\n## 🛠️ Rapport Linting Wiki - {now_str}",
        f"- **Pages analysées :** {results['total_pages']}"
    ]

    if results["orphans"]:
        entry.append("- **Pages orphelines :**")
        for orphan in results["orphans"]:
            entry.append(f"  - ⚠️ [[{orphan}]]")
    else:
        entry.append("- **Pages orphelines :** Aucune 🎉")

    if results["broken_links"]:
        entry.append("- **Liens cassés :**")
        for item in results["broken_links"]:
            entry.append(f"  - ❌ `{item['source']}` ➔ [[{item['target']}]]")
    else:
        entry.append("- **Liens cassés :** Aucun 🎉")

    formatted_text = "\n".join(entry) + "\n"

    # Mode 'a' (append) : Écrit uniquement à la fin de log.md sans écraser le contenu
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    print(f"✅ Rapport de vérification consigné dans {log_path}")


if __name__ == "__main__":
    # Exécution du linting et écriture dans log.md
    report = lint_wiki()
    append_lint_result_to_log(report)