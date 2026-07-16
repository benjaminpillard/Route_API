from typing import Optional
from pydantic import BaseModel

class CommandeCreate(BaseModel):
    numero: int
    statut: str
    total: float
    user_id: Optional[int] = None

class CommandeOut(CommandeCreate):
    id: int

    class Config:
        from_attributes = True