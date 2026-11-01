import os
import platform

from fastapi import FastAPI

app = FastAPI(title="Demo Python na Nextcluster")


@app.get("/")
def home():
    return {
        "mensagem": "Olá do FastAPI na Nextcluster!",
        "python": platform.python_version(),
        "porta": os.environ.get("PORT"),
    }


@app.get("/health")
def health():
    return {"ok": True}
