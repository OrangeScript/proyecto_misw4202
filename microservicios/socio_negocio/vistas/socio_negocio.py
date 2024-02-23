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

        print(id_deportista)

        
        pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id_deportista}/')

        pokemon_test = pokemon_response.text

        return jsonify([pokemon_test])