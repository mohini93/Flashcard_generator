
#This file contains the logic to convert academic text into flashcards using a Hugging Face model.
#Hugging face tools
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM #AutoTokenizer: breaks input text into tokens.
                        #AutoModelForSeq2SeqLM: loads a pre-trained text generation model (sequence-to-sequence)
import torch # needed to run the model and manage tensors (like arrays).

model_name = "valhalla/t5-small-qa-qg-hl" #Hugging Face
#It’s trained for question generation from highlighted text.
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)  # ✅ use_fast=False to avoid SentencePiece error
model = AutoModelForSeq2SeqLM.from_pretrained(model_name) #This model can generate questions from text (Seq2Seq = Sequence-to-Sequence).



def generate_flashcards(text, max_cards=15): #Defines a function to generate flashcards from input text
    sentences = [s.strip() for s in text.strip().split('.') if len(s.strip().split()) > 5] #Removes short sentences (less than 6 words) to avoid useless questions
    flashcards = [] #Creates an empty list to store flashcards.

    for sent in sentences[:max_cards]:
        if not sent: #Skips empty sentences.
            continue
        hl_context = text.replace(sent, f"<hl> {sent} <hl>")
        prompt = f"generate question: {hl_context}"

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=64,
                num_beams=4,
                do_sample=False
            )

        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Converts generated tokens back to text.
        #Removes extra special symbols.
        difficulty = "Easy" if len(sent.split()) < 10 else "Medium" if len(sent.split()) < 20 else "Hard"
        flashcards.append({
            "Question": question.strip(),
            "Answer": sent,
            "Difficulty": difficulty
        })

    return flashcards
#SentencePiece may split it into:
#["un", "believ", "able"]
