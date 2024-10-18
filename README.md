# Multi-Agent Workflow for Resume Processing

## 📝 Project Overview

This project involves creating a multi-agent workflow that automates the processing of multi-page resumes using Large Language Models (LLMs). The system is designed to read resumes, extract key entities, validate them, and incorporate human feedback at each stage to ensure accuracy and completeness. The final output is a JSON file containing all validated entities.

## 🎯 Objectives

- **Resume Reading**: Process multi-page resumes in various formats (e.g., PDF, DOCX).
- **Entity Extraction**: Extract key entities such as personal information, education, work experience, and skills.
- **Entity Validation**: Validate extracted entities and initiate correction if issues are detected.
- **Human Feedback Loop**: Allow human intervention at each stage for feedback and updates.
- **JSON Output**: Compile validated entities into a predefined JSON format.
- **Monitoring**: Used LangGraph and LangSmith to monitor and visualize LLM calls within the agents.


## 🤖 Tech Stack used:
- **python**
- **Groq** - A specialized AI accelerator designed for large language models, offering high performance and efficiency. used "mixtral-8x7b-32768" LLM model through groq.
- **Langchain** - used for documents loader, llm integration
- **Langgraph** - Used for creating multi agent workflows
- **Langsmith** - Monitoring and visualizing LLM calls, tokens, and other LLM parameters
- **git** - for version control system
- **pylint** - for ensuring code quality
- **Streamlit** - For user interface creation "IN PROGRESS"
  


## 🛠️ Installation

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

## 🏃‍♂️ How to Run the Application

 **Add resume file location and run the main.py code**:
   ```sh
   python main.py
   ```
## 🌊 Multi Agent workflow flowchart
![image](https://github.com/user-attachments/assets/20bed49c-e01b-419d-afc5-bfbf948d3de5)

## 💬 How Human Feedback Loop is working


## 👀 Monitoring with LangSmith

LangSmith is a powerful platform designed to provide comprehensive visibility and control over your Large Language Model (LLM) calls within your agents.

1. **Login to LangSmith**: Visit the LangSmith website and enter your credentials to log in to your account.
2. **Go to Projects**: Once logged in, navigate to the "Projects" section of the LangSmith dashboard.
Locate the project(s) that you have integrated with LangSmith. You can identify them by their names or descriptions.
3. **Monitor LLM Call Flows**: Click on a specific project to view its details. Go to the Runs section and analyse llm calls and outputs
4. **visualize**: In the "Monitoring" section, you should see a visualization of the LLM call flows within that project.
The visualization will display the sequence of LLM calls, their relationships, and any dependencies between them.


![image](https://github.com/user-attachments/assets/5886d878-31c7-426a-8711-9834e12696c0)

![image](https://github.com/user-attachments/assets/5d0f3f1f-14bb-41f1-b2f2-45144da2d959)


## 📧 Contact 
For any questions or suggestions, feel free to reach out:

- **Email**: mayur.dabade21@vit.edu
- **GitHub** : [mayurd8862](https://github.com/mayur8862)
- **LinkedIn** : [https://www.linkedin.com/in/mayur-dabade-b527a9230](https://www.linkedin.com/in/mayur-dabade-b527a9230)












