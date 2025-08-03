# Buddy - Indic Language AI Assistant

## 1. AI Assistant Overview

**Assistant Name:** Buddy  
**Purpose & Target Audience:**  
Buddy is a friendly, multilingual student assistant designed to help Indian students in **Telugu, Hindi, and English**. Its primary aim is to make access to academic help, doubt solving, and general knowledge easier for Indic language speakers.

**Key Features:**
- Multilingual support: Telugu, Hindi, and English
- Simple, polite responses tailored for students
- Runs efficiently in a local/low-resource setup
- Feedback capture for continuous improvement
- Downloadable chat history
- Support for factual Q&A and general conversation

---

## 2. System Prompt Design and Justification

### Chosen Open-Source LLM & Environment

**LLM:** [`ai4bharat/IndicBART`](https://huggingface.co/ai4bharat/IndicBART)  
**Deployment/Interaction Environment:**  
We use a **local Python + Streamlit** setup. The `transformers` library loads the model for real-time inference. This ensures the app is free to run without API call costs, and it is truly open-source in both model and hosting.

### Full System Prompt


### Prompt Justification & Impact

- **Persona:** The assistant is named “Buddy” to create a student-friendly, non-intimidating experience.
- **Tone:** Polite and simple answers ensure accessibility for younger students and non-native English speakers.
- **Language Handling:** The prompt ensures support for three major Indian languages. IndicBART handles translation and generation reasonably well.
- **Constraints:** No long or verbose responses. Keeps clarity as priority.

### Iteration:
We modified decoding logic:
- Use **beam search** for short queries to reduce randomness.
- Allow sampling for longer or open-ended queries.

This change significantly reduced hallucinations like repetitive or nonsensical answers to factual questions.

---

## 3. User Reviews and Feedback Analysis

**Feedback Collection Plan:**  
We collected user feedback through a feedback form inside the app (`feedback.csv`).

| User ID | Date | Language | Purpose | Rating | Comment |
|---------|------|----------|---------|--------|---------|
| student_01 | 2025-08-02 | Hindi | GK question | 4 | “Good answer, slightly slow” |
| student_02 | 2025-08-02 | Telugu | Basic doubt | 5 | “Understood everything!” |

### Summary:
- **Accuracy:** 80% of queries were correctly answered
- **Clarity:** Very high for simple questions
- **Tone:** Polite and respectful
- **Issues Found:** Struggled with basic math and string repetition in factual queries like “What is 2 + 3?”

### Key Improvements Identified:
1. Improve math/factual grounding
2. Add fallback messages for unknown queries
3. Add a clearer language switch indicator

---

## 4. Future Roadmap

### Short-Term Goals (1 Week)
- Add math parsing for small arithmetic
- Improve clarity on language selection
- Polish the UI further with icons and speech-to-text

### Mid-Term Goals (2–4 Weeks)
- Add new Indic languages (e.g., Bengali, Marathi)
- Add RAG capability using `faiss` or custom datasets
- Allow voice input using `whisper` or `VOSK`

### Long-Term Vision (1+ Month)
- Make Buddy usable by rural students via mobile
- Build an offline APK using Streamlit’s mobile compatibility or Toga/Beeware
- Create learning pathways in Indian languages using Buddy

---

## 5. Plan to Increase User Adoption

### Acquisition:
- Share public repo on GitHub and Hugging Face Spaces
- Promote in regional student forums and Telegram groups
- Present to local colleges as free learning help

### Promotion:
- Tag as “Indic Learning Assistant” on GitHub
- Write blogs/tutorials on building open-source chatbots

### Feedback Loops:
- In-built feedback with CSV logging
- Future integration with Google Sheets for faster aggregation

### Community Growth:
- Accept community language patches via GitHub
- Encourage user testing in different dialects
- Collaborate with NGOs supporting education in regional languages

---

## License

This project is released under the **MIT License**, encouraging reuse, improvement, and educational access.

---

## Deployment

To run locally:

```bash
git clone https://github.com/<your-username>/buddy-assistant.git
cd buddy-assistant
pip install -r requirements.txt
streamlit run app.py
