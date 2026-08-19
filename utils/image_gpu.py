import gc
import cv2
import fitz  # PyMuPDF
import numpy as np
import ollama
import torch


def process_scan_page(cv_image: np.ndarray) -> np.ndarray:
    """Remet la page en mode paysage si elle a été scanné verticalement."""
    h, w = cv_image.shape[:2]
    # Si la hauteur est supérieure à la largeur (A4 portrait), on bascule en paysage
    if h > w:
        cv_image = cv2.rotate(cv_image, cv2.ROTATE_90_CLOCKWISE)
    return cv_image


def preprocess_and_save_page_gpu(
    pdf_name: str, page_num: int, pdf_page_obj, dpi: int = 300
) -> tuple[bytes, str]:
    """
    Traitement d'image et extraction adaptative :
    - Texte informatique -> Extraction intégrale brute.
    - Scan / Manuscrit -> Extraction STRICTE : Nom, Prénom, E-mail uniquement.
    """
    # Nettoyage de la VRAM GPU pour éviter les Out-Of-Memory
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        gc.collect()

    # Rendu image HD (300 DPI recommandé pour le manuscrit)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    pix = pdf_page_obj.get_pixmap(matrix=mat, alpha=False)

    img_np = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.h, pix.w, pix.n
    )
    if pix.n == 3:
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Correction de l'orientation + encodage PNG
    clean_img = process_scan_page(img_np)
    _, buffer = cv2.imencode(".png", clean_img)
    clean_bytes = buffer.tobytes()

    # Détection de texte natif informatique
    native_text = pdf_page_obj.get_text().strip()
    has_native_text = len(native_text) > 40

    if has_native_text:
        print(f"  ⚡ [Page {page_num}] Texte natif informatique (Extraction intégrale)")
        return clean_bytes, native_text
    else:
        print(f"  👁️ [Page {page_num}] Scan/Manuscrit (Extraction STRICTE : Nom, Prénom, E-mail)")
        
        prompt_vlm = """
        Tu es un numériseur de document strict.
        Transcris les personnes présentes sur ce document scanné ou manuscrit.

        CONSIGNES STRICTES :
        1. Crée un tableau Markdown avec EXACTEMENT 3 colonnes : | Nom | Prénom | E-mail |
        2. Transcris UNIQUEMENT le Nom, le Prénom et l'E-mail réels écrits sur le document.
        3. N'inclus AUCUNE autre information (pas de signature, téléphone, poste, entreprise, etc.).
        4. Si une donnée est illisible ou manquante, laisse la case vide.
        5. Ne fais aucun résumé. Réponds UNIQUEMENT avec le tableau Markdown.
        """

        try:
            response = ollama.chat(
                model="minicpm-v",
                messages=[
                    {
                        "role": "user",
                        "content": prompt_vlm,
                        "images": [clean_bytes],
                    }
                ],
                options={"temperature": 0.0, "num_predict": 600},
            )
            extracted_text = response["message"]["content"].strip()
        except Exception as e:
            print(f"⚠️ Erreur VLM Vision : {e}")
            extracted_text = "[Erreur d'extraction manuscrit]"

        return clean_bytes, extracted_text