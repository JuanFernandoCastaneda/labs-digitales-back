from fastapi import APIRouter, Depends
import logica_maquinas.rayos_x.rayos_x as logica
from pydantic import BaseModel
from datetime import datetime
from rutas.autenticacion import obtener_usuario_actual

class Computo(BaseModel):
    corriente: float
    tiempo: int
    tension_arranque: int
    angulo_arranque: int
    tension_parada: int = None
    tension_incremento: int = None
    angulo_parada: int = None
    angulo_incremento: float = None

# class Respuesta(BaseModel):

enrutador = APIRouter()

@enrutador.post("/rayos_x/")
async def computar(parametros: Computo, usuario = Depends(obtener_usuario_actual)):
    logica.abrir_programa()
    logica.abrir_interfaz_maquina()
    logica.ingresar_parametros(parametros.corriente, parametros.tiempo, parametros.tension_arranque, 
        parametros.tension_parada, parametros.tension_incremento, parametros.angulo_arranque, 
        parametros.angulo_parada, parametros.angulo_incremento)
    logica.ejecutar_parametros()
    # logica.cerrar_programa()