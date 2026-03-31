# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from text_preprocessing import clean_text
from skills import extract_skills
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="centered"
)

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")

# ================= SKILL CATEGORIES =================
SKILL_CATEGORIES = {
    "Programming": ["python", "r", "java", "c++"],
    "ML Frameworks": ["tensorflow", "pytorch", "scikit-learn"],
    "Machine Learning": ["machine learning", "deep learning", "nlp"],
    "Web Development": ["django", "flask", "fastapi"],
    "Database": ["sql", "mysql", "postgresql"],
    "Cloud": ["aws", "azure", "gcp"]
}

# ================= STREAMLIT CONFIG =================
st.markdown("""
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
    <div style="background: linear-gradient(135deg, #4f46e5, #3b82f6); width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(79, 70, 229, 0.25);">
        <span style="color: white; font-size: 20px;">📄</span>
    </div>
    <h1 style="margin: 0; font-size: 28px; font-weight: 700; background: linear-gradient(to right, #1e293b, #334155); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">AI Resume Analyzer</h1>
</div>
<hr style="margin-top: 0; border: none; border-top: 1px solid #e2e8f0; margin-bottom: 30px;">
""", unsafe_allow_html=True)

# ---------- STARTING UI (Styled Cards) ----------

with st.container(border=True):
    st.markdown("<div class='section-title'>📤 Upload Resume</div>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Drag & drop your resume here",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )

st.write("")

with st.container(border=True):
    col_title, col_link = st.columns([0.8, 0.2])
    with col_title:
        st.markdown("<div class='section-title'>💼 Paste Job Description Here</div>", unsafe_allow_html=True)
    with col_link:
        if "jd_text_val" not in st.session_state:
            st.session_state.jd_text_val = ""
            
        def load_sample():
            st.session_state.jd_text_val = "Friendly and innovative work environment\n📌 Example Projects (Good to Have)\nFull-stack web application\nREST API project\nMini AI/ML project\nOpen-source contributions\n📫 How to Apply\n\nSend your resume and portfolio (GitHub/LinkedIn) to: careers@xyztech.com"
            
        st.button("Load sample", type="tertiary", on_click=load_sample, use_container_width=True)

    jd_text = st.text_area(
        "Job Description",
        key="jd_text_val",
        placeholder="Paste the job description here...",
        height=200,
        label_visibility="collapsed"
    )

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    analyze = st.button("Analyze Resume", type="primary", use_container_width=True)

# ---------- END STARTING UI ----------


