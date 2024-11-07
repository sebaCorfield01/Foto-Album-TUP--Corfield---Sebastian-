from flask import request, render_template, redirect, url_for, flash, Response, Blueprint
from typing import Union
from models import db, Photo

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for("main.ver_foto"))  

@main_bp.route("/add_photo", methods=["GET", "POST"])
def añadir_photo() -> Union[str, Response]:
    if request.method == "POST":
        titulo = request.form["titulo"]
        descripcion = request.form.get("descripcion", "")
        imagen = request.form["imagen"]

        new_foto = Photo(titulo=titulo, descripcion=descripcion, imagen=imagen)
        db.session.add(new_foto)
        db.session.commit()
        flash("Foto añadida")
        return redirect(url_for("main.ver_foto"))
    
    return render_template("photo_form.html")

@main_bp.route('/photos', methods=['GET'])
def ver_foto():
    fotos = Photo.query.all()
    return render_template("index.html", fotos=fotos)

@main_bp.route('/update_photo/<int:foto_id>', methods=['GET', 'POST'])
def subir_foto(foto_id: int) -> Union[str, Response]:
    foto = Photo.query.get_or_404(foto_id)
    if request.method == "POST":
        foto.titulo = request.form["titulo"]
        foto.descripcion = request.form.get("descripcion", "")
        foto.imagen = request.form["imagen"]

        db.session.commit()
        flash("Foto actualizada")
        return redirect(url_for("main.ver_foto"))
    
    return render_template("photo_form.html", foto=foto)

@main_bp.route('/delete_photo/<int:foto_id>', methods=['POST'])
def eliminar_foto(foto_id: int) -> Response:
    foto = Photo.query.get_or_404(foto_id)
    db.session.delete(foto)
    db.session.commit()
    flash("Foto eliminada")
    return redirect(url_for("main.ver_foto"))
