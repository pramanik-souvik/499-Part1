import os
import json
import csv
import markdown
import chardet

csv.field_size_limit(100000000)

def count_markdown_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            headings = [line for line in content.splitlines() if line.strip().startswith('#')]
            return len(headings), len(content.encode('utf-8'))
    except Exception as e:
        print(f"Error reading markdown file {file_path}: {e}")
        return 0, 0

def count_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return len(data), len(json.dumps(data).encode('utf-8'))
            elif isinstance(data, dict):
                return len(data.keys()), len(json.dumps(data).encode('utf-8'))
            else:
                return 0, 0
    except Exception as e:
        print(f"Error reading JSON file {file_path}: {e}")
        return 0, 0

def count_csv_data(file_path):
    try:
        with open(file_path, 'rb') as raw_file:
            result = chardet.detect(raw_file.read()) 
        with open(file_path, 'r', encoding=result['encoding']) as f:
            reader = csv.reader(f)
            rows = list(reader)
            return len(rows) - 1, os.path.getsize(file_path)
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
        return 0, 0

def analyze_data(directory):
    markdown_count, json_count, csv_count = 0, 0, 0
    markdown_size, json_size, csv_size = 0, 0, 0

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith('.md'):
            count, size = count_markdown_data(file_path)
            markdown_count += count
            markdown_size += size
        elif file_name.endswith('.json'):
            count, size = count_json_data(file_path)
            json_count += count
            json_size += size
        elif file_name.endswith('.csv'):
            count, size = count_csv_data(file_path)
            csv_count += count
            csv_size += size

    print("Data Summary:")
    print(f"Markdown - Total Entries: {markdown_count}, Size: {markdown_size} bytes")
    print(f"JSON - Total Entries: {json_count}, Size: {json_size} bytes")
    print(f"CSV - Total Entries: {csv_count}, Size: {csv_size} bytes")

if __name__=="__main__":
    data_directory = "data"  

    analyze_data(data_directory)