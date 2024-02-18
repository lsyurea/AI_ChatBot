from ai import getResponseFromOpenAI
from fastapi import APIRouter
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
async def update_conversation(id: int, convo: dict):
    # check if the input is valid
    try:
        _ = ConversationPUT(**convo)
    except Exception as e:
        raise InvalidParamError()

    # update to conversationPost if exists, else create
    try:
        convo_get = await ConversationFull.find_one(id=id)
        print(convo_get)
        # update
        try:
            # update the missing fields
            if 'name' in convo:
                convo_get.name = convo.name
            if 'params' in convo:
                convo_get.params = convo.params
            # save to the database
            await convo_get.save()

        except Exception as e:
            raise InternalServerError()
        
    except Conversation.DoesNotExist:
        # create
        try:
            conversation = await Conversation.create(name=convo.name, params=convo.params)
        except Exception as e:
            raise ResourceNotFoundError()

    except Exception as e:
        raise InternalServerError()
    return convo


@task_router.get("/conversations/{id}", status_code=200)
async def get_conversation(id: int):
    try:
        convo_instance = await ConversationFull.get(id=id)
    except convo_instance.DoesNotExist:
        raise ResourceNotFoundError()
    except Exception as e:
        raise InternalServerError()
    return convo_instance



@task_router.delete("/conversations/{id}", status_code=204)
async def delete_conversation(id: int):
    try:
        conversation = await ConversationFull.get(id=id)
    except Conversation.DoesNotExist:
        raise ResourceNotFoundError()
    except Exception as e:
        raise InternalServerError()
    
    try:
        await conversation.delete()
    except Exception as e:
        raise InternalServerError()
    return {"message": "Conversation deleted successfully"}

@task_router.post("/queries/")
async def create_query(convo: dict, status_code=201):
    
    # check if the input is valid
    try:
        convo_updated = ConversationFull(**convo)
        try:
            return getResponseFromOpenAI(convo_updated)
        except Exception as e:
            raise UnableToCreateResourceError()
    except Exception as e:
        raise InvalidParamError()
