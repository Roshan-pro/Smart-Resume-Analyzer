# app.py

import streamlit as st
import pandas as pd
from resume_utils import extract_text_from_pdf, extract_sections
# from text_processing import preprocess_text
from ai_services import generate_resume_summary, get_resume_fit_score_and_feedback

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