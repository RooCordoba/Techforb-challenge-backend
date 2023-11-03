from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_transacciones
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.transacciones_utils import depositar
from src.utils.tarjeta_utils import get_all_cards_from_user, tarjeta_existe, get_card_by_id

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('monto_a_depositar', type=float, required=True)
user_parser.add_argument('tarjeta_id', type=int, required=True)

@ns_transacciones.route("/depositar_dinero")
class DepositarDinero(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password'],
            'monto_a_depositar': args['monto_a_depositar'],
            'tarjeta_id' : args['tarjeta_id']
        }
        if not user_exist(user):
            return f'Usuario no existe', 405
        elif not coinciden_credenciales(user):
            return f'Contraseña Incorrecta', 405
        elif not tarjeta_existe(get_all_cards_from_user(user), user['tarjeta_id']):
            return f'Tarjeta no encontrada', 405
        elif user['monto_a_depositar']<=0:
            return f'Monto invalido, para depositar, tiene que ser un numero positivo mayor a 0', 405
        else:
            depositar(user['tarjeta_id'], user['monto_a_depositar'])
            return f'Dinero depositado con éxito, tu saldo en la tarjeta es de: {get_card_by_id(user["tarjeta_id"]).saldo} ', 200
