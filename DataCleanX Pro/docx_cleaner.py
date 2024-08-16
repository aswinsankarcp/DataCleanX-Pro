from docx import Document
import re


def clean_docx(docx_path):
    print(f"Cleaning DOCX file: {docx_path}")

    # Load the DOCX file
    doc = Document(docx_path)

    # Example cleaning steps
    for para in doc.paragraphs:
        clean_text = re.sub(r'\s+', ' ', para.text).strip()  # Normalize whitespace
        para.text = clean_text

    cleaned_docx_path = docx_path.replace('.docx', '_cleaned.docx')
    doc.save(cleaned_docx_path)

    print(f"DOCX file cleaned and saved as: {cleaned_docx_path}")
    return cleaned_docx_path
