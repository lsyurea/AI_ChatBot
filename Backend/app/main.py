from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tasks import task_router
from db import init_db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(task_router)
