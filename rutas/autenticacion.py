from fastapi import APIRouter , Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from pydantic import BaseModel
from modelos.usuario import obtener, obtener_con_credenciales, Usuario
from modelos.db import db

enrutador = APIRouter()

MINUTOS_DE_VALIDEZ_TOKEN = 1800
ALGORITHM = "HS256"
LLAVE_SECRETA = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

oauth2_esquema = OAuth2PasswordBearer(tokenUrl="token")

excepcion_de_credenciales = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo hacer la validación de credenciales.",
        headers={"WWW-Authenticate": "Bearer"},
    )

class Credenciales(BaseModel):
    nombre_de_usuario: str
    contrasenia: str

class Token(BaseModel):
    token: str
    tipo: str

def obtener_usuario_actual(token: str = Depends(oauth2_esquema)) -> Usuario:
    try:
        payload = jwt.decode(token, LLAVE_SECRETA, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise excepcion_de_credenciales
    except JWTError:
        raise excepcion_de_credenciales
    usuario = obtener(db, id)
    if usuario is None:
        raise excepcion_de_credenciales
    return usuario

def crear_token(contenido: dict) -> str:
    expiracion = datetime.utcnow() + timedelta(MINUTOS_DE_VALIDEZ_TOKEN)
    contenido.update({"exp": expiracion})
    return jwt.encode(contenido, LLAVE_SECRETA, ALGORITHM)

@enrutador.post("/token", response_model=Token)
def obtener_token(credenciales: Credenciales) -> Token:
    usuario = obtener_con_credenciales(db, credenciales.nombre_de_usuario, credenciales.contrasenia)
    if not usuario:
        raise excepcion_de_credenciales
    return {"token": crear_token({"id": usuario.id}), "tipo": "bearer"}