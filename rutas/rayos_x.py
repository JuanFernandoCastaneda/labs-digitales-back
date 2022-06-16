from fastapi import APIRouter, Depends, WebSocket
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

@enrutador.websocket("/rayos_x/")
async def computar(websocket: WebSocket):
    await websocket.accept()
    usuario = obtener_usuario_actual(await websocket.receive_text())
    if usuario is None:
        await websocket.send("401")
        await websocket.close()
    else:
        parametros = await websocket.receive_json()
        # logica.abrir_programa()
        # logica.abrir_interfaz_maquina()
        # logica.ingresar_parametros(parametros.corriente, parametros.tiempo, parametros.tension_arranque, 
        #     parametros.tension_parada, parametros.tension_incremento, parametros.angulo_arranque, 
        #     parametros.angulo_parada, parametros.angulo_incremento)
        # logica.ejecutar_parametros()
        # logica.exportar_resultados()
        await websocket.send_bytes(bin(173))
        await websocket.close()
    
# Esto no debería ejecutarse sino hasta el final
@enrutador.get("/rayos_x/")
async def enviar_resultado():
    with open("Libro.xlxs", "rb") as f:
        archivo = f.readlines()
    return archivo
