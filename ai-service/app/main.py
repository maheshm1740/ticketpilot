from fastapi import FastAPI

app = FastAPI(title="TicketPilot AI Service")

@app.get("/health")
def health():
    return {"status": "ok"}
