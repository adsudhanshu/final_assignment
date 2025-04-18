import os
import subprocess

def generate_mermaid_visualization_png(graph_state):
    # Set the root directory of your project, not the generated_project folder
    project_root = os.path.abspath(os.path.dirname(__file__))  # The directory where your script is located

    # Mermaid diagram code
    mermaid_code = """
flowchart LR
    A[Analyze SRS] --> B[Project Setup]
    B --> C[Generate Unit Tests]
    C --> D[Generate Backend Code]
    D --> E[Persist Graph State]
    E --> F[Generate Zip File]
    F --> G[Generate README.md]
    G --> H[Generate API Docs]
    H --> I[Generate Workflow Graph]
    I --> END([End])
    """.strip()

    # Save the .mmd file in the root project directory
    mmd_path = os.path.join(project_root, "workflow_graph.mmd")
    with open(mmd_path, "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    # Path where the PNG file will be saved (in root project directory)
    png_path = os.path.join(project_root, "workflow_graph.png")

    # Generate PNG using Mermaid CLI (mmdc)
    try:
        subprocess.run([
            "mmdc",
            "-i", mmd_path,
            "-o", png_path,
            "-t", "default"
        ], check=True)
        return {
            "message": "Mermaid diagram saved as PNG in the root project directory",
            "path": png_path
        }
    except subprocess.CalledProcessError as e:
        return {
            "error": "Failed to generate PNG. Is mermaid-cli (mmdc) installed?",
            "details": str(e)
        }
