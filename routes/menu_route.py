from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from models.database import get_db
from models.user import User

from utils.auth import require_role

from schemas.menu import MenuCreate, MenuOut

from controllers.menu import (
    create_menu,
    list_menu,
    get_menu,
    update_menu,
    delete_menu,
    add_produit_to_menu,
    remove_produit_from_menu
)

menu_route = APIRouter(
    prefix="/menus",
    tags=["Menus"]
)


@menu_route.get("/", response_model=list[MenuOut])
def list_menu_route(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return list_menu(skip, limit, db)


@menu_route.get("/{menu_id}", response_model=MenuOut)
def get_menu_route(
    menu_id: int,
    db: Session = Depends(get_db)
):
    return get_menu(db, menu_id)


@menu_route.post("/", response_model=MenuOut, status_code=status.HTTP_201_CREATED)
def create_menu_route(
    menu: MenuCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return create_menu(db, menu)


@menu_route.put("/{menu_id}", response_model=MenuOut)
def update_menu_route(
    menu_id: int,
    menu: MenuCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return update_menu(db, menu_id, menu)


@menu_route.delete("/{menu_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_route(
    menu_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    delete_menu(db, menu_id)

    return None


@menu_route.post("/{menu_id}/produits/{produit_id}", response_model=MenuOut)
def add_produit_to_menu_route(
    menu_id: int,
    produit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return add_produit_to_menu(db, menu_id, produit_id)


@menu_route.delete("/{menu_id}/produits/{produit_id}", response_model=MenuOut)
def remove_produit_from_menu_route(
    menu_id: int,
    produit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("administrateur"))
):
    return remove_produit_from_menu(db, menu_id, produit_id)