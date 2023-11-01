from flask_restx import Resource, Namespace, Api, Resource
from .db.models import user_model
from .db.database import User
from .utils.extensions import api, ns_users, ns_tarjetas, ns_transacciones
from flask import request, jsonify

@ns_users.route("/Hello")
class Hello(Resource):
    def get(self):
        return {"hello": "world"}
    
@ns_users.route("/get_all_users")
class AllUsers(Resource):
    @ns_users.marshal_list_with(user_model)
    def get(self):
        return User.query.all()
    
"""
@api.route('/crear_usuario', methods=['POST'])
class CrearUsario(Resource):
    def post(nombre, dni):
        if request.method == 'POST':
            data = request.json  # Se espera que los datos se envíen en formato JSON

            # Verificar si se proporcionó un nombre de usuario
            if 'username' in data:
                nuevo_usuario = User(username=data['username'])
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify({"message": "Usuario creado exitosamente"}), 201
            else:
                return jsonify({"error": "Falta el campo 'username' en los datos enviados"}), 400
"""