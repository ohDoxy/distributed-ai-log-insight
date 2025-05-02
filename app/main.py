from fastapi import FastAPI
from app.api import routes

app = FastAPI()

# include routes
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "API is running"}