import os
import json

def merge_json_files(input_folder, output_file):
    merged_data = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_folder, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    
                    if isinstance(data, list):
                        merged_data.extend(data)
                    else:
                        merged_data.append(data)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

    with open(output_file, "w", encoding="utf-8") as output:
        json.dump(merged_data, output, indent=4, ensure_ascii=False)
    print(f"Merged JSON saved to {output_file}")
if __name__ == "__main__":
    input_folder = input("Enter the path : ")
    output_file = "merged_data.json"
    merge_json_files(input_folder, output_file)
