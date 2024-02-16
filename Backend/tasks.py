from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/")
async def read_root():
    return {"message": "This is a python server that controls LLM Chat interactions."}

@task_router.get("/conversations")
async def get_all_conversations():
    return {"message": "Get all conversations"}

@task_router.post("/conversations")
async def create_conversation():
    return {"message": "Create a conversation"}

@task_router.get("/conversations/{id}")
async def get_conversation(id: int):
    return {"message": f"Get conversation with id {id}"}

@task_router.put("/conversations/{id}")
async def update_conversation(id: int):
    return {"message": f"Update conversation with id {id}"}

@task_router.delete("/conversations/{id}")
async def delete_conversation(id: int):
    return {"message": f"Delete conversation with id {id}"}

@task_router.post("/queries")
async def create_query():
    return {"message": "Create a query"}