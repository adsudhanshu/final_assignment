import os
import hashlib
import re
from pathlib import Path
from graph_config.model import GraphState
from langchain_core.prompts import ChatPromptTemplate
from tools.analyze_srs import llm
from langchain_core.output_parsers import StrOutputParser
from persistence.crud import save_graph_state,load_graph_state_by_hash
import json

def generate_backend_code(state:GraphState)->GraphState:
    """Generate FastAPi backend code (models, routes, services ,main and other configuration files) based on the srs analysis"""
    
    if not state.analysis:
        raise ValueError("Error  in the Srs analysis")
    
    srs_hash = hashlib.sha256(state.analysis.encode()).hexdigest()

    generated_code_dict = {}
    # Check if state already exists
    previous = load_graph_state_by_hash(srs_hash)
    if previous:
        print("🔁 Reusing previously generated GraphState")
        print(previous.components)
    

    prompt=ChatPromptTemplate.from_messages([
        ("system","You are a senior backend developer. Generate the fast Api code adhering to modular approach and best coding practices and also error handling, proper log generation."),
        ("user","Based on the following requirements, generate complete code for : - Pydantic models , -SqlAlchemy , -Api routes , -ServiceLayer logic and other main configurations . Requirements: {analysis} and Unit-Test:{unitTest}")
     ])
    
    chain = prompt| llm | StrOutputParser()

    code_output = chain.invoke({"analysis":state.analysis,"unitTest":state.unit_test})

    print("Generated_code",code_output)
     
    # Create the base directory
    project_dir = Path("./generated_project/app")
    project_dir.mkdir(parents=True, exist_ok=True)

    # Updated regex to match full file paths and colons
    pattern = r"\*\*\s*([a-zA-Z0-9_/\\.-]+\.py):?\s*\*\*\s*```(?:python)?\n(.*?)\n```"
    matches = re.findall(pattern, code_output, re.DOTALL)

    if not matches:
        raise ValueError(" No matches found in the generated code!")

    for file_path, code in matches:
        full_path = project_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(code.strip())

        generated_code_dict[file_path] = code.strip()
        print(f"Saved: {full_path}")

    # save_graph_state(srs_hash=srs_hash,generated_code=generated_code_dict)
    state.generated_code = generated_code_dict
    return state