from flask import jsonify
from flask_restful import Resource
from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

db = SQLAlchemy()

class Deportista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)

def data_mock_deportistas():

    data_factory = Faker()

    data_deportista = []
    deportistas = []

    for i in range(0, 10):
        data_deportista.append((
            data_factory.pyint(),  # id
            data_factory.street_name(),  # nombre
        ))

        deportistas.append(
            Deportista(
                id=data_deportista[-1][0],
                nombre=data_deportista[-1][1]
            )
        )

    return deportistas


class VistaDeportista(Resource):

    def get(self):
        deportistas = data_mock_deportistas()
        posicion_deportista = random.randint(0, 9)
        
        deportista = deportistas[posicion_deportista]
        
        lst_deportista = [
            deportista.id,
            deportista.nombre
        ]


        return jsonify(lst_deportista)
