from flask_restx import Resource, reqparse
from src.utils.extensions import api, ns_users
from src.utils.user_utils import user_exist, cerrar_sesion

user_parser = reqparse.RequestParser()
user_parser.add_argument('dni', type=str, required= True)

@ns_users.route("/cerrar_sesion")
class CerarSesion(Resource):
    @api.expect(user_parser)
    def post(self):
        args = user_parser.parse_args()
        user={
            'dni': args['dni']
        }
        if user_exist(user):
            cerrar_sesion(user)
            return f'Sesion Finalizada con exito', 200
        else:
            return f'No se encontró el usuario', 404
        