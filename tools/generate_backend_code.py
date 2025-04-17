from graph_config.model import GraphState
from langchain_core.prompts import ChatPromptTemplate
def generate_backend_code(state:GraphState)->GraphState:
    """Generate FastAPi backend code (models, routes, services ,main and other configuration files) based on the srs analysis"""
    
    if not state.analysis:
        raise.ValueError("Error  in the Srs analysis")
    
    prompt=ChatPromptTemplate.from_messages([
        ("system","You are a senior backend developer. Generate the fast Api code adhering to modular approach and best coding practices."),
        ("user":"")
     ])
    