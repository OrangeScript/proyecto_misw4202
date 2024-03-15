from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Socio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128), nullable=False)