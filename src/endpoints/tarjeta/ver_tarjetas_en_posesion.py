from flask_restx import Resource, reqparse
from ...utils.extensions import api, ns_tarjetas
from ...utils.user_utils import user_exist, coinciden_credenciales
from ...utils.tarjeta_utils import get_all_cards_from_user
from ...db.models import tarjeta_model


user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)

@ns_tarjetas.route("/ver_tarjetas_user")
class VerTarjetasPosesion(Resource):
    @api.expect(user_parser)
    @api.marshal_list_with(tarjeta_model)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password']
        }
        if user_exist(user):
            if coinciden_credenciales(user):
                return get_all_cards_from_user(user), 200
            else:
                return f'Contraseña Incorrecta', 405
        else:
            return f'Usuario no existe', 405