from pydantic import BaseModel
from typing import Optional
from schemas.produit import ProduitOut

class MenuCreate(BaseModel):
    nom: str
    price: float

class MenuOut(MenuCreate):
    id: int
    produits: list[ProduitOut] = []

    class Config:
        from_attributes = True