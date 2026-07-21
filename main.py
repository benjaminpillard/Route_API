from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from models.database import Base, engine

from routes.menu_route import menu_route
from routes.produit_route import produit_route
from routes.commande_route import commande_route
from routes.utilisateur_route import utilisateur_route

from utils.setting import settings


app = FastAPI()
Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(produit_route)
app.include_router(menu_route)
app.include_router(commande_route)
app.include_router(utilisateur_route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)