from flask_restx import Resource, reqparse
from ...utils.extensions import api, ns_users
from ...utils.user_utils import user_exist, coinciden_credenciales, iniciar_sesion

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=str, required= True)
user_parser.add_argument('password', type=str, required= True)

@ns_users.route("/iniciar_sesion")
class IniciarSesion(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password']
        }
        if user_exist(user):
            if coinciden_credenciales(user):
                iniciar_sesion(user)
                return f'Inicio de Sesion correcto', 200
            else:
                return f'Contraseña Incorrecta', 405
        else:
            return f'Usuario con DNI no existe', 405
        
            