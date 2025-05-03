from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# data model for a single entry
class LogEntry(BaseModel):
    timestamp: datetime # when
    source_ip: str # where the event came from
    event_type: str # what type of event (i.e "login_failure")
    message: str
    severity: Optional[str] = "info" # optional flag (warning, critical)