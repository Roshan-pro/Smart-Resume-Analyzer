import re
import string
import pandas as pd
import pickle
import pdfplumber
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initial setup
nltk.download('stopwords')
nltk.download('wordnet')

# Configure Gemini
genai.configure(api_key="AIzaSyB3U-eS5mWFTPTG4R8m9ffAuSnPI2IqB44") 
# Preprocess text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

import pdfplumber

def extract_text_from_pdf(file):
    file.seek(0)  # Reset file pointer before reading
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  
                text += page_text + "\n"
    return text.strip()




def extract_sections(resume_text):
    sections = {
        "Education": "",
        "Skills": "",
        "Experience": "",
        "Projects": "",
        "Certifications": ""
    }

    lines = resume_text.split("\n")
    current_section = None

    for line in lines:
        line_clean = line.strip().lower()
        if "education" in line_clean:
            current_section = "Education"
        elif "skills" in line_clean:
            current_section = "Skills"
        elif "experience" in line_clean or "employment" in line_clean:
            current_section = "Experience"
        elif "project" in line_clean:
            current_section = "Projects"
        elif "certification" in line_clean:
            current_section = "Certifications"
        
        if current_section and line.strip() != "":
            sections[current_section] += line.strip() + " "

    return sections



def generate_resume_summary(resume_text):
        prompt = f"Based on this resume, write a strong professional summary to use at the top of the resume:\n\n{resume_text}"
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()



def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text.strip()

def get_resume_improvement_feedback(resume, job_description):
    prompt = f"""
Compare the following resume with the job description and provide:
1. A decision: Is the candidate a good match? (Yes/No)
2. 3 tips to improve the resume for this role
3. A short sample resume snippet with these improvements

Resume:
{resume}

Job Description:
{job_description}
"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    feedback=response.text.replace("*","") 

    return feedback
def get_resume_fit_score_and_feedback(resume, job_description):
    prompt = f"""
You are a hiring expert. Rate how well the following resume fits the job description. 
Provide the following:

1. A score from 0 to 100 showing how well the resume matches the job.
2. A brief reason for the score (2 lines max).
3. Three improvement tips for the resume.
4. A short resume snippet after improvements.

Resume:
{resume}

Job Description:
{job_description}
"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    feedback_text = response.text.replace("*", "").strip()

    score_match = re.search(r"Score:\s*(\d{1,3})", feedback_text)
    score = int(score_match.group(1)) if score_match else 0

    return score, feedback_text




import streamlit as st
st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
st.title("📄 Smart Resume Analyzer")

uploaded_file = st.sidebar.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📋 Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=300)

    sections = extract_sections(resume_text)
    st.subheader("🔍 Parsed Resume Sections")
    for section, content in sections.items():
        if content.strip():
            st.markdown(f"**{section}:**\n{content}")
    st.sidebar.subheader("💼 Job/Internship Description")
    job_desc_input = st.sidebar.text_area("Paste the job/internship description here:")

    

    if st.sidebar.button("🧠 Analyze Fit & Get Resume Improvement Suggestions"):
        if job_desc_input.strip()=="":
            st.sidebar.warning("⚠️ Please enter a job or internship description.")
        else:
            score, feedback = get_resume_fit_score_and_feedback(resume_text, job_desc_input)
            st.subheader("📊 Resume Fit Score")
            st.markdown(f"### 🔢 Score: {score}% / 100")
            score_df = pd.DataFrame({"Score": [score]}, index=["Your Resume"])
            st.bar_chart(score_df)
            if score >= 80:
                st.success("🟢 Strong match! Your resume aligns well with this job.")
            elif score >= 50:
                st.warning("🟡 Moderate match. Some improvements needed.")
            else:
                st.error("🔴 Low match. Consider updating your resume for this role.")

            st.subheader("✅ Feedback & Resume Suggestions")
            st.write(feedback)
    if st.button("📝 Generate Resume Summary ussing AI"):
        summary = generate_resume_summary(resume_text)
        st.subheader("🔝 Suggested Resume Summary")
        st.write(summary)
