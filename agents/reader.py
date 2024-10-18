"""
This module contains the resume_reader_agent function which reads resumes from 
PDF and DOCX files and extracts their content.
"""

from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader

def resume_reader_agent(file_path):
    """
    Reads a resume from a given file path and extracts the content.

    Args:
        file_path (str): The path to the resume file.

    Returns:
        str: The content of the resume.
    
    """
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.docx'):
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError("Unsupported file format")

    documents = loader.load()

    return documents[0].page_content

# Add a final newline
