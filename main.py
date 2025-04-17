from graph_config.graph import build_analysis_graph
from graph_config.graph import GraphState

if __name__ == "__main__":

    project_root="./generated_project"
    graph = build_analysis_graph()

    initial_state = GraphState(
        srs_docx_path="srs_doc.docx",
        project_root=project_root
        
        )
    final_state = graph.invoke(initial_state)

    print("Analysis result\n")
    print(final_state["analysis"])


