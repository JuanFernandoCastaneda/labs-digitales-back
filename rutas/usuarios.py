from fastapi import APIRouter, Depends
from typing import Optional
from rutas.autenticacion import obtener_usuario_actual
from pydantic import BaseModel

enrutador = APIRouter()

class Usuario(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

@enrutador.get("/users/me/", response_model=Usuario)
async def read_users_me(usuario_actual = Depends(obtener_usuario_actual)):
    return usuario_actual

@enrutador.get("/users/me/items/")
async def read_own_items(current_user = Depends(obtener_usuario_actual)):
    return []