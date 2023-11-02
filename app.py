import os
from src.db.database import db
from flask import Flask
from src.utils.extensions import api
from src.endpoints.user import get_all_users, create_user, iniciar_sesion, cerrar_sesion, eliminar_user
from src.endpoints.tarjeta import pedir_tarjeta , ver_tarjetas_en_posesion, eliminar_tarjeta

def crear_app():
    return Flask(__name__)

# crea la app
app = crear_app()

# Define el destino de la Base de Datos
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'src/db/techforbDB.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.app_context().push()

api.init_app(app)
db.init_app(app)
db.create_all()

# Agrego los endpoints de los users
api.add_namespace(create_user.ns_users)
api.add_namespace(get_all_users.ns_users)
api.add_namespace(iniciar_sesion.ns_users)
api.add_namespace(cerrar_sesion.ns_users)
api.add_namespace(eliminar_user.ns_users)

# Agrego los endpint relacionados a Tarjetas
api.add_namespace(pedir_tarjeta.ns_tarjetas)
api.add_namespace(ver_tarjetas_en_posesion.ns_tarjetas)
api.add_namespace(eliminar_tarjeta.ns_tarjetas)


    