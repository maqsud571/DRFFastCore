# str/api/schemas/user.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    age: int
