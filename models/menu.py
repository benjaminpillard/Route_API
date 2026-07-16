from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.database import Base
from models.produit_menu import produit_menu_association_table

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    price = Column(Float)

    produits = relationship(
        "Produit", 
        secondary=produit_menu_association_table,
        back_populates="menus"
    )