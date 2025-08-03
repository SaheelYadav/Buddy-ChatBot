import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import csv
from datetime import datetime
import pandas as pd

# Page config
st.set_page_config(page_title="Buddy - Indic Student Chatbot", layout="centered")

# Load model
@st.cache_resource
def load_model():
    model_name = "ai4bharat/IndicBART"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# System prompt
system_prompt = "You are Buddy, a friendly assistant who helps students in Telugu, Hindi, or English. You give simple and polite answers."

# Response function
def indic_answer(query):
    input_text = f"{system_prompt}\nQuestion: {query}\nAnswer:"
    inputs = tokenizer([input_text], return_tensors="pt", padding=True)

    is_short = len(query.strip()) < 25

    output = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=100,
        do_sample=not is_short,
        temperature=0.8 if not is_short else 1.0,
        top_k=50 if not is_short else 0,
        top_p=0.95 if not is_short else 1.0,
        num_beams=4 if is_short else 1
    )

    raw_output = tokenizer.decode(output[0], skip_special_tokens=True)

    # Clean up output
    cleaned = raw_output.replace(system_prompt, "")
    cleaned = cleaned.replace("Question:", "").replace("Answer:", "").strip()
    return cleaned

# UI: Title
st.title("🤖 Buddy - Indic Student Chatbot")
st.markdown("Ask me anything in **Telugu**, **Hindi**, or **English**!")

# Chat state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="user_input")

# Handle input
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        response = indic_answer(user_input)
        st.session_state.chat_history.append(("Buddy", response))

# Display chat
st.markdown("### 💬 Conversation")
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")

# Feedback
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### 🙋 Rate Buddy's Response")
    rating = st.slider("How helpful was Buddy?", 1, 5, 3)
    comment = st.text_input("Your suggestion or feedback")

    if st.button("Submit Feedback"):
        with open("feedback.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now(),
                user_input,
                st.session_state.chat_history[-1][1],
                rating,
                comment
            ])
        st.success("✅ Feedback submitted!")

# Clear chat
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# Download chat
if st.session_state.chat_history:
    df = pd.DataFrame(st.session_state.chat_history, columns=["Sender", "Message"])
    st.download_button("📥 Download Chat", df.to_csv(index=False), "chat_history.csv", "text/csv")

# Footer
st.markdown("""
<hr style='margin-top: 50px;'>
<p style='text-align: center; font-size: 14px; color: gray;'>
© 2025 Buddy AI • Open-Source for Educational Use 🇮🇳
</p>
""", unsafe_allow_html=True)
