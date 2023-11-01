from ..utils.extensions import db

class User(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    dni = db.Column(db.String(20), unique= True,  nullable=False)
    celular = db.Column(db.String(20), nullable = True)

    def __init__(self, nombre, apellido, password, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.dni = dni

class Tarjeta(db.Model):
    __tablename__ = 'tarjetas'

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('usuarios.dni'), nullable=False)
    cbu = db.Column(db.Integer,  nullable=False)
    saldo = db.Column(db.Float, nullable= False)

    def __init__(self, user, saldo):
        self.user = user
        self.saldo = saldo

class Transaccion(db.Model):
    __tablename__ = 'transacciones'

    id = db.Column(db.Integer, primary_key=True)
    tarjeta = db.Column(db.Integer, db.ForeignKey('tarjetas.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)

    def __init__(self, tarjeta, monto):
        self.tarjeta = tarjeta
        self.monto = monto
