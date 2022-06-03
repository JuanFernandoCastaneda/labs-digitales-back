from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from modelos.maquina import obtener, obtener_por_pagina, obtener_por_pagina_anonimo, obtener_total_paginas
from modelos.db import db

from rutas.autenticacion import obtener_usuario_actual

enrutador = APIRouter()

class Busqueda(BaseModel):
    nombre: str
    departamento: int
    pagina: int

class Maquina(BaseModel):
    id: int
    departamento_id: int
    nombre: str
    materia: str
    descripcion: str
    foto: str
    fecha: Optional[datetime]

    class Config:
        orm_mode = True

class RespuestaBusqueda(BaseModel):
    maquinas: List[Maquina]
    total: int

@enrutador.post("/maquinas", response_model = RespuestaBusqueda)
def obtener_maquinas_por_pagina(busqueda: Busqueda, usuario = Depends(obtener_usuario_actual)):
    maquinas = obtener_por_pagina(db, busqueda.pagina, busqueda.nombre, busqueda.departamento, usuario.id)
    for maquina in maquinas:
        if maquina.reservas:
            maquina.fecha = maquina.reservas[0].fecha
    total = obtener_total_paginas(db, busqueda.nombre, busqueda.departamento)
    return RespuestaBusqueda(maquinas=maquinas, total=total)

@enrutador.post("/maquinas/anonimo", response_model = RespuestaBusqueda)
def obtener_maquinas_por_pagina_anonimo(busqueda: Busqueda):
    maquinas = obtener_por_pagina_anonimo(db, busqueda.pagina, busqueda.nombre, busqueda.departamento)
    total = obtener_total_paginas(db, busqueda.nombre, busqueda.departamento)
    return RespuestaBusqueda(maquinas=maquinas, total=total)

@enrutador.get("/maquinas/{id}")
def obtener_maquina(id: int):
    return obtener(db, id)
