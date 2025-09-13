import pytesseract
from PIL import Image
import os

# Use existing Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from a medical report image using OCR.
    Returns extracted text as a string.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()


if __name__ == "__main__":
    sample_image = "data/sample_report.jpg"  # ✅ correct path
    try:
        text = extract_text_from_image(sample_image)
        print("✅ OCR Extracted Text:\n", text)
    except Exception as e:
        print("❌ Error:", e)
