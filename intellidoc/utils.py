
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text.lower())
    skills = [token.text for token in doc if token.pos_ == "NOUN"]
    return list(set(skills))
