# 💱 Currency Converter Web App

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![GitHub Repo Size](https://img.shields.io/github/repo-size/chouanbou-eliel-ops/PythonProjectCurrency)
![Last Commit](https://img.shields.io/github/last-commit/chouanbou-eliel-ops/PythonProjectCurrency)

---

## 📖 Description

Currency Converter Web App est une application web développée avec **Flask** permettant aux utilisateurs de convertir des devises en temps réel, de sauvegarder automatiquement leurs conversions et de consulter leur historique personnel via un système d’authentification sécurisé.

Le projet adopte une **architecture modulaire** inspirée des bonnes pratiques professionnelles afin de garantir maintenabilité, évolutivité et clarté du code.

---

## 🚀 Fonctionnalités

- Création de compte utilisateur  
- Connexion / Déconnexion  
- Conversion de devises en temps réel (yfinance)  
- Sauvegarde automatique des conversions  
- Historique personnel par utilisateur  
- Suppression d’une conversion  
- Suppression complète de l’historique  
- Accès administrateur protégé  
- Tableau de bord administrateur  

---

## 🛠 Technologies

- Python 3  
- Flask  
- Flask-SQLAlchemy  
- Flask-Login  
- Flask-Migrate  
- SQLite  
- yfinance  
- HTML / CSS / JavaScript  

---

## 📂 Structure du projet


## 📁 Structure du projet

PythonProjectCurrency/

├── run.py  
├── Config.py   
├── requirements.txt    
├── app/    
│ ├── init.py   
│ ├── extensions.py     
│ ├── models/   
│ ├── routes/   
│ ├── services/     
│ ├── templates/        
│ └── static/       

---

## ⚙ Installation

### 1. Cloner le projet

git clone https://github.com/chouanbou-eliel-ops/PythonProjectCurrency.git

### 2. Créer un environnement virtuel

python -m venv venv

**Activer**
**Windows** :venv\Scripts\activate

**Linux/Mac** :source venv/bin/activate


---

### 3. Installer les dépendances

pip install -r requirements_project2.txt

---

### 4. Initialiser la base de données

- flask db init
- flask db migrate
- flask db upgrade

---

### 5. Lancer l'application

python run.py

Puis ouvrir dans le navigateur :

http://127.0.0.1:5000

---

## 👤 Créer un compte administrateur

Après avoir créé un utilisateur :

flask shell

```python
from app.extensions import db
from app.models.user import User

user = User.query.filter_by(email="admin@test.com").first()
user.is_admin = True
db.session.commit()
```

🔐 Sécurité

- Mots de passe hashés

- Routes protégées par authentification

- Vérification des rôles (admin / user)

📌 Améliorations futures

- Export CSV de l’historique

- Graphiques statistiques

- API publique

- Version Desktop

- Version Mobile


## 👨‍💻 Auteur

Eliel Weme

Étudiant & développeur Python

