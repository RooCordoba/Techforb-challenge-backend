import random
from src.db.database import Tarjeta, db
from src.utils.user_utils import get_user

#me genera un numero random para cbu

def get_card_by_id(id_card):
    card = db.session.query(Tarjeta).filter(Tarjeta.id == id_card).first()
    return card

def generar_cbu():
    return random.randint(00000000000000, 99999999999999)

def cbu_exist(cbu):
    if db.session.query(Tarjeta).filter(Tarjeta.cbu == cbu).first() is not None:
        return True
    return False

def crear_tarjeta_user(user):
    cbu = generar_cbu()
    while cbu_exist(cbu):
        cbu = generar_cbu()
    nueva_tarjeta = Tarjeta(user=user['dni'],
                         cbu=cbu,
                         saldo=0.0
                         )
    db.session.add(nueva_tarjeta)
    db.session.commit()


def get_all_cards_from_user(user):
    user_dni = get_user(user).dni
    all_cards = db.session.query(Tarjeta).filter(Tarjeta.user == user_dni).all()
    return all_cards


def tarjeta_existe(tarjetas_de_user, id_tarjeta):
    for tarjeta in tarjetas_de_user:
        if tarjeta.id == id_tarjeta:
            return True
    return False


def eliminar_tarjeta( id_tarjeta):
    db.session.query(Tarjeta)
    db.session.query(Tarjeta).filter(Tarjeta.id == id_tarjeta).delete()
    db.session.commit()

def get_card_by_cbu(cbu):
    tarjeta = db.session.query(Tarjeta).filter(Tarjeta.cbu == cbu).first()
    return tarjeta