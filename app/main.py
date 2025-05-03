from fastapi import FastAPI
from app.api import routes
from app.core.config import create_db_and_tables

app = FastAPI()
create_db_and_tables()

# include routes
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "API is running"}