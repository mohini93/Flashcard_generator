import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
from flashcards_generator import generate_flashcards
from utils import extract_text_from_file, save_as_csv, save_as_json
import pandas as pd

# ========== Page Configuration ==========
st.set_page_config(page_title="LLM Flashcard Generator", layout="wide")

# ========== Background Style ==========
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f9ff;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.05);
        }
        .stTextInput, .stTextArea, .stSelectbox, .stButton {
            border-radius: 8px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_background()

st.markdown("<h1 style='text-align: center; color: #035e7b;'>🧠 AI Flashcard Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Powered by FLAN-T5 | Generate smart flashcards from PDFs or notes</p>", unsafe_allow_html=True)

# ========== Upload/Input Section ==========
with st.container():
    st.markdown("### 📥 Upload or Paste Content")
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
    with col2:
        subject = st.selectbox("📘 Select Subject (optional)", ["General", "Biology", "History", "Computer Science"])
    text_input = st.text_area("✍️ Or paste educational content below:", height=180)

# ========== Load Text ==========
@st.cache_data(show_spinner="📄 Extracting text from file...")
def load_file_text(file):
    return extract_text_from_file(file)

input_text = ""
if uploaded_file:
    input_text = load_file_text(uploaded_file)
elif text_input:
    input_text = text_input

# ========== Flashcard Generation ==========
if st.button("⚡ Generate Flashcards") and input_text:

    @st.cache_data(show_spinner="🤖 Generating flashcards with FLAN-T5...")
    def cached_generate(text):
        return generate_flashcards(text)

    flashcards = cached_generate(input_text)

    if flashcards:
        st.success(f"✅ Generated {len(flashcards)} flashcards!")
        st.divider()
        st.markdown("### ✏️ Edit Your Flashcards")

        edited_data = []

        with st.form("flashcard_edit_form"):
            for i, card in enumerate(flashcards, 1):
                st.markdown(f"#### 🗂️ Flashcard {i}")
                q = st.text_input(f"🧐 Question {i}", value=card["Question"], key=f"q{i}")
                a = st.text_input(f"💡 Answer {i}", value=card["Answer"], key=f"a{i}")
                d = st.selectbox(f"📊 Difficulty {i}", ["Easy", "Medium", "Hard"],
                                 index=["Easy", "Medium", "Hard"].index(card["Difficulty"]),
                                 key=f"d{i}")
                edited_data.append({"Question": q, "Answer": a, "Difficulty": d})
                st.markdown("---")

            submitted = st.form_submit_button("💾 Save Edited Flashcards")

        if submitted:
            st.success("🎉 Flashcards saved successfully!")

        # ========== Export Section ==========
        st.markdown("### 📤 Export Your Flashcards")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬇️ Export as CSV"):
                csv_file = save_as_csv(edited_data)
                st.download_button("Download CSV", open(csv_file, "rb"), file_name="flashcards.csv")
        with col2:
            if st.button("⬇️ Export as JSON"):
                json_file = save_as_json(edited_data)
                st.download_button("Download JSON", open(json_file, "rb"), file_name="flashcards.json")
    else:
        st.error("❌ No flashcards could be generated. Try a different input.")
