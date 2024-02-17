import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
load_dotenv(find_dotenv())

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You are a helpful assistant"
        },
        {
        "role": "user",
        "content": "What is the purpose of life?"
        }
    ]
)

print(completion.choices[0].message)