from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from models.database import get_db
from models.user import User
from utils.auth import require_role

from schemas.commande import CommandeCreate, CommandeOut

from controllers.commande import (
    create_commande,
    list_commandes,
    get_commande,
    update_commande,
    delete_commande,
    add_produit_to_commande,
    remove_produit_from_commande
)

commande_route = APIRouter(
    prefix="/commandes",
    tags=["Commandes"]
)


@commande_route.get("/", response_model=list[CommandeOut])
def list_commandes_route(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "preparateur", "accueil"))
):
    return list_commandes(skip, limit, db)


@commande_route.get("/{commande_id}", response_model=CommandeOut)
def get_commande_route(
    commande_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "preparateur", "accueil"))
):
    return get_commande(db, commande_id)


@commande_route.post("/", response_model=CommandeOut, status_code=status.HTTP_201_CREATED)
def create_commande_route(
    commande: CommandeCreate,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "accueil"))
):
    return create_commande(db, commande)


@commande_route.put("/{commande_id}", response_model=CommandeOut)
def update_commande_route(
    commande_id: int,
    commande: CommandeCreate,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "preparateur"))
):
    return update_commande(db, commande_id, commande)


@commande_route.delete("/{commande_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commande_route(
    commande_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur"))
):
    delete_commande(db, commande_id)
    return None


@commande_route.post("/{commande_id}/produits/{produit_id}", response_model=CommandeOut)
def add_produit_to_commande_route(
    commande_id: int,
    produit_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "preparateur"))
):
    return add_produit_to_commande(db, commande_id, produit_id)


@commande_route.delete("/{commande_id}/produits/{produit_id}", response_model=CommandeOut)
def remove_produit_from_commande_route(
    commande_id: int,
    produit_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("administrateur", "preparateur"))
):
    return remove_produit_from_commande(db, commande_id, produit_id)