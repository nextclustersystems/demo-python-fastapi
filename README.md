# Demo Python (FastAPI) na Nextcluster

Exemplo mínimo para a "Aplicação com build (Docker)": a plataforma lê o `Dockerfile`, instala o `requirements.txt` e publica.

- Publicar por ZIP: compacte esta pasta (sem `.venv` nem `__pycache__`) e envie na aba **Publicar**.
- Publicar pelo GitHub: aponte o painel Git para o repositório e a branch.
- A aplicação escuta na porta da variável `PORT`. Em **Configurações**, use o health check `/health`.

Local: `docker build -t demo-python . && docker run -p 8000:8000 demo-python` e abra http://localhost:8000.
