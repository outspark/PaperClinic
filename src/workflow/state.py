from typing import Any, TypedDict

from langchain_core.documents import Document


class WorkflowState(TypedDict, total=False):
    file_path: str
    raw_documents: list[Document]
    splits: list[Document]
    vector_store: Any
    generated_question: str
    retrieved_context: str
