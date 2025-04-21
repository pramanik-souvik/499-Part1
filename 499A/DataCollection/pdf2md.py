import os
import fitz  
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USERAS\AppData\Local\Programs\Tesseract-OCR\Tesseract.exe'

def pdf_page_to_image(pdf_path, page_number):
    doc = fitz.open(pdf_path)
    page = doc[page_number]
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

def ocr_image_to_text(image):
    return pytesseract.image_to_string(image, lang="ben")

def convert_scanned_pdf_to_markdown(pdf_path, output_path):
    try:
        doc = fitz.open(pdf_path)
        md_content = ""

        for page_number in range(len(doc)):
            print(f"Processing page {page_number + 1} of {pdf_path}...")
            image = pdf_page_to_image(pdf_path, page_number)
            text = ocr_image_to_text(image)
            md_content += f"## Page {page_number + 1}\n{text}\n\n"

        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)
        
        print(f"Converted: {pdf_path} -> {output_path}")
    except Exception as e:
        print(f"Failed to process {pdf_path}: {e}")

def convert_folder_to_markdown(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file_name)
            md_name = os.path.splitext(file_name)[0] + ".md"
            output_path = os.path.join(output_folder, md_name)

            convert_scanned_pdf_to_markdown(pdf_path, output_path)

if __name__ == "__main__":
    input_folder = "pdfs"
    output_folder = "markdown"

    convert_folder_to_markdown(input_folder, output_folder)
