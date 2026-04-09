from langchain_core.messages import BaseMessage


class LLMService:
    def __init__(self, temperature: float = 0.2) -> None:
        pass

    def invoke(self, messages: list[BaseMessage]) -> str:
        pass


if __name__ == "__main__":
    # 프로젝트 루트에서, .env에 FACTCHAT_* 설정 후:
    # python -m src.services.llm_service
    from dotenv import load_dotenv
    from langchain_core.messages import HumanMessage, SystemMessage

    load_dotenv()

    llm = LLMService()
    text = llm.invoke(
        [
            SystemMessage(content="짧게 한 문장으로만 답하세요."),
            HumanMessage(content="1+1은?"),
        ]
    )
    print(text)
