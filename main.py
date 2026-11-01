import os
import platform

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Demo Python na Nextcluster")


@app.get("/")
def home():
    return {
        "mensagem": "Olá do FastAPI na Nextcluster!",
        "python": platform.python_version(),
        "porta": os.environ.get("PORT"),
        "banco": "ligado" if os.environ.get("DATABASE_URL") else "sem DATABASE_URL",
    }


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/db")
def db():
    """Conta visitas no PostgreSQL indicado em DATABASE_URL (variável de ambiente do app)."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise HTTPException(503, "Defina DATABASE_URL nas variáveis de ambiente do app.")
    import psycopg

    with psycopg.connect(url, connect_timeout=5) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visitas (id serial PRIMARY KEY, em timestamptz NOT NULL DEFAULT now())")
        conn.execute("INSERT INTO visitas DEFAULT VALUES")
        total = conn.execute("SELECT count(*) FROM visitas").fetchone()[0]
        versao = conn.execute("SHOW server_version").fetchone()[0]
    return {"visitas": total, "postgres": versao}
