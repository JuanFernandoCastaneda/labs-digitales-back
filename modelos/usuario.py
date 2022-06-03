from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship
from passlib.context import CryptContext
from modelos.db import ModeloBase

encriptador = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(ModeloBase):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    carrera_principal_id = Column(Integer, ForeignKey("departamentos.id"))
    carrera_principal = relationship("Departamento")
    nombre_de_usuario = Column(String, unique=True)
    nombre_completo = Column(String)
    contrasenia = Column(String)
    reservas = relationship("Reserva")

    def __init__(usuario, id, email, carrera_principal_id, nombre_de_usuario, nombre_completo, contrasenia):
        usuario.id = id
        usuario.email = email
        usuario.carrera_principal_id = carrera_principal_id
        usuario.nombre_de_usuario = nombre_de_usuario
        usuario.nombre_completo = nombre_completo
        usuario.contrasenia = contrasenia


def obtener_con_credenciales(db: Session, nombre_de_usuario: str, contrasenia: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.nombre_de_usuario == nombre_de_usuario and Usuario.contrasenia == encriptador.hash(contrasenia)).first()

def obtener(db: Session, id: int) -> Usuario:
    return db.query(Usuario).filter(Usuario.id == id).first()

def crear(db: Session, usuario: Usuario) -> Usuario:
    usuario.contrasenia = encriptador.hash(usuario.contrasenia)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario