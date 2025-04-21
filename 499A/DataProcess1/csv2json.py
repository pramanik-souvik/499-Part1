import csv
import json

def csv_to_json(csv_file, json_file):

    data = []

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Conversion complete: {csv_file} → {json_file}")

if __name__ == "__main__":
    csv_file = "data.csv"
    json_file = "data.json"
    csv_to_json(csv_file, json_file)
