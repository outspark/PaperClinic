import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from src.workflow.graph_builder import WorkflowBuilder


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="문서 기반 질문 생성 후 학생 답 평가")
    parser.add_argument("pdf", type=Path, help="입력 PDF 경로")
    parser.add_argument(
        "-a",
        "--answer",
        required=True,
        help="학생 답안",
    )
    args = parser.parse_args()
    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file():
        parser.error(f"PDF 파일이 없습니다: {pdf_path}")

    builder = WorkflowBuilder()
    graph = builder.build()

    result = graph.invoke({"file_path": str(pdf_path)})

    evaluation = builder.evaluation.evaluate(
        question=result["generated_question"],
        user_answer=args.answer,
        context=result["retrieved_context"],
    )

    print("=== Generated question ===")
    print(result["generated_question"])
    print("\n=== Evaluation ===")
    print(json.dumps(evaluation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