if analyze and uploaded_file and jd_text:

    # ================= EXTRACT RESUME TEXT =================
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    # ================= CLEAN TEXT =================
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    # ================= EXTRACT RESUME SKILLS =================
    resume_skills = list(set(extract_skills(clean_resume)))

    # ================= CATEGORIZE RESUME SKILLS =================
    categorized_skills = {}

    for category, skills in SKILL_CATEGORIES.items():
        matched = set(skills) & set(resume_skills)
        if matched:
            categorized_skills[category] = list(matched)

    # ================= SPLIT JD INTO REQUIRED & PREFERRED =================
    jd_lower = jd_text.lower()

    required_text = ""
    preferred_text = ""

    # Extract Required Skills section safely
    if "required skills" in jd_lower:
        parts = jd_lower.split("required skills")
        if len(parts) > 1:
            required_section = parts[1]
            required_text = required_section.split("preferred skills")[0]

            if "preferred skills" in required_section:
                required_text = required_section.split("preferred skills")[0]
            else:
                required_text = required_section

    # Extract Preferred Skills section safely
    if "preferred skills" in jd_lower:
        parts = jd_lower.split("preferred skills")
        if len(parts) > 1:
            preferred_text = parts[1]

    # ================= EXTRACT JD SKILLS =================
    required_skills = list(set(extract_skills(clean_text(required_text))))
    preferred_skills = list(set(extract_skills(clean_text(preferred_text))))

    jd_skills = list(set(required_skills + preferred_skills))

    # ================= MATCHING =================
    matched_skills = list(set(jd_skills) & set(resume_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    matched_required = list(set(required_skills) & set(resume_skills))
    matched_preferred = list(set(preferred_skills) & set(resume_skills))

    # ================= SCORE CALCULATION =================
    required_score = (
        (len(matched_required) / len(required_skills)) * 100
        if len(required_skills) > 0 else 0
    )

    preferred_score = (
        (len(matched_preferred) / len(preferred_skills)) * 100
        if len(preferred_skills) > 0 else 0
    )

    final_score = (required_score * 0.7) + (preferred_score * 0.3)

    # ================= DISPLAY SECTION =================

    # ================= DISPLAY SECTION =================

    # 1. Extracted Resume Skills
    with st.container(border=True):
        st.markdown("<div class='section-title'>🧠 Extracted Resume Skills</div>", unsafe_allow_html=True)
        if resume_skills:
            skills_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in resume_skills])
            st.markdown(skills_html, unsafe_allow_html=True)
        else:
            st.write("No skills found.")

    st.write("")

    # 2. Skill Categories
    with st.container(border=True):
        st.markdown("<div class='section-title'>🧩 Skill Categories</div>", unsafe_allow_html=True)
        if categorized_skills:
            for category, skills in categorized_skills.items():
                st.markdown(f"**{category}:** {', '.join(skills)}")
        else:
            st.write("No categorized skills detected.")

    st.write("")

    # 3. Job Description skills
    with st.container(border=True):
        st.markdown("<div class='section-title'>🎯 Job Description Skills</div>", unsafe_allow_html=True)
        if jd_skills:
            jd_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in jd_skills])
            st.markdown(jd_html, unsafe_allow_html=True)
        else:
            st.write("No skills found.")

    st.write("")

    # 4. Matched Skills / Missing Skills Columns
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("<div class='section-title'>✅ Matched Skills</div>", unsafe_allow_html=True)
            for skill in matched_skills:
                st.markdown(f"✅ {skill}")
            if not matched_skills:
                st.write("None")

    with col2:
        with st.container(border=True):
            st.markdown("<div class='section-title'>❌ Missing Skills</div>", unsafe_allow_html=True)
            for skill in missing_skills:
                st.markdown(f"❌ {skill}")
            if not missing_skills:
                st.write("None")

    st.write("")

    # 5. Resume Matchscore
    with st.container(border=True):
        st.markdown("<div class='section-title'>📊 Resume Matchscore</div>", unsafe_allow_html=True)
        
        score_msg = "Excellent Match 🎉" if final_score>=80 else "Good Match — Improve missing skills" if final_score>=50 else "Needs Improve"
        
        col_m1, col_m2 = st.columns([1, 1])
        with col_m1:
            st.markdown(f"**Matchscore**<br><span style='font-size: 14px; opacity: 0.8;'>{score_msg}</span>", unsafe_allow_html=True)
        with col_m2:
            st.markdown(f"<div class='match-score-value'>{final_score:.1f}%</div>", unsafe_allow_html=True)
        
        st.progress(int(final_score) if final_score <= 100 else 100)

    st.write("")

    # 6. ATS Feedback
    with st.container(border=True):
        st.markdown("<div class='section-title'>📝 ATS Feedback</div>", unsafe_allow_html=True)
        
        if final_score >= 80:
            st.success("🎉 Excellent Matchscore\nYour resume is strongly Aligned with JD")
        elif 50 <= final_score < 80:
            st.warning("👍 Good Matchscore\nYour resume is moderately aligned with JD")
        else:
            st.error("⚠️ Low Matchscore  \nyour resume is not strongly Aligned with JD")
            
        important_missing = list(set(required_skills) - set(resume_skills))
        if not important_missing:
            important_missing = missing_skills
            
        if important_missing:
            st.markdown("Try adding important missing skills:")
            missing_html_ats = "".join([f"<span class='missing-badge-ats'>{skill}</span>" for skill in important_missing])
            st.markdown(missing_html_ats, unsafe_allow_html=True)
