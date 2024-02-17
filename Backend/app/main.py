from fastapi import FastAPI
from tasks import task_router
from db import init_db

app = FastAPI()

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(task_router)
