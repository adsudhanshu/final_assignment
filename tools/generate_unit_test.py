
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

    print("Unit test")
    print(test_code)

    state.unit_test=test_code.strip()
    return state