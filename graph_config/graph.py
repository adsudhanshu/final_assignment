from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from tools.analyze_srs import analyze_srs_node
from tools.project_setup import project_setup_chain
from graph_config.model import GraphState
from tools.generate_unit_test import generate_unit_tests
from tools.generate_backend_code import generate_backend_code

def build_analysis_graph():
    graph = StateGraph(GraphState)
    analyze_node = RunnableLambda(analyze_srs_node)
    graph.add_node("AnalyzeSRS", analyze_node)

    project_setup_node = RunnableLambda(project_setup_chain)
    graph.add_node("ProjectSetup",project_setup_node)

    graph.add_node("generate_unit_test",generate_unit_tests)

    graph.add_node("generate_backend_code",generate_backend_code)
    graph.set_entry_point("AnalyzeSRS")
    graph.add_edge("AnalyzeSRS","ProjectSetup")
    graph.add_edge("ProjectSetup","generate_unit_test")
    graph.add_edge("generate_unit_test","generate_backend_code")
    graph.add_edge("generate_backend_code",END)
    return graph.compile()
