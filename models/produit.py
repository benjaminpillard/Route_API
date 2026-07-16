from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from models.database import Base
from sqlalchemy.orm import relationship

from models.produit_menu import produit_menu_association_table
from models.commande_produit import association_table

class Produit(Base):
    __tablename__ = "produits"

    id = Column(Integer, primary_key=True, index=True)
    produit = Column(String) # changer titre en title 
    price = Column(Float)

    
    user_id = Column(Integer, nullable=True) # a enlever 

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    menus = relationship("Menu", 
        secondary=produit_menu_association_table,
        back_populates="produits"
    )

    commandes = relationship("Commande", 
        secondary=association_table,
        back_populates="produits"
    )