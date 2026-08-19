import ollama

def auto_validate_and_correct(raw_text: str, file_name: str, page_num: int, model_name: str = "llama3:latest") -> str:
    """Correction automatique et intelligente de la transcription manuscrite."""
    if not raw_text.strip():
        return ""

    print(f"🤖 [Auto-Validation Agent] Correction de la page {page_num}...")

    prompt = f"""
Vous êtes un expert en correction de fautes d'OCR sur documents manuscrits.

Voici le texte brut extrait par un OCR depuis un manuscrit ({file_name}, page {page_num}) :
---
{raw_text}
---

MISSION :
1. Corrigez les erreurs de lecture de l'OCR (lettres mal lues, mots tronqués, ponctuation cassée).
2. Ne modifiez PAS le sens et ne RACCOURCISSEZ PAS le texte. Conservation à 100%.
3. Renvoyez uniquement le texte corrigé et propre, sans aucun texte d'introduction.
"""

    try:
        res = ollama.generate(
            model=model_name,
            prompt=prompt,
            options={"temperature": 0.1}
        )
        return res.get("response", "").strip()
    except Exception as e:
        print(f"❌ Erreur Auto-Validation : {e}")
        return raw_text
