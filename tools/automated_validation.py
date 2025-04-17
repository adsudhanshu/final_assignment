import subprocess
import sys
import os
from graph_config.model import GraphState

def detect_missing_packages(error_message: str):
    missing_packages = []
    if "ModuleNotFoundError" in error_message:
        lines = error_message.splitlines()
        for line in lines:
            if "ModuleNotFoundError" in line:
                package_name = line.split("No module named ")[1]
                missing_packages.append(package_name)
    return missing_packages

def install_missing_packages(packages: list):
    for package in packages:
        try:
            print(f" Installing missing package: {package}")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"Successfully installed: {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")

def start_fastapi():
    try:
        result = subprocess.run(
            [sys.executable,"-m","uvicorn", "generated_project.app.main:app", "--reload", "--port", "8080"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print("FastAPI app started successfully.")
            return True
        else:
            missing_packages = detect_missing_packages(result.stderr)
            if missing_packages:
                print(f" Missing packages: {missing_packages}")
                install_missing_packages(missing_packages)
                return start_fastapi()  # Recursive retry
            else:
                print(f"FastAPI failed to start: {result.stderr}")
            return False
    except Exception as e:
        print(f"FastAPI failed to start: {e}")
        return False

def run_tests():
    try:
        test_result = subprocess.run(
            ["pytest", "generated_project/tests", "--maxfail=1", "--disable-warnings", "-q"],
            capture_output=True, text=True
        )
        if test_result.returncode == 0:
            print("All tests passed.")
        else:
            missing_packages = detect_missing_packages(test_result.stderr)
            if missing_packages:
                print(f"Missing packages in tests: {missing_packages}")
                install_missing_packages(missing_packages)
                return run_tests()  # Recursive retry
            else:
                print(f"Some tests failed: {test_result.stderr}")
    except Exception as e:
        print(f"Error running tests: {e}")

def automated_validation_node(state: GraphState) -> GraphState:
    print(" Starting automated validation node")
    
    if state.metadata is None:
        state.metadata = {}

    # Step 1: Re-run FastAPI and tests
    fastapi_status = start_fastapi()
    if fastapi_status:
        run_tests()

    return state
