from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from models.database import get_db
from models.user import User

from utils.auth import require_role

from schemas.produit import ProduitCreate, ProduitOut

from controllers.produit import (
    create_produit,
    list_produits,
    get_produit,
    update_produit,
    delete_produit
)

produit_route = APIRouter(
    prefix="/produits",
    tags=["Produits"]
)


@produit_route.get("/", response_model=list[ProduitOut])
def list_produits_route(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return list_produits(skip, limit, db)


@produit_route.get("/{produit_id}", response_model=ProduitOut)
def get_produit_route(
    produit_id: int,
    db: Session = Depends(get_db)
):
    return get_produit(db, produit_id)


@produit_route.post("/", response_model=ProduitOut, status_code=status.HTTP_201_CREATED)
def create_produit_route(
    produit: ProduitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return create_produit(db, produit)

@produit_route.put("/{produit_id}", response_model=ProduitOut)
def update_produit_route(
    produit_id: int,
    produit: ProduitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return update_produit(db, produit_id, produit)


@produit_route.delete("/{produit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_produit_route(
    produit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    delete_produit(db, produit_id)

    return None