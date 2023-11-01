import os
from src.db.database import db
from flask import Flask
from src.utils.extensions import api
from src.endpoints import ns_users, ns_tarjetas, ns_transacciones

# crea la app
app = Flask(__name__)

# Define el destino de la Base de Datos
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src/db/techforbDB.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.app_context().push()

api.init_app(app)
db.init_app(app)
db.create_all()

api.add_namespace(ns_users)
api.add_namespace(ns_tarjetas)
api.add_namespace(ns_transacciones)

    