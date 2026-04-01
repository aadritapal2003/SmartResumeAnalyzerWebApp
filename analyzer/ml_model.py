import PyPDF2
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SKILLS_DB = ["python", "django", "machine learning", "data analysis", "sql", "html", "css"]

JOB_MAP = {
    "python": "Python Developer",
    "django": "Backend Developer",
    "machine learning": "ML Engineer",
    "data analysis": "Data Analyst",
    "sql": "Database Analyst",
    "html": "Frontend Developer",
    "css": "UI Developer"
}

ALL_SKILLS = ["python", "django", "machine learning", "data analysis", "sql", "html", "css", "react", "nodejs"]

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        try:
            text += page.extract_text()
        except:
            pass

    return text.lower()

def generate_chart(skills):
    if not skills:
        skills = ["No Skills"]

    values = [1] * len(skills)

    plt.figure()
    plt.bar(skills, values)
    plt.xticks(rotation=30)

    # Correct path
    chart_path = os.path.join(BASE_DIR, 'static/analyzer/chart.png')
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    plt.savefig(chart_path)
    plt.close()

    return 'analyzer/chart.png'

def suggest_skills(found_skills):
    return list(set(ALL_SKILLS) - set(found_skills))

def analyze_resume(file):
    text = extract_text(file)

    found_skills = [skill for skill in SKILLS_DB if skill in text]

    score = int((len(found_skills) / len(SKILLS_DB)) * 100)

    jobs = list(set([JOB_MAP.get(skill, "General Role") for skill in found_skills]))

    chart = generate_chart(found_skills)

    suggestions = suggest_skills(found_skills)

    return score, found_skills, jobs, chart, suggestions