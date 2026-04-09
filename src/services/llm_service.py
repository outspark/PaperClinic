import os

from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI


class LLMService:
    def __init__(self, temperature: float = 0.2) -> None:
        self._llm = ChatOpenAI(
            model=os.environ["FACTCHAT_MODEL"],
            temperature=temperature,
            base_url=os.environ["FACTCHAT_BASE_URL"].rstrip("/"),
            api_key=os.environ["FACTCHAT_API_KEY"],
        )

    def invoke(self, messages: list[BaseMessage]) -> str:
        response = self._llm.invoke(messages)
        content = response.content
        if isinstance(content, str):
            return content
        return "".join(str(part) for part in content)
