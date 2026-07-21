# Wacdo API (FastAPI)

API REST pour gerer:
- utilisateurs (inscription, login JWT, profils)
- produits
- menus
- commandes

Le projet utilise FastAPI, SQLAlchemy, Alembic et JWT.

## Stack technique

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- PyJWT
- Pydantic Settings
- PostgreSQL (Render) ou SQLite (local)

## Prerequis

- Python 3.11+
- pip

## Installation

1. Cloner le projet puis se placer dans le dossier.
2. Creer un environnement virtuel.
3. Installer les dependances.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Variables d environnement

Le projet charge les variables depuis un fichier `.env` a la racine.

Exemple minimal:

```env
SECRET_KEY=change_this_secret
ALGORITHM=HS256
DATABASE_URL=sqlite:///./wacdo.db
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

Notes:
- `DATABASE_URL` accepte SQLite ou PostgreSQL.
- Si une URL commence par `postgresql://`, elle est adaptee automatiquement en `postgresql+psycopg://`.
- `CORS_ORIGINS` accepte plusieurs origines separees par des virgules.

## Lancer l API en local

```bash
uvicorn main:app --reload
```

Documentation interactive:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Migrations Alembic

Creer une migration:

```bash
alembic revision --autogenerate -m "description"
```

Appliquer les migrations:

```bash
alembic upgrade head
```

## Endpoints principaux

Base path par module:
- `/users`
- `/produits`
- `/menus`
- `/commandes`

Auth utilisateurs:
- `POST /users/register`
- `POST /users/login`
- `GET /users/me`
- `GET /users/all` (role admin)
- `DELETE /users/{user_id}` (role admin)

Produits:
- `GET /produits/`
- `GET /produits/{produit_id}`
- `POST /produits/` (role admin)
- `PUT /produits/{produit_id}` (role admin)
- `DELETE /produits/{produit_id}` (role admin)

Menus:
- `GET /menus/`
- `GET /menus/{menu_id}`
- `POST /menus/` (role admin)
- `PUT /menus/{menu_id}` (role admin)
- `DELETE /menus/{menu_id}` (role admin)
- `POST /menus/{menu_id}/produits/{produit_id}` (role admin)
- `DELETE /menus/{menu_id}/produits/{produit_id}` (role admin)

Commandes:
- `GET /commandes/` (roles admin, preparateur, accueil)
- `GET /commandes/{commande_id}` (roles admin, preparateur, accueil)
- `POST /commandes/` (roles admin, accueil)
- `PUT /commandes/{commande_id}` (roles admin, preparateur)
- `DELETE /commandes/{commande_id}` (role admin)
- `POST /commandes/{commande_id}/produits/{produit_id}` (roles admin, preparateur)
- `DELETE /commandes/{commande_id}/produits/{produit_id}` (roles admin, preparateur)

## Deploiement Render

Le fichier `Procfile` contient la commande web:

```bash
web: uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
```

Configuration recommandee sur Render:
- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Variables d environnement a definir:
	- `SECRET_KEY`
	- `ALGORITHM`
	- `DATABASE_URL`
	- `CORS_ORIGINS`

## Workflow Git rapide

```bash
git add .
git commit -m "Mise a jour API"
git push origin main
```

Si Render est connecte a la branche `main`, le deploiement part automatiquement apres le push.

