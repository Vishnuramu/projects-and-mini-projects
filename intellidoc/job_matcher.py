import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load semantic model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_job_descriptions():
    jobs = [
        {
            "title": "Python Developer",
            "description": (
                "We are hiring a Python Developer with experience in Django, Flask, and building RESTful APIs. "
                "The ideal candidate should have strong knowledge of Pandas, NumPy, and SQL databases like MySQL or PostgreSQL. "
                "Familiarity with Git, Docker, Streamlit, and deployment on AWS or GCP is preferred. "
                "Experience with Scikit-learn, data pipelines, and writing clean, modular Python code is a plus."
            )
        },
        {
            "title": "Java Developer",
            "description": (
                "Seeking an experienced Java Developer with hands-on skills in Java, Spring Boot, Hibernate, and Microservices. "
                "Should be proficient in REST API development, Maven, JPA, and version control using Git. "
                "Familiarity with cloud platforms and CI/CD tools like Jenkins is a bonus."
            )
        },
        {
            "title": "Full Stack Developer",
            "description": (
                "Looking for a Full Stack Developer skilled in both frontend and backend technologies. "
                "Must have experience with React, JavaScript, HTML5, CSS3, Node.js, Express, and MongoDB. "
                "Good understanding of REST APIs, Redux, and responsive design is essential."
            )
        },
        {
            "title": "Data Analyst",
            "description": (
                "We need a Data Analyst with expertise in data cleaning, transformation, and visualization. "
                "Proficient in Python, SQL, Excel, Power BI or Tableau. "
                "Should be comfortable with Pandas, NumPy, and statistical data analysis techniques."
            )
        },
        {
            "title": "Machine Learning Engineer",
            "description": (
                "ML Engineer skilled in building and deploying ML models using Scikit-learn, TensorFlow, and Keras. "
                "Experience with feature engineering, data preprocessing, and model evaluation required. "
                "Python proficiency and cloud deployment experience is necessary."
            )
        },
        {
            "title": "DevOps Engineer",
            "description": (
                "Looking for a DevOps Engineer with strong understanding of AWS, Docker, Kubernetes, Jenkins, and CI/CD pipelines. "
                "Must have knowledge of infrastructure as code (Terraform), Git, and system monitoring tools."
            )
        },
        {
            "title": "Cybersecurity Analyst",
            "description": (
                "Cybersecurity Analyst responsible for network and system security. "
                "Experience with penetration testing, SIEM tools, firewalls, threat assessment, and incident response. "
                "Knowledge of risk management frameworks and compliance is a must."
            )
        },
        {
            "title": "Cloud Engineer",
            "description": (
                "Cloud Engineer experienced in deploying applications on AWS, Azure, or GCP. "
                "Skills in cloud architecture, Linux, shell scripting, and tools like Terraform and Ansible are required. "
                "Should also be familiar with cost optimization and scalability."
            )
        },
        {
            "title": "Frontend Developer",
            "description": (
                "Frontend Developer with experience in React.js, JavaScript, HTML5, CSS3, and Redux. "
                "Should understand responsive design principles and UI/UX best practices. "
                "Bonus for experience with frontend testing tools and Tailwind CSS."
            )
        },
        {
            "title": "Backend Developer",
            "description": (
                "Backend Developer skilled in building scalable server-side applications. "
                "Should have experience with Node.js or Django/Flask, PostgreSQL or MongoDB, Redis, and REST API development. "
                "Understanding of authentication, caching, and deployment is essential."
            )
        }
    ]
    return pd.DataFrame(jobs)

def match_resume_to_jobs(resume_text, job_df):
    job_df['match_score'] = job_df['description'].apply(
        lambda desc: round(float(util.cos_sim(
            model.encode(resume_text, convert_to_tensor=True),
            model.encode(desc, convert_to_tensor=True)
        )), 4) * 100
    )
    return job_df.sort_values(by='match_score', ascending=False)
