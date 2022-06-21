from fastapi import APIRouter, Depends, WebSocket
import logica_maquinas.rayos_x.rayos_x as logica
from pydantic import BaseModel
from datetime import datetime
from rutas.autenticacion import obtener_usuario_actual
import json

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

@enrutador.websocket("/rayos_x/")
async def computar(websocket: WebSocket):
    await websocket.accept()
    usuario = obtener_usuario_actual(await websocket.receive_text())
    if usuario is None:
        await websocket.send("401")
        await websocket.close()
    else:
        parametros = json.loads(await websocket.receive_json())
        await logica.abrir_programa()
        await logica.abrir_interfaz_maquina()
        await logica.ingresar_parametros(parametros.get("corriente"), parametros.get("tiempo"), parametros.get("tension_arranque"), 
            parametros.get("tension_parada", None), parametros.get("tension_incremento", None), 
            parametros.get("angulo_arranque"), parametros.get("angulo_parada", None), parametros.get("angulo_incremento", None))
        await logica.ejecutar_parametros()
        await logica.exportar_resultados()
        with open("Libro.xlsx", "rb") as f:
            archivo = f.readlines()
        await websocket.send_bytes(archivo)
        await websocket.close()
