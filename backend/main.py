from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import psycopg2
import bcrypt
import hashlib

app = FastAPI(title="Movie Ticket Booking API")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper functions to handle password hashing with direct use of bcrypt
# and pre-hashing with SHA256 to avoid the 72-byte limit.
def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    sha256_hash = hashlib.sha256(pwd_bytes).digest()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(sha256_hash, salt).decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    pwd_bytes = password.encode('utf-8')
    sha256_hash = hashlib.sha256(pwd_bytes).digest()
    try:
        return bcrypt.checkpw(sha256_hash, hashed_password.encode('utf-8'))
    except Exception:
        return False

class UserRegister(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

def get_db_conn():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise HTTPException(status_code=500, detail="DATABASE_URL not set")
    return psycopg2.connect(db_url)

@app.get("/")
async def root():
    return {"message": "Welcome to Movie Ticket Booking API", "status": "online"}

@app.get("/db-check")
async def db_check():
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return {"status": "connected", "database_version": version[0]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/register")
async def register(user: UserRegister):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        # Check if user already exists
        cur.execute("SELECT id FROM users WHERE email = %s OR username = %s", (user.email, user.username))
        if cur.fetchone():
            raise HTTPException(status_code=400, detail="User already exists")
        
        hashed_password = hash_password(user.password)
        cur.execute(
            "INSERT INTO users (username, email, phone_number, password_hash) VALUES (%s, %s, %s, %s)",
            (user.username, user.email, user.phone_number, hashed_password)
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@app.post("/login")
async def login(user: UserLogin):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, username, password_hash FROM users WHERE email = %s", (user.email,))
        db_user = cur.fetchone()
        
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not verify_password(user.password, db_user[2]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return {"message": "Login successful", "user": {"id": db_user[0], "username": db_user[1]}}
    finally:
        cur.close()
        conn.close()
