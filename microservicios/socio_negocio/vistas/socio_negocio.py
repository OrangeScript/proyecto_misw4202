from flask import jsonify
from flask_restful import Resource
from faker import Faker
import requests

class vistaSocioNegocio(Resource):

    ##Obtener deportista
    def get(self):
        
        deportista_response = requests.get('http://127.0.0.1:5000/obtener_deportista')

        return jsonify([deportista_response.status_code, deportista_response.text])

    ##Usar ID deportista
    def post(self):
        deportista = requests.get('http://127.0.0.1:5000/obtener_deportista')
        id_deportista = deportista.text[1:3]
        name_deportista = deportista.nombre
        concat = f"{id_deportista}{name_deportista}"

        print(id_deportista)

        
        enlace_response = requests.post(f'http://127.0.0.1:5002/obtener_enlace/{concat}')
        return jsonify([enlace_response])