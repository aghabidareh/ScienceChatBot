import re
import os

def preprocess(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.،؟!]", "", text)
    return text


def preprocess_all(input_folder, combined_file):
    combined_text = ""
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            combined_text += preprocess(text) + "\n"

    with open(combined_file, "w", encoding="utf-8") as f:
        f.write(combined_text)


input_folder = "data"
combined_file = "data/combined/combined_text.txt"
preprocess_all(input_folder, combined_file)
