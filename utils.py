import fitz  # PyMuPDF
import pandas as pd
import json

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    return ""

def save_as_csv(flashcards, filename="flashcards.csv"):
    df = pd.DataFrame(flashcards)
    df.to_csv(filename, index=False)
    return filename

def save_as_json(flashcards, filename="flashcards.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(flashcards, f, indent=2)
    return filename
