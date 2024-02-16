from typing import List
from beanie import Document 
from pydantic import BaseModel, Enum, UUID4, Field

class Request(BaseModel):
    description: str

class Details(BaseModel):
    description: str

class ConversationParams(BaseModel):
    description: str

class QueryRoleType(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    function = "function"

class Prompt(Document, QueryRoleType):
    role: QueryRoleType
    content: str

class ChatMessage(BaseModel, Prompt):
    prompts: List[Prompt]

class APIError(Document, Request, Details):
    code: int
    message: str
    request: Request
    details: Details

class Conversation(Document, ConversationParams):
    id: UUID4
    name: str=Field(max_length=200)
    params: ConversationParams
    tokens: int

class ConversationFull(Document, ConversationParams, ChatMessage):
    id: UUID4
    name: str=Field(max_length=200)
    params: ConversationParams
    tokens: int
    messages: List[ChatMessage]

class ConversationPOST(BaseModel, ConversationParams):
    name: str=Field(max_length=200)
    params: ConversationParams

class ConversationPUT(BaseModel, ConversationParams):
    name: str=Field(max_length=200)
    params: ConversationParams