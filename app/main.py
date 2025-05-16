from fastapi import FastAPI
from app.sentiment import analyze_sentiment
from app.config import settings

app = FastAPI(title = settings.app_name)

@app.get("/")
def health():
    return {"status" : "ok"}

@app.post("/analyze")
def analyze(text: str):
    return {"sentiment": analyze_sentiment(text)}