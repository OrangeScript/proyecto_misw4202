from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Socio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    pais = db.Column(db.String(128), nullable=False)
    ciudad = db.Column(db.String(128), nullable=False)
    timezone = db.Column(db.String(128), nullable=False)
    ip = db.Column(db.String(128), nullable=False)


class eventos_app(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_componente = db.Column(db.String(128), nullable=False)
    fecha_log = db.Column(db.DateTime, nullable=False)
    mensaje_log = db.Column(db.String(250), nullable=False)
