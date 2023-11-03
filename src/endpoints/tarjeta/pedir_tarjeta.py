from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_tarjetas
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.tarjeta_utils import crear_tarjeta_user

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)

@ns_tarjetas.route("/pedir_tarjeta")
class PedirTarjeta(Resource):
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
            crear_tarjeta_user(user)
            return f'Tarjeta Creada con exito', 201