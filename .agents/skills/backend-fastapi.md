---
description: How to set up and develop the FastAPI backend for the Movie Ticket Booking project, deployed on Render
---

# Backend — FastAPI on Render

## Overview
The backend is a **FastAPI** (Python) application that serves as the REST API for the Movie Ticket Booking system. It connects to the Neon PostgreSQL database and is deployed on **Render**.

## Setup Steps

### 1. Initialize the FastAPI Project
```bash
cd backend/
python -m venv venv
# Activate: venv\Scripts\activate (Windows)
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv alembic
pip freeze > requirements.txt
```

### 2. Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── config.py           # Settings & env vars
│   ├── database.py         # DB connection setup
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── routers/            # API route modules
│   │   ├── movies.py
│   │   ├── bookings.py
│   │   ├── users.py
│   │   └── payments.py
│   └── utils/              # Helper functions
├── requirements.txt
├── .env.example
├── render.yaml             # Render deployment config
└── Dockerfile              # (optional) for containerized deploy
```

### 3. Key API Endpoints (planned)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/movies` | List all movies |
| GET | `/movies/{id}` | Movie details |
| GET | `/shows` | List showtimes |
| POST | `/bookings` | Create a booking |
| GET | `/bookings/{id}` | Booking details |
| POST | `/users/register` | User registration |
| POST | `/users/login` | User login |

### 4. Render Deployment
1. Push code to a GitHub repo
2. Go to [https://dashboard.render.com](https://dashboard.render.com)
3. Create a new **Web Service**
4. Connect your GitHub repo → select `backend/` root
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Add environment variables (DB connection string, secrets)

### 5. Key Dependencies
- `fastapi` — Web framework
- `uvicorn` — ASGI server
- `sqlalchemy` — ORM
- `psycopg2-binary` — PostgreSQL driver
- `python-dotenv` — Environment variable management
- `alembic` — Database migrations
- `pydantic` — Data validation
