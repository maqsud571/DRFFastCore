# str/schemas/user.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    age: int

class ItemResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True
