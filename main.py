import os
from secret import LANGCHAIN_API_KEY, GROQ_API_KEY
from langchain_groq import ChatGroq
from agents.reader import resume_reader_agent
from agents.extracter import extracter_agent
from agents.validator import validator_agent


# Set the API key environment variable
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_ENDPOINT"]= "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]= LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"]= "pibit_assignment"

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the language model
llm = ChatGroq(
    model="mixtral-8x7b-32768"
)


from langgraph.graph import Graph, END

workflow = Graph()

# Add nodes to the graph
workflow.add_node("read_resume", resume_reader_agent)
workflow.add_node("extract_entities", extracter_agent)
workflow.add_node("validate_entities", validator_agent)
# workflow.add_node("generate_output", generate_output)

# Add edges to the graph
workflow.add_edge("read_resume", "extract_entities")
workflow.add_edge("extract_entities", "validate_entities")
workflow.add_edge("validate_entities", END)
# workflow.add_edge("validate_entities", "generate_output")
# workflow.add_edge("extract_entities", END)

# Set the entrypoint node
workflow.set_entry_point("read_resume")

    # Compile the graph
app = workflow.compile()

result = app.invoke("resume.pdf")

print(result)

