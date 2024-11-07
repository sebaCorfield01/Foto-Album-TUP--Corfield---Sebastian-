
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_por_defecto'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fotos.db'  # URI de la base de datos SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
