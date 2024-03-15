from dotenv import dotenv_values
import sys

from faker import Faker
from flask_jsonpify import jsonify
from datetime import datetime
from .logs_logica import escribir_log

from .deportista import Deportista, db

NOW = datetime.now()
COMPONENTE = 'deportista'

def crear_deportista_aleatorio(api_key=None):
    try:
        admin_api_key = dotenv_values('./admin_credentials.env')['API_KEY']
        if api_key != admin_api_key:
            escribir_log(COMPONENTE, NOW, f'Llave no autorizada{admin_api_key}')

            return {'message': 'API Key no reconocida'}, 403
        fake = Faker()
        nuevo_deportista = Deportista(
            nombre = fake.name(),
            edad = fake.random_int(min=15, max=90),
            peso = fake.random_int(min=30, max=150),
            estatura = fake.random_int(min=100, max=240),
            lesiones = fake.paragraph(nb_sentences=6),
            incapacidades = fake.paragraph(nb_sentences=8),
            alergias = fake.paragraph(nb_sentences=3)
        )
        db.session.add(nuevo_deportista)
        db.session.commit()
        escribir_log(COMPONENTE, NOW, f'Se creo nuevo deportista')
    except Exception as e:
        escribir_log(COMPONENTE, NOW, f'{e}')
        sys.exit(1)

    return {'message': f'Se ha creado un deportista nuevo'}, 200

def consultar_deportista(id_deportista):

    try:
        query = db.session.query(Deportista).filter(Deportista.id == id_deportista).first()
        query = query.__dict__
        del query['_sa_instance_state']
        escribir_log(COMPONENTE, NOW, 'Se consulto deportista')

    except Exception as e:
        escribir_log(COMPONENTE, NOW, f'{e}')
        sys.exit(1)

    return jsonify(query), 200