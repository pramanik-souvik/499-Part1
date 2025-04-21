import json
import csv
from transformers import pipeline

# Use a model that supports text2text-generation
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/mt5-small",  # Multilingual model
    tokenizer="google/mt5-small",
    device=0  # Use CUDA if available
)

def generate_qa(context):
    prompt = f"Generate 3 relevant questions and answers based on the following text:\n\n{context}"
    
    # Enable beam search to allow multiple output sequences
    result = qa_pipeline(
        prompt,
        max_length=256,
        num_return_sequences=3,
        do_sample=False,
        num_beams=5,
        clean_up_tokenization_spaces=True
    )
    
    questions = []
    answers = []
    for qa in result:
        parts = qa["generated_text"].split("\n")
        if len(parts) >= 2:
            questions.append(parts[0])
            answers.append(parts[1])
    
    return questions, answers

# Process JSON file
def process_json(input_json, output_json):
    with open(input_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    qa_data = []
    for item in data:
        context = item["content"]
        questions, answers = generate_qa(context)
        qa_data.append({"context": context, "questions": list(zip(questions, answers))})

    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(qa_data, file, indent=4, ensure_ascii=False)

# Process CSV file
def process_csv(input_csv, output_csv):
    with open(input_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        context = row["content"]
        questions, answers = generate_qa(context)
        row["questions"] = "; ".join(questions)
        row["answers"] = "; ".join(answers)

    with open(output_csv, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["type", "content", "questions", "answers"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    process_json("merged_data.json", "qa_data.json")
    process_csv("merged_data.csv", "qa_data.csv")
