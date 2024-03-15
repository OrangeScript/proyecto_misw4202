from flask import Flask
from waitress import serve
import sys

from routes import routing
from src.socio import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///socio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()

app.register_blueprint(routing, name='socio')

db.init_app(app)
db.create_all()

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'dev':
        app.run(host='0.0.0.0', port=5001, debug=True)
    else:
        serve(app, host='0.0.0.0', port=5001, threads=4)

