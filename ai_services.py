import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyB3U-eS5mWFTPTG4R8m9ffAuSnPI2IqB44")

def generate_resume_summary(resume_text):
        prompt = f"Based on this resume, write a strong professional summary to use at the top of the resume:\n\n{resume_text}"
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    

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