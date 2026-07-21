# Wacdo API

API REST développée avec **FastAPI** pour la gestion d'un système de restauration rapide (type borne de commande).

Le projet permet de gérer les utilisateurs, les produits, les menus, les commandes ainsi que l'authentification par JWT avec gestion des rôles.

# Technologies utilisées

- Python 3.13+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT (JSON Web Token)
- Argon2 (hachage des mots de passe)
- Uvicorn

# 📁 Structure du projet

wacdo/
│
├── controllers/      # Logique métier
├── models/           # Modèles SQLAlchemy
├── routes/           # Routes API
├── schemas/          # Schémas Pydantic
├── utils/            # Fonctions utilitaires
├── alembic/          # Migrations de base de données
├── main.py           # Point d'entrée FastAPI
├── config.py         # Configuration du projet
├── requirements.txt
└── .env


# Installation

## 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/wacdo.git

cd wacdo
```
## 2. Créer un environnement virtuel

Windows

```bash
python -m venv .venv
```
Activation

```bash
.venv\Scripts\activate
```
Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```
## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Configuration

Créer un fichier `.env`.

Exemple :

```env
DATABASE_URL=postgresql+psycopg://utilisateur:motdepasse@localhost/wacdo

SECRET_KEY=votre_cle_secrete

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Adapter les valeurs selon votre environnement.

# Migration de la base de données

Créer les tables :

```bash
alembic upgrade head
```

Nouvelle migration :

```bash
alembic revision --autogenerate -m "description"
```

# Lancer le projet

```bash
uvicorn main:app --reload
```

L'application est disponible sur :

```
http://127.0.0.1:8000
```

# Documentation

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

#  Authentification

L'API utilise une authentification JWT.

Fonctionnalités :

- Connexion utilisateur
- Génération d'un token JWT
- Mot de passe sécurisé (Argon2)
- Gestion des rôles
- Protection des routes

Exemples de rôles :

- Administrateur
- Employé
- Accueil



# Fonctionnalités

- Authentification JWT
- Gestion des utilisateurs
- Gestion des produits
- Gestion des menus
- Gestion des commandes
- Gestion des rôles
- Validation des données avec Pydantic
- Documentation automatique Swagger

# Architecture

Le projet suit une architecture inspirée du modèle MVC.

- **Models** : structure de la base de données
- **Schemas** : validation des données
- **Controllers** : logique métier
- **Routes** : endpoints FastAPI

Cette organisation facilite la maintenance et l'évolution du projet.

# Sécurité

- Hachage des mots de passe avec Argon2
- Authentification JWT
- Variables sensibles stockées dans `.env`
- Validation des entrées avec Pydantic


# Dépendances principales

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- PyJWT
- Psycopg
- Uvicorn


# Objectifs du projet

Ce projet a été réalisé afin de :

- mettre en pratique FastAPI ;
- concevoir une API REST complète ;
- utiliser SQLAlchemy avec PostgreSQL ;
- gérer une authentification sécurisée par JWT ;
- appliquer une architecture claire et maintenable.

---

# Auteur

**Benjamin Pillard**

Projet réalisé dans le cadre de ma formation en développement web.

---

# 📄 Licence

Projet réalisé à des fins pédagogiques.
