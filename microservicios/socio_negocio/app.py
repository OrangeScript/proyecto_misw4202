from flask import Flask
from flask_restful import Api
from vistas.socio_negocio import vistaSocioNegocio

app = None

def create_flask_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///socioNegocio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app_context = app.app_context()
    app_context.push()
    add_urls(app)

    return app

def add_urls(app):
    api = Api(app)
    api.add_resource(vistaSocioNegocio, '/obtener_deportista')


if __name__ == '__main__':
    
    app = create_flask_app()
    app.run(host="127.0.0.1", port="5001", debug=True)