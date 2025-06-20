from pdfminer.high_level import extract_text as extract_pdf_text
import docx

def extract_resume_text(file_path):
    """
    Detects file type and extracts text from PDF or DOCX resume.
    """
    if file_path.endswith('.pdf'):
        return extract_pdf_text(file_path)
    elif file_path.endswith('.docx'):
        return extract_docx_text(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a .pdf or .docx file.")

def extract_docx_text(path):
    """
    Extracts text from .docx Word files.
    """
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
