# Multi-Agent Workflow for Resume Processing


## Project Overview

This project involves creating a multi-agent workflow that automates the processing of multi-page resumes using Large Language Models (LLMs). The system is designed to read resumes, extract key entities, validate them, and incorporate human feedback at each stage to ensure accuracy and completeness. The final output is a JSON file containing all validated entities.

## Objectives

- **Resume Reading**: Process multi-page resumes in various formats (e.g., PDF, DOCX).
- **Entity Extraction**: Extract key entities such as personal information, education, work experience, and skills.
- **Entity Validation**: Validate extracted entities and initiate correction if issues are detected.
- **Human Feedback Loop**: Allow human intervention at each stage for feedback and updates.
- **JSON Output**: Compile validated entities into a predefined JSON format.
- **Monitoring**: Used LangGraph and LangSmith to monitor and visualize LLM calls within the agents.

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   https://github.com/mayurd8862/Multi-Agent-Workflow-for-Resume-Processing.git
   cd Multi-Agent-Workflow-for-Resume-Processing
   ```
2. **Create a virtual environment and activate it**:
   ```sh
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install the required packages:**:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
- Create a .env file in the root directory of the project and following api keys to it.
  
  ```sh
   LANGCHAIN_API_KEY = your_langchain_api_key
   GROQ_API_KEY = your_groq_api_key
   ```






















