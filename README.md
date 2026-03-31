# 📄 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

An intelligent, sleek, and modern web application built with Python and Streamlit to help candidates optimize their resumes. It parses PDF and DOCX files, intelligently extracts technical skills, matches them against target job descriptions, and calculates a percentage-based **ATS (Applicant Tracking System) Matchscore.** Featuring a premium custom UI with real-time insightful feedback, it helps you quickly identify missing skills to increase your parsing success rates.

## ✨ Features

- **📤 Upload Resume:** Drag-and-drop parsing for both `.pdf` and `.docx` file formats.
- **🧠 Extracted Resume Skills:** Uses natural language logic to correctly identify your technical abilities from plain text.
- **🧩 Skill Categories:** Neatly organizes your detected skills into domain categories (Programming, ML, Cloud, Database, Web Dev).
- **🎯 Job Description Skills:** Dynamically extracts the required and preferred skills directly from the pasted job description.
- **✅ Matched & ❌ Missing Skills:** Clearly lists the overlap (what you have) and the gaps (what you need to learn or add to the resume).
- **📊 Resume Matchscore:** Calculates an exact, weighted percentage ATS score based on the JD to see how you stack up.
- **📝 ATS Feedback:** Provides immediate, color-coded alerts and distinctly highlights the most critical missing skills so you know exactly what to improve before applying.

## 🎨 Premium UI
Featuring a fully custom-styled, elegant light-theme interface. The application utilizes soft shadows, crisp typography (Outfit font), subtle border highlights, gradient buttons, and responsive animated containers to provide an exceptional user experience on top of the native Streamlit layout.

## 🚀 Installation & Local Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/Ushasri-Dasari/AI-Ats-Resume-Analyzer.git
   cd AI-Ats-Resume-Analyzer
   ```

2. **Create and Activate a Virtual Environment** (Recommended)
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```
   The application will instantly launch in your default web browser at `http://localhost:8501`.

## 🛠️ Technology Stack
- **Dashboard Framework:** [Streamlit](https://streamlit.io/)
- **Text Processing:** `nltk`, `scikit-learn`
- **File Parsing:** `PyPDF2`, `python-docx`
- **Styling:** Custom CSS Injection

---
*Developed by Ushasri Dasari*
