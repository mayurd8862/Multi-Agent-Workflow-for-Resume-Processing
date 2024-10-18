"""
This module contains functions to interact with the Groq API and extract key information from resumes.
"""

import os
from langchain_groq import ChatGroq
from secret import GROQ_API_KEY

# Set the API key environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the language model
llm = ChatGroq(
    model="mixtral-8x7b-32768"
)



def get_human_feedback(prompt):
    """
    Get human feedback based on a prompt.

    Args:
        prompt (str): The prompt to present to the user.

    Returns:
        str: The feedback provided by the user.
    """
    # Replace with appropriate feedback mechanism (e.g., Streamlit input in actual implementation)
    return input("Your feedback: ")

def extracter_agent(loaded_doc, feedback=""):
    """
    Extracts key information from resumes using a language model.

    Args:
        loaded_doc (str): The content of the loaded resume document.
        feedback (str, optional): Human feedback to refine the extraction process. Defaults to an empty string.

    Returns:
        str: The extracted information in a structured JSON format.
    """
    prompt = f"""
    You are an Extractor Agent. Your task is to extract key information from resumes. The resumes will be 
    provided to you by the Resume Reader Agent. The entities you need to extract include:

    - Name
    - Contact Information (Phone Number, Email Address)
    - Education (Degrees, Institutions, Graduation Dates)
    - Work Experience (Job Titles, Companies, Employment Dates, Job Responsibilities)
    - Skills
    - Certifications
    - Projects
    - Languages
    - Additional Information (if any)

    Here is the resume content:

    {loaded_doc}

    Human feedback:
    {feedback}

    Consider the human feedback while extracting information. If the feedback suggests any corrections or 
    additions, incorporate them into your extraction.

    Please extract the entities in a structured format like JSON:
    """

    response = llm.invoke(prompt)
    extracted_content = response.content

    feedback = get_human_feedback("Entities have been extracted. Any feedback on the extraction?")

    if feedback:
        return extracter_agent(loaded_doc, feedback=feedback)

    return extracted_content
