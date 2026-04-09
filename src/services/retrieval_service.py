import os

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


class RetrievalService:
    def __init__(self, embedding_model: str = "text-embedding-3-small") -> None:
        self._embeddings = OpenAIEmbeddings(
            model=embedding_model,
            api_key=os.environ["OPENAI_API_KEY"],
        )

    def build_store(self, splits: list[Document]) -> FAISS:
        return FAISS.from_documents(splits, self._embeddings)

    def retrieve(self, store: FAISS, query: str, k: int = 4) -> list[Document]:
        return store.similarity_search(query, k=k)
