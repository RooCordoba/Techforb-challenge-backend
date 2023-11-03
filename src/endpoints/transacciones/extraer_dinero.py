from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_transacciones
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.transacciones_utils import extraer
from src.utils.tarjeta_utils import get_all_cards_from_user, tarjeta_existe, get_card_by_id

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('monto_a_extraer', type=float, required=True)
user_parser.add_argument('tarjeta_id', type=int, required=True)

@ns_transacciones.route("/extraer_dinero")
class ExtraerDinero(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password'],
            'monto_a_extraer': args['monto_a_extraer'],
            'tarjeta_id' : args['tarjeta_id']
        }
        if not user_exist(user):
            return f'Usuario no existe', 405
        elif not coinciden_credenciales(user):
            return f'Contraseña Incorrecta', 405
        elif not tarjeta_existe(get_all_cards_from_user(user), user['tarjeta_id']):
            return f'Tarjeta no encontrada', 405
        elif get_card_by_id(user['tarjeta_id']).saldo < user['monto_a_extraer']:
            return f'No hay suficiente saldo en la tarjeta para realizar la extracción, tu saldo es: {get_card_by_id(user["tarjeta_id"]).saldo}', 405
        elif user['monto_a_extraer']<=0:
            return f'Para extraer dinero ingrese un numero positivo mayor a 0',405
        else:
            extraer(user['tarjeta_id'], user['monto_a_extraer'])
            return f'Dinero extraido con éxito, tu saldo en la tarjeta es de: {get_card_by_id(user["tarjeta_id"]).saldo} ', 200
