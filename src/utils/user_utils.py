from flask_restx import reqparse
from ..db.database import db, User

# Hace que los endpoints tengan una interfaz mas amigable a la hora de rellenar campos
user_parser = reqparse.RequestParser()
user_parser.add_argument('nombre', type=str, required= True)
user_parser.add_argument('apellido', type=str, required= True)
user_parser.add_argument('password', type=str, required= True)
user_parser.add_argument('dni', type=str, required= True)
user_parser.add_argument('celular', type=str, required= False)


# Crea un usuario y lo registra en la base de datos
def crear_user(usuario):
    nuevo_usuario = User(nombre=usuario['nombre'],
                         apellido=usuario['apellido'],
                         password=usuario['password'],
                         dni=usuario['dni'],
                         celular=usuario['celular']
                         )
    db.session.add(nuevo_usuario)
    db.session.commit()

# Me da True si el usuario existe, y False si no, lo busca por el DNI
def user_exist(usuario):
    dni = usuario['dni']
    if db.session.query(User).filter(User.dni == dni).first() is None:
        return False
    return True
