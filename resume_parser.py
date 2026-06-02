import pdfplumber
from pypdf import PdfReader
from pdf2image import convert_from_bytes
import pytesseract

# OPTIONAL (only needed if PATH ever fails)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file):
    text = ""

    # -------------------------
    # 1. Try pdfplumber (BEST)
    # -------------------------
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception:
        pass

    if text.strip():
        return text

    # -------------------------
    # 2. Try PyPDF fallback
    # -------------------------
    try:
        file.seek(0)
        reader = PdfReader(file)

        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception:
        pass

    if text.strip():
        return text

    # -------------------------
    # 3. OCR fallback (scanned PDFs)
    # -------------------------
    try:
        file.seek(0)
        images = convert_from_bytes(file.read())

        for img in images:
            text += pytesseract.image_to_string(img)
    except Exception as e:
        return f"OCR failed: {str(e)}"

    return text if text.strip() else "No readable text found"


def extract_skills(text):
    skills = [
        "python", "java", "c++", "machine learning",
        "data analysis", "pandas", "numpy",
        "nlp", "streamlit", "scikit-learn"
    ]

    found_skills = []
    text_lower = text.lower()

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)

    return found_skills