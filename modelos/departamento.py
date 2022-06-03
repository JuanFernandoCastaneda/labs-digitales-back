from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship
from passlib.context import CryptContext
from modelos.db import ModeloBase

class Departamento(ModeloBase):
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

    def __init__(departamento, id, nombre):
        departamento.id = id
        departamento.nombre = nombre

def obtener(db: Session, id: int) -> Departamento:
    return db.query(Departamento).filter(Departamento.id == id).first()
    
def crear(db: Session, departamento: Departamento) -> Departamento:
    db.add(departamento)
    db.commit()
    db.refresh(departamento)
    return departamento