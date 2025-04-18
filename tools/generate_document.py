# tools/generate_readme.py

from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage, HumanMessage 
from tools.analyze_srs import llm

# Optional: LangGraph-compatible tool
def generate_readme_tool(state):
    

    prompt = f"""
You are an expert Python developer. Write a complete README.md file for a root-level LangGraph-based AI system.

Project details:
- It uses LangGraph and LangChain agents/tools to analyze a Software Requirements Specification (SRS) document (.docx).
- It then generates a production-grade FastAPI backend from that SRS.
- The project includes:
    - Unit test generation (test-driven)
    - Backend code generation (routes, services, models)
    - Code validation and debugging
    - Iteration with persistent memory (PostgreSQL)
    - Deployment packaging (zipped project)
    - Graphviz workflow diagram generation
    - Dynamic agent creation using RAG from PDF files
    - FastAPI endpoint to accept SRS input
    - LangSmith logging

The structure is modular, clean, and follows best practices. Mention all key features, steps, APIs, and tools used. The workflow visual is saved as `workflow_graph.png` in root.

Write the README.md content.
    """

    readme_content = llm.invoke([HumanMessage(content=prompt)]).content

    # Optionally save it
    with open("README.md", "w") as f:
        f.write(readme_content)

    return {
        "readme_content": readme_content,
        "path": "README.md"
    }
