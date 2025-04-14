## 📄 Smart Resume Analyzer
An AI-powered web application to analyze resumes, compare them to job descriptions, score their compatibility, and suggest improvements. Built with Streamlit and Google Gemini API, this tool helps job seekers optimize their resumes in real-time.

## 🚀 Features
Text Extraction: Extracts content from resumes in PDF format.

Job Fit Scoring: Compares resume to job description and rates compatibility on a scale of 0-100%.

AI Resume Summary: Generates a professional resume summary using AI.

Suggestions for Improvement: Provides tailored tips to improve your resume based on the job description.

Modular Design: Built with clean, scalable, and maintainable code.

## 🧠 Problem Statement
Job seekers often struggle to optimize their resumes for specific roles, and recruiters are overwhelmed by generic applications.
Smart Resume Analyzer solves this problem by using AI to analyze the resume in the context of a job description and provides tailored suggestions to improve the resume.

## 📂 Project Structure
vbnet
Copy code
smart-resume-analyzer/
├── app.py                   ← Streamlit frontend
├── resume_utils.py          ← PDF parsing + section extraction
├── text_processing.py       ← Text preprocessing (cleaning, lemmatization)
├── ai_services.py           ← Gemini API integration
├── tests/                   ← Unit & integration tests
│   ├── test_resume_utils.py
│   ├── test_text_processing.py
│   └── test_ai_services.py
├── docs/                    ← (You can use this for future docs or keep it empty)
├── requirements.txt         ← Python dependencies
└── README.md                ← Main project guide

## 🛠️ Tech Stack
- Frontend: Streamlit

- Backend: Python

- AI/ML: Google Gemini (Generative AI)

- Parsing: pdfplumber

- Text Processing: NLTK, Regex, Lemmatizer

- Testing: Pytest (or unittest)

## 📦 Setup Instructions
Follow these steps to get the project up and running on your local machine.

1. Clone the repository
    ```bash
    Copy code
    git clone https://github.com/yourusername/smart-resume-analyzer.git
    cd smart-resume-analyzer

2. Install dependencies
Make sure you have Python 3.x installed, then run:
    ```bash
    Copy code
    pip install -r requirements.txt

3. Set up the API key
In ai_services.py, replace the line where the API key is set:

python
    ```bash
    Copy code
    genai.configure(api_key="your_gemini_api_key_here")
    Ensure you replace "your_gemini_api_key_here" with your actual Gemini API Key.

## ▶️ Running the App
To launch the web application:
    ```bash
    Copy code
    streamlit run app.py
This will start the Streamlit server locally, and you can access the app at http://localhost:8501.

## 🧪 Running Tests
You can run the tests to make sure everything is working:
    ```bash
    Copy code
    pytest tests/
Alternatively, you can use the built-in unittest framework:
    ```bash
    Copy code
    python -m unittest discover tests/
## 📘 API Documentation
For details on how the AI engine works and what data is sent to Google Gemini, refer to the API Documentation.

## 📸 Screenshots
Here are some example screenshots of how the app looks:
![alt text](<Screenshot (135).png>)--->![alt text](<Screenshot (136).png>)----->![alt text](<Screenshot (137).png>)

Upload Resume	Job Matching
## ✨ Future Enhancements
- User Authentication: Allow users to save and retrieve resumes.

- Cloud Deployment: Host the app on a cloud platform like Heroku or Streamlit Cloud.

- Email Integration: Send the updated resume directly via email.

- Additional Analytics: Provide detailed feedback on how to improve resume sections.

## 👨‍💻 Author
Name: Roshan Kumar

Email: rk1861303@gmail.com

GitHub: https://github.com/Roshan-pro

## 📄 License
This project is licensed under the MIT License. See LICENSE for more details.
