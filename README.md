# ResearchAI

ResearchAI is an enterprise-grade platform foundation for an IEEE compliance workflow. Sprint 1 focuses on a scalable architecture without implementing validation, PDF parsing, AI, or business logic.

## Architecture

- Backend: FastAPI, SQLAlchemy 2, Alembic, PostgreSQL, Pydantic v2
- Frontend: React, Vite, TailwindCSS, Axios
- Structured logging, environment-based configuration, and modular package organization

## Folder Structure

```text
researchai/
backend/
frontend/
docs/
storage/
logs/
```

## Installation

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Running Backend

```bash
cd backend
uvicorn main:app --reload
```

## Running Frontend

```bash
cd frontend
npm run dev
```

