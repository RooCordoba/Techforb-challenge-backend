from flask_restx import Resource
from src.db.models import user_model
from src.db.database import User
from src.utils.extensions import api, ns_users


# Obtiene una JSON con todos los usarios en la base de datos
@ns_users.route("/get_all_users")
class AllUsers(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return User.query.all(), 200