from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Deportista(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    estatura = db.Column(db.Float, nullable=False)
    lesiones = db.Column(db.String, nullable=True)
    incapacidades = db.Column(db.String, nullable=True)
    alergias = db.Column(db.String, nullable=True)