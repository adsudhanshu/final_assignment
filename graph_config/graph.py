from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from tools.analyze_srs import analyze_srs_node
from tools.project_setup import project_setup_chain
from graph_config.model import GraphState
from tools.generate_unit_test import generate_unit_tests
from tools.generate_backend_code import generate_backend_code
from tools.automated_validation import automated_validation_node
from tools.deployment import ZipGeneratedProjectNode
from persistence.crud import save_graph_state
from tools.generate_visual import generate_graphviz_visualization
from tools.generate_document import generate_readme_tool

def build_analysis_graph():
    graph = StateGraph(GraphState)
    analyze_node = RunnableLambda(analyze_srs_node)
    graph.add_node("AnalyzeSRS", analyze_node)

    project_setup_node = RunnableLambda(project_setup_chain)
    graph.add_node("ProjectSetup",project_setup_node)

    graph.add_node("generate_unit_test",generate_unit_tests)

    graph.add_node("generate_backend_code",generate_backend_code)

    graph.add_node("automated_validation",automated_validation_node)

    persistence_node = RunnableLambda(save_graph_state)
    graph.add_node("PersistentGraphState",persistence_node)

    zip_node = ZipGeneratedProjectNode(zip_filename='generated_project')
    graph.add_node("ZipGeneratedProject", RunnableLambda(lambda input,config=None:zip_node.execute(input)))

    generate_visual = RunnableLambda(generate_graphviz_visualization)
    graph.add_node("GenerateViz",generate_visual)

    generate_readme = RunnableLambda(generate_readme_tool)
    graph.add_node("GenerateReadme",generate_readme)

    graph.set_entry_point("AnalyzeSRS")
    graph.add_edge("AnalyzeSRS","ProjectSetup")
    graph.add_edge("ProjectSetup","generate_unit_test")
    graph.add_edge("generate_unit_test","generate_backend_code")
    # graph.add_edge("generate_backend_code","PersistentGraphState")
    graph.add_edge("generate_backend_code","ZipGeneratedProject")
    graph.add_edge("ZipGeneratedProject","GenerateViz")
    graph.add_edge("GenerateViz","GenerateReadme")
    graph.add_edge("GenerateReadme",END)
    # graph.add_edge("automated_validation",END)
    return graph.compile()
