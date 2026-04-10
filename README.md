# PaperClinic

* PDF 문서를 읽어 질문을 만들고, 학생 답안을 문서 근거와 평가 기준으로 채점하는 실습용 프로젝트 
* LangGraph 사용

## 실행

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

- CLI: `python app.py <파일.pdf> -a "학생 답안"`
- UI: `streamlit run streamlit_app.py`

## 코드 구성

```mermaid
flowchart TB
    subgraph entry["진입점"]
        app["app.py"]
        st["streamlit_app.py"]
    end

    subgraph wf["workflow"]
        gb["graph_builder.py"]
        state["state.py"]
    end

    subgraph svc["services"]
        ds["document_service"]
        rs["retrieval_service"]
        llm["llm_service"]
        qs["question_service"]
        ev["evaluation_service"]
    end

    subgraph cfg["config"]
        py["prompts.yaml"]
        ey["evaluation.yaml"]
    end

    subgraph util["utils"]
        pm["prompt_manager"]
        yl["yaml_loader"]
    end

    app --> gb
    st --> gb
    gb --> ds
    gb --> rs
    gb --> llm
    gb --> qs
    gb --> ev
    qs --> pm
    ev --> pm
    ev --> ey
    pm --> py
```

## LangGraph 흐름과 평가

```mermaid
flowchart LR
    A[load_docs] --> B[split_docs]
    B --> C[build_store]
    C --> D[generate_question]
    D --> E[retrieve_context]
    E --> F([END])

    G[학생 답 입력] --> H[evaluation.evaluate]
    D -.->|"question"| H
    E -.->|"context"| H
```

`WorkflowBuilder.evaluation`으로 질문·근거·학생 답을 넘겨 평가

## 환경 변수 `.env`


| 변수 | 필수 | 설명 |
|------|------|------|
| `OPENAI_API_KEY` | 예 | 임베딩용 **OpenAI 공식 API** 키 |
| `FACTCHAT_API_KEY` | 예 | 채팅용 키 (임베딩 키와 별도) |
| `FACTCHAT_BASE_URL` | 예 | FactChat 등 OpenAI SDK 호환 엔드포인트 베이스 URL (예: `https://.../v1`) |
| `FACTCHAT_MODEL` | 예 | 해당 엔드포인트에서 쓸 모델 이름 |
| `LANGCHAIN_TRACING_V2` | 아니오 | `true`로 두면 LangSmith 추적 |
| `LANGCHAIN_API_KEY` | 아니오 | LangSmith API 키 |
| `LANGCHAIN_PROJECT` | 아니오 | LangSmith 프로젝트 이름 |

