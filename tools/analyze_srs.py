import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from docx import Document
from pydantic import BaseModel

llm = ChatGroq(
     model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key= os.getenv("GROK_API_KEY") ,
)

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a backend architect.Extract key Software requirements (functional , non-functional, backend models, workflows, APIs) from the following SRS."),
        ("user","{srs_text}")
    ])


chain = prompt | llm

class GraphState(BaseModel):
    srs_docx_path:str
    analysis:str | None=None


def analyze_srs_node(state: GraphState) -> GraphState:
    """Tool to analyze a Software Requirements Specification (SRS) document in .docx format.
    This tool reads the provided .docx file, extracts its textual content, and sends it to an LLM
    with a backend-focused prompt to extract:

    - API endpoints and operations

    - Business logic and workflows

    - Database schema and models

    - Authentication and role-based access

    - Functional and non-functional requirements

    The output is added to the LangGraph state under the key 'analysis'."""
    doc = Document(state.srs_docx_path)
    srs_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() ])


    output = chain.invoke({"srs_text":srs_text})

    return GraphState(srs_docx_path=state.srs_docx_path , analysis= output.content)
