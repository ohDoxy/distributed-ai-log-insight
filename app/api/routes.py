from fastapi import APIRouter
from app.models.log import LogEntry

router = APIRouter()

# temp storage
logs = []

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/logs")
def ingest_log(entry: LogEntry):
    logs.append(entry)
    return {"message": "Log recieved", "log_count": len(logs)}