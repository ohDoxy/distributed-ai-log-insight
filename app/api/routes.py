from fastapi import APIRouter, HTTPException
from app.models.log import LogEntry, LogEntryCreate
from sqlmodel import Session, select
from app.core.config import engine
from datetime import datetime
from typing import List

router = APIRouter()

# a router to get logs
@router.get("/logs", response_model=List[LogEntry])
def get_all_logs():
    # open new db session
    with Session(engine) as session:
        result = session.exec(select(LogEntry)) # SELECT * FROM logentry

        # get all rows
        logs = result.all()
        return logs


# receives a JSON log and saves it into the database
@router.post("/logs")
def ingest_log(entry: LogEntryCreate):

    # for timestamp string conversion to datetime
    if isinstance(entry.timestamp, str):
        ts = entry.timestamp.rstrip("Z") # remove trailing Z so we can convert
        try:
            entry.timestamp = datetime.fromisoformat(ts)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid timestamp format")
        
    # convert Pydantic model to SQLModel instance
    log = LogEntry(**entry.dict())

    # create a new database session with the engine
    with Session(engine) as session:
        session.add(log)
        session.commit() # save changes to db
        session.refresh(log)

    return {"message": "Log saved", "log_id": log.id}