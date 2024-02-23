from flask import Flask
from flask_restful import Api
from vistas.deportista import VistaDeportista

app = None

def create_flask_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admon_reservas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    # CORS(app)

    # jwt = JWTManager(app)

    # @jwt.user_lookup_loader
    # def user_lookup_callback(_jwt_header, jwt_data):
    #     identity = jwt_data["sub"]
    #     return Usuario.query.filter_by(id=identity).one_or_none()

    return app

def add_urls(app):
    api = Api(app)
    api.add_resource(VistaDeportista, '/obtener_deportista')


if __name__ == '__main__':
    
    app = create_flask_app()
    app.run()