from graph_config.model import GraphState
from typing import Dict
from graphviz import Digraph
import os

def generate_graphviz_visualization(graph_state):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    dot = Digraph(comment="LangGraph Workflow")
    dot.attr(rankdir='LR', size='10')

    # Define nodes
    dot.node("A", "Analyze SRS")
    dot.node("B", "Project Setup")
    dot.node("C", "Generate Unit Tests")
    dot.node("D", "Generate Backend Code")
    dot.node("E", "Persist Graph State")
    dot.node("F", "Generate Zip File")
    dot.node("G", "Generate README.md")
    dot.node("H", "Generate API Docs")
    dot.node("I", "Generate Workflow Graph")
    dot.node("END", "End")

    # Define edges
    dot.edges([
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("F", "G"),
        ("G", "H"),
        ("H", "I"),
        ("I", "END")
    ])
    print(project_root)
    png_path = os.path.join(project_root, "workflow_graph.png")
    dot.render(png_path, format="png", cleanup=True)

    return {"message":"Workflow graph saved", "path":f"{png_path}.png"}