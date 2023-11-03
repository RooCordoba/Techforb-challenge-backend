from src.utils.extensions import db

class User(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    dni = db.Column(db.Integer, unique= True,  nullable=False)
    celular = db.Column(db.Integer, nullable = True)
    is_logged_in = db.Column(db.Boolean)

    def __init__(self, nombre, apellido, password, dni, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.dni = dni
        self.celular = celular
        self.is_logged_in = False

class Tarjeta(db.Model):
    __tablename__ = 'tarjetas'

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('usuarios.dni'), nullable=False)
    cbu = db.Column(db.Integer, unique=True,  nullable=False)
    saldo = db.Column(db.Float, nullable= False)

    def __init__(self, user, cbu, saldo):
        self.user = user
        self.cbu = cbu
        self.saldo = saldo

class Transaccion(db.Model):
    __tablename__ = 'transacciones'

    id = db.Column(db.Integer, primary_key=True)
    tarjeta = db.Column(db.Integer, db.ForeignKey('tarjetas.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    cbu_destino = db.Column(db.Integer, nullable=False)

    def __init__(self, tarjeta, monto, cbu_destino):
        self.tarjeta = tarjeta
        self.monto = monto
        self.cbu_destino = cbu_destino
