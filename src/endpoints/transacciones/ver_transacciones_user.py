from flask_restx import Resource, reqparse, abort
from src.utils.extensions import api, ns_transacciones
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.transacciones_utils import ver_todas_transacciones
from src.utils.tarjeta_utils import get_all_cards_from_user, tarjeta_existe
from src.db.models import transaccion_model


user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('tarjeta_id', type=int, required=True)

@ns_transacciones.route("/ver_transacciones_tarjeta")
class Ver_Transacciones_Tajeta(Resource):
    @api.expect(user_parser)
    @api.marshal_list_with(transaccion_model)
    def get(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password'],
            'tarjeta_id' : args['tarjeta_id']
        }
        if not user_exist(user):
            abort(405, message="Usuario no existe")
        elif not coinciden_credenciales(user):
            abort(405, message="Contraseña Incorrecta")
        elif not tarjeta_existe(get_all_cards_from_user(user), user['tarjeta_id']):
            abort(405, message="Tarjeta no encontrada")
        else:
            transacciones = ver_todas_transacciones(user['tarjeta_id'])
            return transacciones, 200