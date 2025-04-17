import os
import re
from pathlib import Path
from graph_config.model import GraphState
from langchain_core.prompts import ChatPromptTemplate
from tools.analyze_srs import llm
from langchain_core.output_parsers import StrOutputParser

def generate_backend_code(state:GraphState)->GraphState:
    """Generate FastAPi backend code (models, routes, services ,main and other configuration files) based on the srs analysis"""
    
    if not state.analysis:
        raise ValueError("Error  in the Srs analysis")
    
    prompt=ChatPromptTemplate.from_messages([
        ("system","You are a senior backend developer. Generate the fast Api code adhering to modular approach and best coding practices and also error handling, proper log generation."),
        ("user","Based on the following requirements, generate complete code for : - Pydantic models , -SqlAlchemy , -Api routes , -ServiceLayer logic and other main configurations . Requirements: {analysis}")
     ])
    
    chain = prompt| llm | StrOutputParser()

    code_output = chain.invoke({"analysis":state.analysis})

    print("Generated_code",code_output)
     
     # Create test folder
    project_dir = Path("./generated_project/app")
    project_dir.mkdir(parents=True, exist_ok=True)

    # Parse markdown and extract each test file
    pattern = r"\*\*(\w+\.py)\*\*\s*```(?:python)?(.*?)```"
    matches = re.findall(pattern, code_output, re.DOTALL)

    generated_code_dict = {}

    for filename, code in matches:
        filepath = project_dir / filename
        cleaned_code = code.strip()

        with open(filepath, "w") as f:
            f.write(cleaned_code)

        generated_code_dict[filename] = cleaned_code
        print(f"📁 Saved code: {filepath}")

    state.generated_code = generated_code_dict

    return state
    