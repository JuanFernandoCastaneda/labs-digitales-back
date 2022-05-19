from fastapi import APIRouter

enrutador = APIRouter()

@enrutador.post("/maquinas/rayos-x/computar")
def computar_rayos_x():
    return {"info": "info"}