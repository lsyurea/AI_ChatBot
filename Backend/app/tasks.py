from ai import getResponseFromOpenAI
from fastapi import APIRouter
from pydantic import UUID4
from models import Conversation, ConversationFull, ConversationPOST, ConversationPUT, Prompt, APIError
from errors import InvalidParamError, ResourceNotFoundError, UnableToCreateResourceError, InternalServerError
import uuid

task_router = APIRouter()

@task_router.get("/")
async def read_root():
    return {"message": "This is a python server that controls LLM Chat interactions."}


# Start of conversation
@task_router.post("/conversations/", status_code=201)
async def create_conversation(convo: dict):
    # check if the input is valid
    try:
        _ = ConversationPOST(**convo)
    except Exception as e:
        raise InvalidParamError()
    
    # Process the validated input and create the conversation
    try:
        # fill up the missing fields
        convo['id'] = str(uuid.uuid4())
        convo['tokens'] = 0
        if not 'params' in convo:
            convo['params'] = {}
        convo['messages'] = []
        convo_instance = ConversationFull(**convo)

        # save to the database
        await convo_instance.insert()

    except Exception as e:
        raise InternalServerError()
    
    return {"id": convo_instance.id}

@task_router.get("/conversations", status_code=200)
async def get_all_conversations():
    try:
        conversations = await ConversationFull.find_all().to_list()
        return list(map(lambda x: Conversation(id=str(x.id), name=x.name, params=x.params, tokens=x.tokens), conversations))
    except Exception as e:
        raise ResourceNotFoundError()


@task_router.put("/conversations/{id}", status_code=204)
async def update_conversation(id: UUID4, convo: dict):
    # check if the input is valid
    try:
        _ = ConversationPUT(**convo)
    except Exception as e:
        raise InvalidParamError()

    # update to conversationPost if exists, else create

    try:
        convo_get = await ConversationFull.find_one(ConversationFull.id == id)
        if not convo_get:
            try: 
                convo_get = await ConversationFull.create(id=str(uuid.uuid4()) , name=convo.name, params=convo.params, tokens=0, messages=[])
                return convo_get
            except Exception as e:
                raise ResourceNotFoundError()

        # update
        try:
            # update the missing fields
            if 'name' in convo:
                convo_get.name = convo['name']
            if 'params' in convo:
                convo_get.params = convo['params']
            # save to the database
            await convo_get.save()

        except Exception as e:
            raise InternalServerError()
        
    except Exception as e:
        raise InternalServerError()
    return convo


@task_router.get("/conversations/{id}", status_code=200)
async def get_conversation(id: UUID4):
    try:
        convo_instance = await ConversationFull.get(id)
        if not convo_instance:
            raise ResourceNotFoundError()
    except Exception as e:
        if e.__class__.__name__ == "ResourceNotFoundError":
            raise ResourceNotFoundError()
        raise InternalServerError()
    return convo_instance

@task_router.delete("/conversations/{id}", status_code=204)
async def delete_conversation(id: UUID4):
    try:
        conversation = await ConversationFull.get(id)
        if not conversation:
            raise ResourceNotFoundError()
    except Exception as e:
        if e.__class__.__name__ == "ResourceNotFoundError":
            raise ResourceNotFoundError()
        raise InternalServerError()
    
    try:
        await conversation.delete()
    except Exception as e:
        raise InternalServerError()

@task_router.post("/queries/")
async def create_query(id: str, convo: dict, status_code=201):
    
    try:
        convo_cur = await ConversationFull.get(id)
        if not convo_cur:
            raise ResourceNotFoundError()
    except Exception as e:
        if e.__class__.__name__ == "ResourceNotFoundError":
            raise ResourceNotFoundError()
        raise InternalServerError()

    # check if the input is valid
    try:
        convo_updated = Prompt(**convo)
        
        try:
            res = getResponseFromOpenAI(convo_updated)
            # Update the conversation
            if not res:
                raise UnableToCreateResourceError()
            msg = res.choices[0].message
            convo_cur.tokens += res.usage.total_tokens
            convo_cur.messages.append(Prompt(**{"role": msg.role, "content": msg.content}))
            await convo_cur.save()
            return {"id": id}


        except Exception as e:
            raise UnableToCreateResourceError()
    except Exception as e:
        raise InvalidParamError()
