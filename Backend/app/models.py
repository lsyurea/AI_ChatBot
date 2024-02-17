from typing import List, Optional
from beanie import Document 
from enum import Enum
from typing import Optional
from beanie import Document 
from pydantic import UUID4, Field
from enum import Enum

# Represents the schema for the mongo database

class QueryRoleType(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    function = "function"

class Prompt(Document):
    role: QueryRoleType
    content: str

class APIError(Document):
    code: int
    message: str
    request: Optional[dict] = None
    details: Optional[dict] = None

class Conversation(Document):
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

class ConversationPOST(Document):
    name: str = Field(max_length=200)
    params: Optional[dict] = None

class ConversationPUT(Document):
    name: Optional[str] = Field(max_length=200)
    params: Optional[dict] = None