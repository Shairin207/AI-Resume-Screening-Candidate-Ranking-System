# 🤖 AI Resume Screening & Candidate Ranking System

An AI-powered Resume Screening System that automates candidate shortlisting by analyzing resumes and matching them with job descriptions using NLP and Machine Learning techniques.

---

## 🚀 Features

- 📄 Upload multiple PDF resumes
- 🧠 Extract text using PDF parsing + OCR fallback
- 🔍 Extract key skills from resumes
- 📊 Match resumes with job description
- 🏆 Rank candidates based on similarity score
- 📉 Identify missing skills for each candidate
- 📥 Download shortlisted candidates as CSV
- 🌐 Interactive web UI using Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- PyPDF2
- pdfplumber
- pdf2image
- pytesseract

---

## ⚙️ How It Works

1. Upload resumes (PDF format)
2. Enter job description
3. System extracts text from resumes
4. Skills are detected using keyword-based NLP
5. ML model calculates similarity score
6. Candidates are ranked automatically
7. Export results as CSV

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shairin207/AI-Resume-Screening-Candidate-Ranking-System
cd AI_Resume_Screening_System
```
## 2. Create virtual environment
```bash
python -m venv .venv
```
## 3. Activate virtual environment
```bash
.venv\Scripts\activate
```
## 4. Install dependencies
```bash
pip install -r requirements.txt
```
##  5.▶️ Run the App
```bash
python -m streamlit run app.py
```
## 📁 Project Structure

```text
AI_Resume_Screening_System/
│
├── app.py
├── resume_parser.py
├── ranking.py
├── export_csv.py
├── requirements.txt
├── README.md
├── resumes/
│   └── sample_resume.pdf
└── outputs/
    └── shortlisted_candidates.csv
```

## 📊 How It Works

- Upload resumes in PDF format
- Enter the job description
- The system extracts text from uploaded resumes
- Skills are identified using NLP-based keyword matching
- A machine learning model calculates similarity scores
- Candidates are ranked automatically based on relevance
- Results can be downloaded as a CSV file

---
## 📊 Example Output

### 🏆 Candidate Rankings

| Candidate | Score (%) | Skills | Missing Skills |
|------------|------------|---------|----------------|
| Candidate 1.pdf | 5.65 | machine learning | python, pandas, numpy, scikit-learn |
| Candidate 2.pdf| 1.95 | None detected | python, machine learning, pandas, numpy, scikit-learn |

### 🔟 Top Candidates

| Candidate | Score (%) | Skills | Missing Skills |
| Candidate 1.pdf | 5.65 | machine learning | python, pandas, numpy, scikit-learn |
| Candidate 2.pdf | 1.95 | None detected | python, machine learning, pandas, numpy, scikit-learn |

### 📌 Interpretation

- Higher scores indicate a stronger match with the job description.
- Extracted skills represent keywords found in the resume.
- Missing skills highlight important requirements absent from the resume.
- Candidates are automatically ranked from highest to lowest score.

## 💡 Future Improvements

- Advanced NLP-based skill extraction
- Deep learning-based candidate ranking
- ATS (Applicant Tracking System) scoring
- Recruiter analytics dashboard
- Resume recommendation system
- Cloud deployment using Streamlit Cloud or Render
- Support for additional resume formats (DOCX, TXT)
- Enhanced skill matching using transformer-based NLP models
### 👨‍💻 Author
Shairin Akter Hashi 
