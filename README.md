# FastAPI Item API

Une API REST construite avec **FastAPI** pour gérer une collection d’items (nom, prix, disponibilité), avec tests automatisés, CI/CD et déploiement sur Render.

---

##  Fonctionnalités

- CRUD complet (Create, Read, Update, Delete) pour les items
- Documentation Swagger intégrée (`/docs`)
- Tests automatisés avec `pytest`
- Analyse de code avec `flake8`
- Analyse de sécurité avec `bandit`
- Intégration continue via GitHub Actions

---

##  Stack utilisée

- **FastAPI** – framework web léger et rapide
- **SQLAlchemy** – ORM pour interagir avec la base de données MySQL
- **Pytest** – framework de tests
- **Flake8** – outil de linting
- **Bandit** – outil d’analyse de sécurité Python
- **GitHub Actions** – CI/CD
- **Render** – hébergement cloud

---

## Installation locale

1. **Cloner le projet**

    git clone https://github.com/claire-estelle16/Devops_Claire.git

    cd votre-repo

2.  **Créer un environnement virtuel**

    python -m venv venv

    source venv/bin/activate  ou `venv\Scripts\activate`

3.  **Installer les dépendances**

    pip install -r requirements.txt

4.  **Lancer l'application**

    uvicorn main:app --reload

---

## Variables d’environnement

À définir dans un fichier .env ou directement dans Render/GitHub :

    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=db_devops
    DB_USER=root
    DB_PASSWORD=root

---

## Endpoints de l'API

Méthode	Route	Description

    GET	/items	Liste tous les items
    GET	/items/{id}	 Affiche un item spécifique
    POST /items	  Crée un nouvel item
    PUT	/items/{id}	  Met à jour un item
    DELETE	/items/{id}	  Supprime un item

    Accès à Swagger UI : http://localhost:8000/docs

---

## Tests et qualité de code

**Tests unitaires** :

    pytest

**Linting (PEP8)** :

    flake8 .

**Analyse de sécurité** :

bandit -r .

---

## CI/CD GitHub Actions

**Le fichier .github/workflows/ci.yml** :

    Vérifie le code avec flake8 et bandit

    Lance les tests avec pytest

    Si tout est OK, déploie automatiquement sur Render


