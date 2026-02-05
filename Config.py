import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY =    "dev-secret-key" #On verra plus tard
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
