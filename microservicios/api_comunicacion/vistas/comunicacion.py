from flask import jsonify
from flask_restful import Resource

class VistaComunicacion(Resource):
    def post(self, concat):
        enlace = f'http://{concat}.uniandes.edu.co'
        return jsonify(enlace)
