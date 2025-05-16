# Sentiment Checker API

A simple FastAPI app that analyzes the sentiment of a sentence and returns `positive`, `negative`, or `neutral`.

---

## Features

- Built with **FastAPI**
- Sentiment detection using **TextBlob**
- Auto-config via **`.env`** and **Pydantic**
- Unit tested with **Pytest**
- CI using **GitHub Actions**
- Dockerized

---

## How to Run Locally

```bash
git clone https://github.com/samriddhi004/Sentiment-Checker.git
cd Sentiment-Checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
venv/bin/python -m uvicorn app.main:app --reload
```
Then open your browser and go to:
 http://127.0.0.1:8000/docs
