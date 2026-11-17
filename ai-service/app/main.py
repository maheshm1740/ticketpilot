from fastapi import FastAPI, HTTPException

from .llm import provider
from .schemas import ClassifyRequest, ClassifyResponse

app = FastAPI(title="TicketPilot AI Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/classify", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    try:
        return provider.classify(req)
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=502, detail="LLM provider failed")
