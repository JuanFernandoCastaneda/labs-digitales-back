from fastapi import APIRouter, Depends
from pydantic import BaseModel

from rutas.autenticacion import obtener_usuario_actual

enrutador = APIRouter()

class Usuario(BaseModel):
    username: str
    departamento: int
    email: str
    full_name: str

@enrutador.get("/users/me/", response_model = Usuario)
def read_users_me(usuario_actual = Depends(obtener_usuario_actual)):
    return usuario_actual
