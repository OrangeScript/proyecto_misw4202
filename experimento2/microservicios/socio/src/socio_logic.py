from dotenv import dotenv_values
from faker import Faker
from flask_jsonpify import jsonify
from requests import get

from .socio import Socio, db

def crear_socio_aleatorio(api_key=None):
    admin_api_key = dotenv_values('./admin_credentials.env')['API_KEY']
    if api_key != admin_api_key:
        return {'message': 'API Key no reconocida'}, 403
    fake = Faker()
    nuevo_socio = Socio(
        nombre = fake.name(),
    )
    db.session.add(nuevo_socio)
    db.session.commit()
    return {'message': f'Se ha creado un socio nuevo'}, 200

def consultar_socio(id_socio):
    query = db.session.query(Socio).filter(Socio.id == id_socio).first()
    query = query.__dict__
    del query['_sa_instance_state']
    print(query)
    return jsonify(query)

def consultar_registro_medico(id_deportista):
    response = get(f'http://localhost:5000/deportista/registrosmedicos/{id_deportista}').json()
    return response