from typing import List, Optional
from beanie import Document 
from enum import Enum
from pydantic import UUID4, Field, BaseModel

# Represents the schema for the mongo database

class QueryRoleType(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    function = "function"

class Prompt(BaseModel):
    role: QueryRoleType
    content: str

class APIError(BaseModel):
    code: int
    message: str
    request: Optional[dict] = None
    details: Optional[dict] = None

class Conversation(BaseModel):
    id: UUID4
    name: str=Field(max_length=200)
    params: dict
    tokens: int

class ConversationFull(Document):
    id: UUID4
    name: str = Field(max_length=200)
    params: dict
    tokens: int
    messages: List[Prompt]

class ConversationPOST(BaseModel):
    name: str = Field(max_length=200)
    params: Optional[dict] = None

class ConversationPUT(BaseModel):
    name: Optional[str] = Field(max_length=200)
    params: Optional[dict] = None