from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Session
from modelos.db import ModeloBase

class Reserva(ModeloBase):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    maquina_id = Column(Integer, ForeignKey("maquinas.id"))
    fecha = Column(DateTime)

    def __init__(maquina, id, usuario_id, maquina_id, fecha):
        maquina.id = id
        maquina.usuario_id = usuario_id
        maquina.maquina_id = maquina_id
        maquina.fecha = fecha

def crear(db: Session, reserva: Reserva) -> Reserva:
    db.add(reserva)
    db.commit()
    db.refresh(reserva)
    return reserva

def obtener(db: Session, id: int) -> Reserva:
    return db.query(Reserva).filter(Reserva.id == id).first()
