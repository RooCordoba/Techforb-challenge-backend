from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace


api = Api()
db = SQLAlchemy()

# me permite darle un nombre
ns_users = Namespace("users")
ns_tarjetas = Namespace("tarjetas")
ns_transacciones = Namespace("transacciones")
