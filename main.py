from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from flask import flash

import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/")
def cargarIndex():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def cargarAlumnos():
    alumno_form = forms.UserForm(request.form)
    
    if request.method == "POST" and alumno_form.validate():
        nombre = alumno_form.nombre.data
        primerApellido = alumno_form.primerApellido
        segundoApellido = alumno_form.segundoApellido
        
        mensaje = f"Bienvenido: {nombre}"
        
        flash(mensaje)
        
    return render_template("alumnos.html", form = alumno_form)

# Método Main
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()