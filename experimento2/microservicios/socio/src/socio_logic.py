from dotenv import dotenv_values
import sys

from faker import Faker
from flask_jsonpify import jsonify
from requests import get
from datetime import datetime
from .logs_logica import escribir_log

from .socio import Socio, db

NOW = datetime.now()
COMPONENTE = 'socio-negocio'

def crear_socio_aleatorio(api_key=None):
    try:
        admin_api_key = dotenv_values('./admin_credentials.env')['API_KEY']
        if api_key != admin_api_key:
            escribir_log(COMPONENTE, NOW, f'Llave no autorizada {admin_api_key}')
            
            return {'message': 'API Key no reconocida'}, 403
        
        fake = Faker()
        nuevo_socio = Socio(
            nombre = fake.name(),
        )
        db.session.add(nuevo_socio)
        db.session.commit()
        escribir_log(COMPONENTE, NOW, f'Se creo nuevo socio de negocio')
    except Exception as e:
        escribir_log(COMPONENTE, NOW, f'{e}')
        sys.exit(1)

    return {'message': f'Se ha creado un socio nuevo'}, 200

def consultar_socio(id_socio):

    try: 
        query = db.session.query(Socio).filter(Socio.id == id_socio).first()
        query = query.__dict__
        del query['_sa_instance_state']
        escribir_log(COMPONENTE, NOW, 'Se consulto socio de negocio')

    except Exception as e:
        escribir_log(COMPONENTE, NOW, f'{e}')
        sys.exit(1)

    return jsonify(query), 200

def consultar_registro_medico(id_deportista):

    try:
        response = get(f'http://localhost:5000/deportista/registrosmedicos/{id_deportista}').json()
        escribir_log(COMPONENTE, NOW, 'Se consulto registro medico')

    except Exception as e:
        escribir_log(COMPONENTE, NOW, f'{e}')
        sys.exit(1)

    return response, 200