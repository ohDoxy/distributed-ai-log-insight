from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# data model for a single post log entry
# create a table named logentry
class LogEntryCreate(SQLModel):
    timestamp: datetime # a column named timestamp
    source_ip: str # ..etc
    event_type: str
    message: str
    severity: Optional[str] = "info"

# used for database model + response
class LogEntry(LogEntryCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)