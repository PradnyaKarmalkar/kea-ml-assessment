from fastapi import FastAPI
import time

from app.schemas import QueryRequest, QueryResponse
from app.similarity import find_best_match

app = FastAPI(title="KeaBuilder ML Service")


@app.get("/")
def home():
    return {"message": "ML Similarity Service Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/match", response_model=QueryResponse)
def match_query(request: QueryRequest):
    start_time = time.time()

    result = find_best_match(request.query)

    latency = round((time.time() - start_time) * 1000, 2)

    return {
        **result,
        "latency_ms": latency
    }