from src.db.database import db, Tarjeta, Transaccion

def depositar(tarjeta_id, monto):
    tarjeta = db.session.query(Tarjeta).filter(Tarjeta.id ==tarjeta_id).first()
    tarjeta.saldo += monto
    nueva_transaccion = Transaccion(tarjeta=tarjeta_id,
                         monto=monto,
                         cbu_destino=tarjeta.cbu
                         )
    db.session.add(nueva_transaccion)
    db.session.commit()



def extraer(tarjeta_id, monto):
    tarjeta = db.session.query(Tarjeta).filter(Tarjeta.id ==tarjeta_id).first()
    tarjeta.saldo -= monto
    nueva_transaccion = Transaccion(tarjeta=tarjeta_id,
                         monto= -monto,
                         cbu_destino=tarjeta.cbu
                         )
    db.session.add(nueva_transaccion)
    db.session.commit()

def hacer_transaccion(user):
    monto = user['monto_a_depositar']

    tarjeta = db.session.query(Tarjeta).filter(Tarjeta.id == user['tarjeta_id']).first()
    tarjeta.saldo -= monto

    tarjeta_destino = db.session.query(Tarjeta).filter(Tarjeta.cbu== user['cbu_destino']).first()
    tarjeta_destino.saldo += monto

    nueva_transaccion_tarjeta = Transaccion(tarjeta=tarjeta.id,
                                    monto=-monto,
                                    cbu_destino=tarjeta_destino.cbu)
    nueva_transaccion_tarjeta_destino = Transaccion(tarjeta=tarjeta_destino.id,
                                             monto=+monto,
                                             cbu_destino=tarjeta.cbu)
    db.session.add(nueva_transaccion_tarjeta)
    db.session.add(nueva_transaccion_tarjeta_destino)
    db.session.commit()


def ver_todas_transacciones(tarjeta_id):
    transacciones =  db.session.query(Transaccion).filter(Transaccion.tarjeta == tarjeta_id).all()
    return transacciones