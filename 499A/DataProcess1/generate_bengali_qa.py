import pandas as pd

# Load the processed CSV
file_path = "processed_output1.csv"  # Change path if needed
df = pd.read_csv(file_path)

# Function to generate 5 Bengali Q&A pairs from a given text
def generate_qa_pairs(text):
    questions = [
        "এই লেখার মূল বিষয়বস্তু কী?",
        "এতে কী ঐতিহাসিক ঘটনা বর্ণনা করা হয়েছে?",
        "লেখাটি কোন সময়কাল নিয়ে আলোচনা করে?",
        "এতে উল্লেখযোগ্য ব্যক্তি বা ঘটনাবলি কী কী?",
        "এর প্রেক্ষাপট কী ছিল?"
    ]
    # For now, using the source text as answer placeholder
    qa_pairs = [{"question": q, "answer": text} for q in questions]
    return qa_pairs

# List to hold final Q&A dataset
qa_data = []

# Iterate through each row to generate Q&A
for idx, row in df.iterrows():
    # Use passage if it's valid, otherwise fallback to content
    source_text = row["passage"] if isinstance(row["passage"], str) and len(row["passage"]) > 100 else row["content"]
    qa_pairs = generate_qa_pairs(source_text)
    for qa in qa_pairs:
        qa_data.append({
            "id": idx + 1,
            "original_title": row["title"],
            "source_text": source_text,
            "question": qa["question"],
            "answer": qa["answer"]
        })

# Create final Q&A DataFrame
qa_df = pd.DataFrame(qa_data)

# Save to CSV
output_file = "bengali_history_qa_dataset.csv"
qa_df.to_csv(output_file, index=False)
print(f"✅ Q&A dataset saved to {output_file}")
