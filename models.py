from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    primerApellido = db.Column(db.String(50))
    segundoApellido = db.Column(db.String(50))
    edad = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)