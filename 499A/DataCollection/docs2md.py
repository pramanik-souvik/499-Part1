import os
from docx import Document

def docx_to_markdown(docx_path, output_path):
    try:
        doc = Document(docx_path)
        md_content = ""

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:
                if paragraph.style.name.startswith("Heading"):
                    level = int(paragraph.style.name[-1])
                    md_content += f"{'#' * level} {text}\n\n"
                else:
                    md_content += f"{text}\n\n"

        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)
        
        print(f"Converted: {docx_path} -> {output_path}")
    except Exception as e:
        print(f"Failed to process {docx_path}: {e}")

def convert_folder_to_markdown(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".docx"):
            docx_path = os.path.join(input_folder, file_name)
            md_name = os.path.splitext(file_name)[0] + ".md"
            output_path = os.path.join(output_folder, md_name)

            docx_to_markdown(docx_path, output_path)

if __name__ == "__main__":
    input_folder = "docs"
    output_folder = "markdown"

    convert_folder_to_markdown(input_folder, output_folder)
