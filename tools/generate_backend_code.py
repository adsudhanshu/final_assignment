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

    state.generated_code = code_output
    return state
    