import streamlit as st
import tempfile
import os

from resume_parser import extract_resume_text
from job_matcher import load_job_descriptions, match_resume_to_jobs
from utils import extract_skills

# Streamlit app settings
st.set_page_config(page_title="IntelliDoc", layout="wide")
st.title("📄 IntelliDoc – AI Resume & Skill Analyzer")

# Upload section
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF or DOCX)", type=['pdf', 'docx'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    try:
        # Extract resume text
        resume_text = extract_resume_text(tmp_path)

        st.subheader("📝 Extracted Resume Text")
        st.text_area("Resume Text", resume_text, height=300)

        # Skill extraction
        st.subheader("🧠 Extracted Skills")
        skills = extract_skills(resume_text)
        st.write(", ".join(skills) if skills else "No skills identified.")

        # Job matching
        st.subheader("📊 Job Match Results")
        job_df = load_job_descriptions()
        matched_jobs = match_resume_to_jobs(resume_text, job_df)

        # Format result: reset index and start from 1
        matched_jobs = matched_jobs.reset_index(drop=True)
        matched_jobs.index = matched_jobs.index + 1  # Index starts from 1
        matched_jobs = matched_jobs.rename(columns={
            'title': 'Role',
            'match_score': 'Match Score (%)'
        })

        # Show top 5 results
        st.dataframe(matched_jobs[['Role', 'Match Score (%)']].head(5))

    except Exception as e:
        st.error(f"❌ Conversion or Extraction Failed: {str(e)}")
        st.warning("⚠️ Resume text could not be extracted.")
    finally:
        os.remove(tmp_path)
