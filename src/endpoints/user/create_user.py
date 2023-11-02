from flask_restx import Resource
from ...utils.extensions import api, ns_users
from ...utils.user_utils import *

# Endpoint para crear usuario  
@ns_users.route("/crear_usuario")
class CrearUsuario(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        nuevo_user={
            'nombre': args['nombre'],
            'apellido': args['apellido'],
            'password': args['password'],
            'dni': args['dni'],
            'celular': args['celular']
        }
        if user_exist(nuevo_user):
            return f'Usuario con ese dni ya registrado', 405
        else:
            crear_user(nuevo_user)
            return f' Nuevo usuario creado: {nuevo_user.get("nombre")}', 201
            
