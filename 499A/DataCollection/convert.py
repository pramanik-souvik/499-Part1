import os
import json
import csv
from markdown import markdown
from bs4 import BeautifulSoup

def parse_markdown_to_structure(md_content):
    html_content = markdown(md_content)
    soup = BeautifulSoup(html_content, "html.parser")

    data = []
    for section in soup.find_all():
        tag = section.name
        text = section.get_text(strip=True)
        data.append({"type": tag, "content": text})
    return data

def convert_markdown_to_json_and_csv(md_path, json_path, csv_path):
    try:
        with open(md_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        structured_data = parse_markdown_to_structure(md_content)

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(structured_data, json_file, ensure_ascii=False, indent=4)

        with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["type", "content"])
            writer.writeheader()
            writer.writerows(structured_data)

        print(f"Converted: {md_path} -> {json_path}, {csv_path}")
    except Exception as e:
        print(f"Failed to process {md_path}: {e}")

def convert_folder_to_json_and_csv(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".md"):
            md_path = os.path.join(input_folder, file_name)
            base_name = os.path.splitext(file_name)[0]
            json_path = os.path.join(output_folder, f"{base_name}.json")
            csv_path = os.path.join(output_folder, f"{base_name}.csv")

            convert_markdown_to_json_and_csv(md_path, json_path, csv_path)

if __name__ == "__main__":
    input_folder = "markdown"
    output_folder = "output"
    
    convert_folder_to_json_and_csv(input_folder, output_folder)
