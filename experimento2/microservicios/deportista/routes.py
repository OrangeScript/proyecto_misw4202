from flask import Blueprint
import src.deportista_logic as logic

from src.deportista import db

routing = Blueprint('routes', __name__, template_folder='templates')

@routing.get('/deportista/registrosmedicos/<id_deportista>')
def consultar_perfil_deportivo_deportista(id_deportista):
    response = logic.consultar_deportista(id_deportista)
    return response

@routing.post('/deportista/<api_key>')
def crear_deportista(api_key):
    response = logic.crear_deportista_aleatorio(api_key=api_key)
    return response