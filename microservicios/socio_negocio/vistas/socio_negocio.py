from flask import jsonify
from flask_restful import Resource
import requests
from retrying import retry

class vistaSocioNegocio(Resource):

    ##Obtener deportista
    @retry
    def get(self):
        
        deportista_response = requests.get('http://127.0.0.1:5000/obtener_deportista')

        return jsonify([deportista_response.status_code, deportista_response.text])

    ##Usar ID deportista
    @retry
    def post(self):
        deportista = requests.get('http://127.0.0.1:5000/obtener_deportista').json()
        id_deportista = deportista[0]
        name_deportista = deportista[1].replace(' ', '')
        concat = f"{id_deportista}{name_deportista}"
        enlace_response = requests.post(f'http://127.0.0.1:5002/obtener_enlace/{concat}').json()
        return enlace_response