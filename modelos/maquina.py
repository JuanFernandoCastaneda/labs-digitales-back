from sqlalchemy import Column, ForeignKey, Integer, String, or_
from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql.expression import nulls_last
from modelos.db import ModeloBase
from typing import Optional
from modelos.reserva import Reserva

class Maquina(ModeloBase):
    __tablename__ = "maquinas"
    id = Column(Integer, primary_key=True, index=True)
    departamento_id = Column(Integer, ForeignKey("departamentos.id"))
    departamento = relationship("Departamento")
    nombre = Column(String)
    materia = Column(String)
    descripcion = Column(String)
    foto = Column(String)
    reservas = relationship("Reserva")

    def __init__(maquina, id, departamento_id, nombre, materia, descripcion, foto):
        maquina.id = id
        maquina.departamento_id = departamento_id
        maquina.nombre = nombre
        maquina.materia = materia
        maquina.descripcion = descripcion
        maquina.foto = foto

    class Config:
        orm_mode = True

def obtener_por_pagina(db: Session, pagina: int, nombre: str, departamento: int, usuario_id: int):
    query = db.query(Maquina).outerjoin(Reserva).where(or_(Reserva.usuario_id == usuario_id, Reserva.usuario_id == None))\
        .order_by(nulls_last(Reserva.fecha.desc()))
    if departamento > 0:
        query = query.filter(Maquina.departamento_id == departamento)
    return query.filter(Maquina.nombre.contains(nombre)).limit(12).offset(pagina * 12).all()

def obtener_por_pagina_anonimo(db: Session, pagina: int, nombre: str, departamento: int):
    query = db.query(Maquina).filter(Maquina.nombre.contains(nombre))
    if departamento > 0:
        query = query.filter(Maquina.departamento_id == departamento)
    return query.order_by(Maquina.nombre.asc()).limit(12).offset(pagina * 12).all()

def obtener_total_paginas(db: Session, nombre: str, departamento: int):
    query = db.query(Maquina).filter(Maquina.nombre.contains(nombre))
    if departamento > 0:
        query = query.filter(Maquina.departamento_id == departamento)
    return (query.count() // 12) + 1

def obtener(db: Session, id: int) -> Optional[Maquina]:
    return db.query(Maquina).filter(Maquina.id == id).first()

def crear(db: Session, maquina: Maquina) -> Maquina:
    db.add(maquina)
    db.commit()
    db.refresh(maquina)
    return maquina
