from ..db.database import db, User

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


def get_user(user):
    dni = user['dni']
    user_db = db.session.query(User).filter(User.dni == dni).first()
    return user_db


def coinciden_credenciales(user):
    user_db = get_user(user)
    if user['password'] == user_db.password:
        return True
    return False

def iniciar_sesion(user):
    user_db = get_user(user)
    user_db.is_logged_in = True
    db.session.commit()

def cerrar_sesion(user):
    user_db = get_user(user)
    user_db.is_logged_in = False
    db.session.commit()

def eliminar_usuario(user):
    user_db = get_user(user)
    db.session.delete(user_db)
    db.session.commit()