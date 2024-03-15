from flask import Blueprint
import src.socio_logic as logic

from src.socio import db

routing = Blueprint('routes', __name__, template_folder='templates')

@routing.get('/socio/<id_socio>')
def consultar_socio(id_socio):
    response = logic.consultar_socio(id_socio)
    return response

@routing.post('/socio/<api_key>')
def crear_socio(api_key):
    response = logic.crear_socio_aleatorio(api_key=api_key)
    return response

@routing.get('/socio/registrosmedicos/<id_deportista>')
def consultar_registros_medicos_deportista(id_deportista):
    response = logic.consultar_registro_medico(id_deportista)
    return response