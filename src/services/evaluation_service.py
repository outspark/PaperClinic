import json
from pathlib import Path

from src.services.llm_service import LLMService
from src.utils.prompt_manager import PromptManager


def _parse_json_from_llm(text: str) -> dict:
    pass


class EvaluationService:
    def __init__(
        self,
        llm: LLMService,
        prompts: PromptManager,
        evaluation_config_path: Path | str,
    ) -> None:
        pass

    def _criteria_block(self) -> str:
        pass

    def _max_score(self) -> int:
        pass

    def evaluate(
        self,
        *,
        question: str,
        user_answer: str,
        context: str,
    ) -> dict:
        pass


if __name__ == "__main__":
    # 프로젝트 루트에서, .env 설정 후:
    # python -m src.services.evaluation_service
    from dotenv import load_dotenv

    load_dotenv()

    root = Path(__file__).resolve().parents[2]
    prompts_path = root / "config" / "prompts.yaml"
    eval_path = root / "config" / "evaluation.yaml"

    llm = LLMService()
    prompts = PromptManager(prompts_path)
    svc = EvaluationService(llm, prompts, eval_path)

    out = svc.evaluate(
        question="이 수업의 목표는?",
        user_answer="자연어 시스템을 설계하고 평가하는 능력을 기른다.",
        context="[chunk 1]\n이 수업은 NLP 시스템 설계와 평가를 다룬다.",
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))
