"""
This module initializes the multi-agent workflow for processing resumes using LangChain and Groq API.
"""

import os
from secret import LANGCHAIN_API_KEY, GROQ_API_KEY
from langgraph.graph import Graph, END
from langchain_groq import ChatGroq
from agents.reader import resume_reader_agent
from agents.extracter import extracter_agent
from agents.validator import validator_agent
import json 

def main():
    """
    Main function to set up and invoke the multi-agent workflow for resume processing.
    """
    # Set the API key environment variable
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
    os.environ["LANGCHAIN_PROJECT"] = "pibit_assignment"
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

    # Initialize the language model
    llm = ChatGroq(
        model="mixtral-8x7b-32768"
    )

    # Initialize the workflow graph
    workflow = Graph()

    # Add nodes to the graph
    workflow.add_node("read_resume", resume_reader_agent)
    workflow.add_node("extract_entities", extracter_agent)
    workflow.add_node("validate_entities", validator_agent)

    # Add edges to the graph
    workflow.add_edge("read_resume", "extract_entities")
    workflow.add_edge("extract_entities", "validate_entities")
    workflow.add_edge("validate_entities", END)

    # Set the entry point node
    workflow.set_entry_point("read_resume")

    # Compile the graph
    app = workflow.compile()

    # Invoke the workflow with the resume file
    result = app.invoke("resume.pdf")

    with open("parsed_resume.json", "w") as json_file:
        json.dump(result, json_file, indent=4)


if __name__ == "__main__":
    main()
