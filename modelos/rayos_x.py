from sqlalchemy import Boolean, Column, Float, Integer
from modelos.db import ModeloBase

class Rayos_X(ModeloBase):
    __tablename__ = "rayos_x"
    id = Column(Integer, primary_key=True, index=True)
    # Corriente
    corriente_constante = Column(Boolean)
    corriente_minima = Column(Integer)
    corriente_maxima = Column(Integer, nullable=True)
    incremento_corriente = Column(Integer, nullable=True)
    # Tensión
    tension_constante = Column(Boolean)
    tension_minima = Column(Integer)
    tension_maxima = Column(Integer, nullable=True)
    incremento_tension = Column(Integer, nullable=True)
    # Tiempo integración
    tiempo_integracion = Column(Integer)
    # Ángulo
    angulo_inicio = Column(Integer)
    angulo_parada = Column(Integer)
    incremento_angulo = Column(Float)

    # También tengo como que saber el usuario.
