import os
from models import ConversationFull
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
load_dotenv(find_dotenv())

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

# This is to implement get request from the OpenAI API
def getResponseFromOpenAI(convo: ConversationFull) -> str:
    msgs = convo.messages
    if convo.params:
        params_message = f"Parameters: {convo.params}"
        msgs.append({"role": "user", "content": params_message})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs,
        max_tokens=convo.tokens,
        # name=convo.name
    )
    return completion.choices[0].message    
