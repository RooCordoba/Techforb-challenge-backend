from flask_restx import Resource, reqparse
from ...utils.extensions import api, ns_users
from ...utils.user_utils import user_exist, crear_user

# Hace que los endpoints tengan una interfaz mas amigable a la hora de rellenar campos
user_parser = reqparse.RequestParser()
user_parser.add_argument('nombre', type=str, required= True)
user_parser.add_argument('apellido', type=str, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('celular', type=int, required= False)

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
            
