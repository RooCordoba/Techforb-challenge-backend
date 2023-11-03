from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_users
from src.utils.user_utils import user_exist, coinciden_credenciales, eliminar_usuario

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=str, required= True)
user_parser.add_argument('password', type=str, required= True)

@ns_users.route("/eliminar_user")
class EliminarUser(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password']
        }
        if not user_exist(user):
            return f'Usuario no existe', 405
        elif not coinciden_credenciales(user):
            return f'Contraseña Incorrecta', 405
        else:
            eliminar_usuario(user)
            return f'Usuario eliminado corectamente', 200
