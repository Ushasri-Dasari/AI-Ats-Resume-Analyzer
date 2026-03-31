# skills.py
# Predefined industry skills
SKILLS = [
     "python", "r", "sql", "django", "flask", "fastapi",
    "machine learning", "deep learning", "nlp",
    "tensorflow", "pytorch", "scikit-learn",
    "numpy", "pandas",
    "data structures", "algorithms",
    "statistics", "probability",
    "aws", "azure", "gcp",
    "git", "github",
    "html", "css", "javascript"
]

# Function to extract skills from text
def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILLS if skill in text]
    return found_skills
