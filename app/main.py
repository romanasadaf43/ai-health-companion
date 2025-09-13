from ocr_module import extract_text_from_image
from llm_module import analyze_text

def process_report(image_path):
    # Step 1: OCR - Extract text from lab report
    extracted_text = extract_text_from_image(image_path)
    print("\n📝 OCR Extracted Text:\n", extracted_text)

    # Step 2: LLM - Analyze extracted text
    analysis = analyze_text(extracted_text)
    print("\n🤖 AI Health Companion Analysis:\n", analysis)

if __name__ == "__main__":
    # Test with sample lab report image
    process_report("data/sample_report.jpg")

