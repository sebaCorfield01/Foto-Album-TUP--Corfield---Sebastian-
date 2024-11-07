from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  
class Photo(db.Model):
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(250), nullable=False)

    def __init__(self, titulo: str, descripcion: str, imagen: str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.imagen = imagen
