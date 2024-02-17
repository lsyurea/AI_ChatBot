from fastapi import APIRouter, HTTPException
from models import Conversation, ConversationFull, ConversationPOST, ConversationPUT, Prompt, APIError
from pydantic import ValidationError

task_router = APIRouter()

@task_router.get("/")
async def read_root():
    return {"message": "This is a python server that controls LLM Chat interactions."}


@task_router.get("/conversations")
async def get_all_conversations():
    print("executing get_all_conversations")
    try:
        conversations = await ConversationFull.all().to_list()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return conversations


@task_router.post("/conversations/", response_model=ConversationPOST, status_code=201)
async def create_conversation(convo: ConversationPOST):
    # Validate input using Pydantic model
    print("executing create_conversation")
    try:
        _ = ConversationPOST(**convo.dict())
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Process the validated input and create the conversation
    try:
        # Replace this with your actual conversation creation logic
        conversation = await Conversation.create(name=convo.name, params=convo.params)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Return the created conversation
    return conversation


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