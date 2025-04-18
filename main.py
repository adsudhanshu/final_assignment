from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from graph_config.graph import build_analysis_graph, GraphState
from tools.deployment import ZipGeneratedProjectNode
import os
import shutil

app = FastAPI()

@app.post("/generate_project/")
async def generate_project(srs_file: UploadFile = File(...)):
    print("Received request!")

    os.makedirs("temp", exist_ok=True)
    srs_path = os.path.join("temp", srs_file.filename)
    with open(srs_path, "wb") as f:
        shutil.copyfileobj(srs_file.file, f)

    project_root = "./generated_project"
    os.makedirs(project_root, exist_ok=True)
    graph = build_analysis_graph(srs_path)
    initial_state = GraphState(srs_docx_path=srs_path, project_root=project_root)
    final_state = graph.invoke(initial_state)

    # Zip result
    zip_node = ZipGeneratedProjectNode(zip_filename="generated_project.zip")
    zip_path = zip_node.execute()

    return FileResponse(zip_path, filename="generated_project.zip", media_type="application/zip")
