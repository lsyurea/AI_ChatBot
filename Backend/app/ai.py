import os
from models import Prompt
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
load_dotenv(find_dotenv())

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

# This is to implement get request from the OpenAI API
def getResponseFromOpenAI(convo: Prompt) -> str:

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": convo.role, "content": convo.content}],
    )
    return completion
