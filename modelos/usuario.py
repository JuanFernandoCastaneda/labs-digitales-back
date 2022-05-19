from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from modelos.db import ModeloBase


encriptador = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(ModeloBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=True)
    username = Column(String, unique=True)
    nombre_completo = Column(String, nullable=True)
    deshabilitado = Column(Boolean, nullable=True)
    contrasenia = Column(String)
    # items

    def __init__(usuario, id, email, username, nombre_completo, deshabilitado, contrasenia):
        usuario.id = id
        usuario.email = email
        usuario.username = username
        usuario.nombre_completo = nombre_completo
        usuario.deshabilitado = deshabilitado
        usuario.contrasenia = contrasenia


def obtener_usuario_con_credenciales(db: Session, username: str, contrasenia: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.username == username and Usuario.contrasenia == encriptador.hash(contrasenia)).first()

def obtener_usuario(db: Session, id: int) -> Usuario:
    return db.query(Usuario).filter(Usuario.id == id).first()

def crear_usuario(db: Session, usuario: Usuario) -> Usuario:
    usuario.contrasenia = encriptador.hash(usuario.contrasenia)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario