import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
import tempfile

def load_document(file):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.name[file.name.rfind('.'):]) as temp_file:
        temp_file.write(file.getvalue())
        temp_file_path = temp_file.name

    # Load the document based on its type
    if file.name.endswith('.pdf'):
        loader = PyPDFLoader(temp_file_path)
    elif file.name.endswith('.docx'):
        loader = Docx2txtLoader(temp_file_path)
    else:
        raise ValueError("Unsupported file format")

    documents = loader.load()
    return documents

def main():
    st.title("Simple Resume Reader")

    uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

    if uploaded_file is not None:
        try:
            documents = load_document(uploaded_file)
            st.success("Resume loaded successfully!")
            st.write(documents[0].page_content)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()