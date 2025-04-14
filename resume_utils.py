import pdfplumber

def extract_text_from_pdf(file):
    file.seek(0)
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
