from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/")
async def read_root():
    return {"message": "This is a python server"}
