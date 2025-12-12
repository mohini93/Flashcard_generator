# 🧠 LLM-Powered Flashcard Generator

This is a lightweight yet powerful **Flashcard Generator** that uses a Hugging Face Large Language Model to convert educational content into **question-answer flashcards**. Built using **Python** and **Streamlit**, it supports `.txt` / `.pdf` input, auto-generates 15 flashcards, allows editing, and offers export to **CSV** and **JSON** formats.

---

## 🔍 Project Overview

Many students and educators need an efficient way to revise key concepts from long academic texts. This tool reads textbook or lecture content and turns it into editable flashcards — saving time, improving retention, and making study smarter.

---
| Library        | Purpose                                    |
| -------------- | ------------------------------------------ |
| `transformers` | LLM loading (`valhalla/t5-small-qa-qg-hl`) |
| `torch`        | Backend for model execution (PyTorch)      |
| `streamlit`    | Web interface for interaction              |
| `PyMuPDF`      | Extracting text from `.pdf` files          |
| `pandas`       | Flashcard export (CSV, JSON)               |

---
## ✅ Features

- Upload `.txt` or `.pdf` documents
- Paste raw educational text directly
- Generate up to **15 question-answer flashcards**
- Each flashcard includes:
  - **Question**
  - **Answer**
  - **Difficulty Level** (Easy, Medium, Hard)
- Edit questions & answers before exporting
- Export to:
  - CSV
  - JSON

---

## 📸 Screenshot

![Screenshot 2025-06-17 151923](https://github.com/user-attachments/assets/19c6512b-d0c8-4ebe-8b8d-db65880797a9)
![Screenshot 2025-06-17 152240](https://github.com/user-attachments/assets/c141fee3-81c8-4e98-9c81-1e6ec72247ac)



---

## 📦 Folder Structure
<pre> flashcard_generator/ ├── app.py # Streamlit UI logic ├── flashcard_generator.py # Core logic to generate Q&A flashcards ├── utils.py # File upload parsing and export helpers ├── prompt_template.txt # Optional prompt format (for instruction-tuned models) ├── requirements.txt # Python dependencies └── README.md # Project documentation </pre>

---

## 🧠 How It Works

1. The app uses Hugging Face’s `valhalla/t5-small-qa-qg-hl` model.
2. It highlights sentences to generate questions using a special prompt.
3. Each flashcard is tagged with a difficulty level based on sentence length.
4. Flashcards can be edited in the browser.
5. Final cards are exported as `.csv` or `.json`.

---
## Short Demo Video
https://www.loom.com/share/e798fceab7cb47cfbbde2e65146c3910?sid=08659b1a-dc5b-4366-a34d-43251db61075

## Setup Guide
# 1. Clone the repository
git clone https://github.com/your-username/flashcard-generator.git
cd flashcard-generator

# 2. (Optional) Create and activate a virtual environment
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py




