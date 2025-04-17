import re
from pathlib import Path
from graph_config.model import GraphState
from tools.analyze_srs import llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_unit_tests(state:GraphState)->GraphState:
    """Uses LLM to generate unit test based on SRS analysis string. Parses analysis string , extract endpoints/models and create pytest tests."""

    print(state.analysis)
    if not state.analysis:
        raise ValueError("Missing analysis in state")
    

    prompt = ChatPromptTemplate.from_messages([
        ("system","You are an expert in FastAPI and pytest TDD developement"),
        ("user","Generate complete pytest unit tests for this FastAPi backend.Be modular, cover all logic and edge case .Use proper assertions and mocks.Here is the analysis of the Requirement from the SRS document {analysis}")
    ])
    chain= prompt| llm| StrOutputParser()

    print("LLm generating unit test")
    test_code = chain.invoke({"analysis":state.analysis})

    print("Unit tests generated.")

    # Create test folder
    test_dir = Path("./generated_project/tests")
    test_dir.mkdir(parents=True, exist_ok=True)

    # Parse markdown and extract each test file
    pattern = r"\*\*(\w+\.py)\*\*\s*```(?:python)?(.*?)```"
    matches = re.findall(pattern, test_code, re.DOTALL)

    unit_test_dict = {}

    for filename, code in matches:
        filepath = test_dir / filename
        cleaned_code = code.strip()

        with open(filepath, "w") as f:
            f.write(cleaned_code)

        unit_test_dict[filename] = cleaned_code
        print(f"Saved test: {filepath}")

    state.unit_test = unit_test_dict
    return state
