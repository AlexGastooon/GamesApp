from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: Optional[str]
    nickname: str
    roles: List[Role]
    
class Game(BaseModel):
    id: Optional[UUID] = uuid4()
    game_name: str
    game_description: str
    rating: int