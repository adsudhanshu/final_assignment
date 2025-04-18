#  AI-Powered FastAPI Project Generator

This project leverages **LangGraph**, **LangChain**, and **FastAPI** to automate the generation of complete FastAPI backend projects from a given **SRS (Software Requirements Specification)** document.

##  Features

-   Upload `.docx` SRS files
-   Automated:
-   Requirement Analysis
-   Project Scaffolding
-   Backend Code Generation
-   Unit Test Generation
-   Validation
-   Documentation
-   Workflow Visualization
-   Zips the final generated project for download
-   Exposed via FastAPI endpoints


## ▶️ How to Run

### 1. Install Dependencies

pip install -r requirements.txt

2. Start the FastAPI Server
uvicorn main:app --reload
3. Open the API Docs
Visit:
📎 http://127.0.0.1:8000/docs

You can upload your .docx SRS file and download the generated project as a .zip.

## API Endpoint
POST /generate_project/
Description: Upload your .docx SRS file and receive a zipped FastAPI project.

Form Field:

srs_file: .docx file

Response:

application/zip containing your generated FastAPI backend

## Tech Stack
Python 3.10+

FastAPI — API server

LangGraph / LangChain — Graph-based LLM pipelines

Graphviz / Mermaid — Workflow visualizations

Docx, Pydantic, OpenAI API, etc.
