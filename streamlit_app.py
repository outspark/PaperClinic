import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from src.workflow.graph_builder import WorkflowBuilder


@st.cache_resource
def builder() -> WorkflowBuilder:
    return WorkflowBuilder()


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="PaperClinic", layout="wide")
    st.title("문서 기반 질문 · 답안 평가")

    b = builder()
    graph = b.build()

    uploaded = st.file_uploader("PDF 업로드", type=["pdf"])

    if st.button("질문 생성") and uploaded is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded.getvalue())
            path = tmp.name
        try:
            out = graph.invoke({"file_path": path})
        finally:
            os.unlink(path)
        st.session_state["generated_question"] = out["generated_question"]
        st.session_state["retrieved_context"] = out["retrieved_context"]

    if "generated_question" in st.session_state:
        st.subheader("생성된 질문")
        st.write(st.session_state["generated_question"])

        with st.expander("검색된 문서 근거 (참고)"):
            st.text(st.session_state["retrieved_context"])

        answer = st.text_area("학생 답안", height=200, key="student_answer")

        if st.button("평가하기") and answer.strip():
            ev = b.evaluation.evaluate(
                question=st.session_state["generated_question"],
                user_answer=answer.strip(),
                context=st.session_state["retrieved_context"],
            )
            st.subheader("평가 결과")
            st.json(ev)


if __name__ == "__main__":
    main()
