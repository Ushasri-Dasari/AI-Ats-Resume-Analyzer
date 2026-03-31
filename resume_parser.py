import pdfplumber
import docx

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

def extract_text_from_docx(uploaded_file):
    document = docx.Document(uploaded_file)
    return "\n".join([p.text for p in document.paragraphs])
