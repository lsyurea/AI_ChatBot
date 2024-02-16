from fastapi import FastAPI
from tasks import task_router

app = FastAPI()

app.include_router(task_router)
