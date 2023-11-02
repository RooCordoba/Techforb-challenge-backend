from flask_restx import fields
from ..utils.extensions import api

user_model = api.model("User",{
    "id": fields.Integer,
    "nombre": fields.String,
    "apellido": fields.String,
    "password": fields.String,
    "dni": fields.String,
    "celular": fields.String,
    "is_logged_in": fields.Boolean
})

tarjeta_model = api.model("Tarjeta", {
    "id": fields.Integer,
    "user": fields.Integer,
    "cbu": fields.Integer,
    "saldo": fields.Float
})

transaccion_model = api.model("Transaccion",{
    "id": fields.Integer,
    "tarjeta": fields.Integer,
    "monto": fields.Float
})


