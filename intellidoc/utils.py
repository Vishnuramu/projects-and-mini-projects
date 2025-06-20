import spacy
import subprocess
import importlib.util

# ✅ Auto-download SpaCy model if not found
def ensure_spacy_model():
    model_name = "en_core_web_sm"
    if importlib.util.find_spec(model_name) is None:
        subprocess.run(["python", "-m", "spacy", "download", model_name])

ensure_spacy_model()

# ✅ Load the model
nlp = spacy.load("en_core_web_sm")

# 🧠 Extract skills from resume text
def extract_skills(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    # 🎯 Define skill keywords to match
    keywords = [
        "python", "java", "sql", "machine learning", "deep learning",
        "django", "flask", "react", "node.js", "aws", "docker",
        "pandas", "numpy", "excel", "power bi", "tableau", "git", "streamlit"
    ]

    # 🔍 Match found keywords
    matched = [kw for kw in keywords if kw in tokens]
    return list(set(matched))
