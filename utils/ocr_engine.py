import easyocr
import ollama
import cv2
import numpy as np

reader_easyocr = easyocr.Reader(['fr', 'en'], gpu=True)
client = ollama.Client()

def extract_handwritten_content(pdf_path: str, page_num: int, clean_img_bytes: bytes) -> str:
    """Extraction du texte manuscrit via LLaVA Vision ou EasyOCR GPU."""
    try:
        res = client.generate(
            model="llava:latest",
            prompt="Transcris intégralement le texte manuscrit présent sur cette image. Ne fais aucun résumé.",
            images=[clean_img_bytes]
        )
        txt = res.get("response", "").strip()
        if len(txt) > 15:
            return txt
    except Exception as e:
        print(f"⚠️ Fallback EasyOCR GPU sur page {page_num}: {e}")

    # OCR EasyOCR GPU
    nparr = np.frombuffer(clean_img_bytes, np.uint8)
    cv_img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    results = reader_easyocr.readtext(cv_img, detail=0)
    return "\n".join(results).strip()
