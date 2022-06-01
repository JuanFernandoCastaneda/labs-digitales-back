from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from modelos.maquina import obtener, obtener_por_pagina, obtener_por_pagina_anonimo
from modelos.db import db

from rutas.autenticacion import obtener_usuario_actual

enrutador = APIRouter()

class Busqueda(BaseModel):
    nombre: str
    departamento: str
    pagina: int

class Maquina(BaseModel):
    id: int
    departamento: str
    nombre: str
    materia: str
    descripcion: str
    foto: str
    fecha: Optional[datetime]

    class Config:
        orm_mode = True

@enrutador.post("/maquinas", response_model = List[Maquina])
def obtener_maquinas_por_pagina(busqueda: Busqueda, usuario = Depends(obtener_usuario_actual)):
    maquinas = obtener_por_pagina(db, busqueda.pagina, busqueda.nombre, busqueda.departamento, usuario.id)
    for maquina in maquinas:
        if maquina.reservas:
            maquina.fecha = maquina.reservas[0].fecha
    return maquinas

@enrutador.post("/maquinas/anonimo", response_model = List[Maquina])
def obtener_maquinas_por_pagina_anonimo(busqueda: Busqueda):
    return obtener_por_pagina_anonimo(db, busqueda.pagina, busqueda.nombre, busqueda.departamento)

@enrutador.get("/maquinas/{id}")
def obtener_maquina(id: int):
    return obtener(db, id)
