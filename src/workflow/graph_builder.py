from pathlib import Path

from langchain_core.documents import Document

from src.workflow.state import WorkflowState

from langgraph.graph.state import CompiledStateGraph

_CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"


def _format_context(docs: list[Document]) -> str:
    pass


class WorkflowBuilder:
    """LangGraph 조립 (실습에서 구현)."""

    def __init__(self) -> None:
        pass

    def _load_docs(self, state: WorkflowState) -> WorkflowState:
        pass

    def _split_docs(self, state: WorkflowState) -> WorkflowState:
        pass

    def _build_store(self, state: WorkflowState) -> WorkflowState:
        pass

    def _generate_question(self, state: WorkflowState) -> WorkflowState:
        pass

    def _retrieve_context(self, state: WorkflowState) -> WorkflowState:
        pass

    def build(self) -> CompiledStateGraph:
        pass
