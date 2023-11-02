from flask_restx import Resource, reqparse
from ...utils.extensions import api, ns_tarjetas
from ...utils.user_utils import user_exist, coinciden_credenciales
from ...utils.tarjeta_utils import eliminar_tarjeta, get_all_cards_from_user, tarjeta_existe

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('id_tarjeta_a_eliminar', type=int, required= True)

@ns_tarjetas.route("/eliminar_tarjeta")
class EliminarTarjeta(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password'],
            'id_tarjeta_a_eliminar' : args['id_tarjeta_a_eliminar']
        }
        if user_exist(user):
            if coinciden_credenciales(user):
                if tarjeta_existe(get_all_cards_from_user(user),user['id_tarjeta_a_eliminar']):
                    eliminar_tarjeta(user['id_tarjeta_a_eliminar'])
                    return f'Tarjeta Eliminada con Exito', 200
                else:
                    return f'Id de Tarjeta Invalida', 405
            else:
                return f'Contraseña Incorrecta', 405
        else:
            return f'Usuario no existe', 405