import motor
import motor.motor_asyncio
from models import Conversation, ConversationFull, ConversationPOST, ConversationPUT, Prompt, APIError
import beanie


async def init_db():
    # use it if you want to run python3 run.py directly or with uvicorn and docker compose up -d
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    # use it if you just want to run docker compose up -d
    # client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://ai_db:27017")
    # initialising schema does not work down below even after referring to documentation
    await beanie.init_beanie(database=client.db_name, document_models=[Conversation, Prompt, APIError, ConversationFull, ConversationPOST, ConversationPUT])