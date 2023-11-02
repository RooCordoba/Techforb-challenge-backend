from flask_restx import Resource
from ...db.models import user_model
from ...db.database import User
from ...utils.extensions import api, ns_users


# Obtiene una JSON con todos los usarios en la base de datos
@ns_users.route("/get_all_users")
class AllUsers(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return User.query.all()