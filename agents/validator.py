"""
This module contains functions to interact with the Groq API for extracting, validating, 
and correcting information from resumes.
"""

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

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
    return input(prompt)

def corrector(suggestions, entities):
    """
    Correct the extracted information from a resume based on given suggestions.

    Args:
        suggestions (str): The suggestions to correct the extracted information.
        entities (str): The extracted information from the resume.

    Returns:
        str: The corrected information in a structured JSON format.
    """
    prompt = f"""
    Consider the following suggestions for the extracted information from the resume:
    {suggestions}

    Extracted information from a resume:
    {entities}

    Make changes according to the given suggestions and provide final information from the resume 
    in a structured format like JSON.
    """
    response = llm.invoke(prompt)

    return response.content

def validator_agent(entities, feedback=""):
    """
    Validate the extracted information from a resume and correct if necessary.

    Args:
        entities (str): The extracted information from the resume.
        feedback (str, optional): Human feedback to refine the validation process. Defaults to an empty string.

    Returns:
        str: The validated (and possibly corrected) information in a structured JSON format.
    """
    prompt = f"""
    Validate the following extracted information from a resume:
    {entities}

    Check for the following:
    1. All fields are present
    2. Email and phone formats are valid
    3. Education and work experience entries have all required fields
    4. The information aligns with the human feedback

    If any issues are found, describe them. If no issues are found, respond with "All information is valid."

    Human feedback:
    {feedback}

    Consider the human feedback while validating information. If the feedback suggests any corrections or additions, 
    incorporate them into your validation.

    Output your findings in JSON format with a 'valid' boolean field and an 'issues' list field.
    """
    response = llm.invoke(prompt)
    validation_result = response.content

    if '"valid": false' in validation_result:
        corrected_entities = corrector(validation_result, entities)
        return validator_agent(corrected_entities)
    
    print("\n>>>>> 3) ✅ Extracted data Validated by validator_agent and there are no errors in the output .....\n")

    feedback = get_human_feedback("FEEDBACK -> Entities have been validated, any feedback on the validation? If no press 'ENTER': ")
    
    if feedback:
        return validator_agent(entities, feedback=feedback)
    return entities
        