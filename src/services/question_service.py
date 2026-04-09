from langchain_core.messages import HumanMessage, SystemMessage

from src.services.llm_service import LLMService
from src.utils.prompt_manager import PromptManager


class QuestionService:
    def __init__(self, llm: LLMService, prompts: PromptManager) -> None:
        self._llm = llm
        self._prompts = prompts

    def generate_question(self, context: str) -> str:
        user = self._prompts.render_user("question_generation", context=context)
        system = self._prompts.system_prompt("question_generation")
        messages = [
            SystemMessage(content=system),
            HumanMessage(content=user),
        ]
        return self._llm.invoke(messages).strip()
