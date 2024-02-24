from flask import Flask
from flask_restful import Api
from vistas.socio_negocio import vistaSocioNegocio
from waitress import serve

app = None

def create_flask_app():
    app = Flask(__name__)
    app_context = app.app_context()
    app_context.push()
    add_urls(app)

    return app

def add_urls(app):
    api = Api(app)
    api.add_resource(vistaSocioNegocio, '/obtener_deportista')


if __name__ == '__main__':    
    app = create_flask_app()
    serve(app=app, host='127.0.0.1', port=5001, threads=4, connection_limit=200)