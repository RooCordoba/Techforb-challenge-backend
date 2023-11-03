from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_transacciones
from src.utils.user_utils import user_exist, coinciden_credenciales
from src.utils.transacciones_utils import hacer_transaccion
from src.utils.tarjeta_utils import get_all_cards_from_user, tarjeta_existe, get_card_by_id
from src.utils.tarjeta_utils import get_card_by_cbu

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=int, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('monto_a_transferir', type=float, required=True)
user_parser.add_argument('tarjeta_id', type=int, required=True)
user_parser.add_argument('cbu_destino', type=int, required=True)

@ns_transacciones.route("/transferir_dinero")
class TransferirDinero(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni'],
            'password': args['password'],
            'monto_a_transferir': args['monto_a_transferir'],
            'tarjeta_id' : args['tarjeta_id'],
            'cbu_destino': args['cbu_destino']
        }
        if not user_exist(user):
            return f'Usuario no existe', 405
        elif not coinciden_credenciales(user):
            return f'Contraseña Incorrecta', 405
        elif not tarjeta_existe(get_all_cards_from_user(user), user['tarjeta_id']):
            return f'Tarjeta no encontrada', 405
        elif get_card_by_id(user['tarjeta_id']).saldo < user['monto_a_transferir']:
            return f'No hay suficiente saldo en la tarjeta para realizar la transferencia, tu saldo es de {get_card_by_id(user["tarjeta_id"]).saldo}', 405
        elif get_card_by_cbu(user['cbu_destino']) is None:
            return f'El CBU no pertenece a ninguna tarjeta existente', 405
        elif user['monto_a_transferir']<=0:
            return f'Para transferir dinero ingrese un numero positivo mayor a 0',405
        else:
            hacer_transaccion(user)
            return "Transaccion completada con exito", 200