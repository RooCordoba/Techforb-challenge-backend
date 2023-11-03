from flask_restx import Resource, reqparse, abort
from src.utils.extensions import api, ns_tarjetas
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.tarjeta_utils import get_all_cards_from_user
from src.db.models import tarjeta_model


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
        if not user_exist(user):
            abort(405,  message="Usuario no Existe")
        elif not coinciden_credenciales(user):
            abort(405,  message="Contraseña Inconrrecta")
        else:
            return get_all_cards_from_user(user), 200