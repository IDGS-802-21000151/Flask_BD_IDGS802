from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Alumnos
from flask import flash

import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/", methods=["GET", "POST"])
def cargarIndex():
    formRegistro = forms.UserForm(request.form)
    
    if request.method == "POST" and formRegistro.validate():
        alumno = Alumnos(nombre = formRegistro.nombre.data,
                        primerApellido = formRegistro.primerApellido.data,
                        email = formRegistro.email.data)
        
        #Insert into alumnos values()
        db.session.add(alumno)
        db.session.commit()
    
    return render_template("index.html", formRegistro = formRegistro)

@app.route("/alumnos", methods=["GET", "POST"])
def cargarAlumnos():
    alumnos = Alumnos.query.all()
        
    return render_template("ABC_Completo.html", alumnos = alumnos)

@app.route("/alumnos/edit/<int:idAlumno>", methods=["GET"])
def editarAlumno(idAlumno):
    alumno = Alumnos.query.get(idAlumno)
        
    return render_template("editarAlumno.html", alumno = alumno)

@app.route("/alumnos", methods=["DELETE"])
def eliminarAlumno():
    alumnos = Alumnos.query.all()
        
    return render_template("ABC_Completo.html", alumnos = alumnos)

# Método Main
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        
    app.run()