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
from tools.generate_visual import generate_mermaid_visualization_png
from tools.generate_document import generate_readme_tool
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import shutil

app = FastAPI()

@app.post("/generate_project/")
async def generate_project(srs_file: UploadFile = File(...)):
    # Save the uploaded SRS file
    srs_file_path = os.path.join("temp", srs_file.filename)
    os.makedirs(os.path.dirname(srs_file_path), exist_ok=True)
    
    with open(srs_file_path, "wb") as buffer:
        shutil.copyfileobj(srs_file.file, buffer)
    
    # Process the SRS (call your graph-building function or logic here)
    graph = build_analysis_graph(srs_file_path)
    
    # Generate the zip of the generated project
    zip_filename = "generated_project.zip"
    zip_node = ZipGeneratedProjectNode(zip_filename=zip_filename)
    zip_file_path = zip_node.execute()

    # Return the generated zip file as response
    return FileResponse(zip_file_path, media_type='application/zip', filename=zip_filename)
def build_analysis_graph(srs_file_path):
    graph = StateGraph(GraphState)
    analyze_node = RunnableLambda(analyze_srs_node, args=[srs_file_path])
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

    generate_visual = RunnableLambda(generate_mermaid_visualization_png)
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
