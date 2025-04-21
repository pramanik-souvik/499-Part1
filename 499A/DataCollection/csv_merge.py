import os
import pandas as pd

def merge_csv_files(input_folder, output_file):
    merged_data = pd.DataFrame()

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(input_folder, file_name)
            try:
                data = pd.read_csv(file_path)
                merged_data = pd.concat([merged_data, data], ignore_index=True)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

    merged_data.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"Merged CSV saved to {output_file}")

if __name__ == "__main__":
    input_folder = input("Enter the path: ")
    output_file = "merged_data.csv"
    merge_csv_files(input_folder, output_file)

