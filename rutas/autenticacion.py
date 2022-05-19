from fastapi import APIRouter , Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from pydantic import BaseModel
from modelos.usuario import obtener_usuario, obtener_usuario_con_credenciales, Usuario
from modelos.db import db

enrutador = APIRouter()

MINUTOS_DE_VALIDEZ_TOKEN = 1800
ALGORITHM = "HS256"
LLAVE_SECRETA = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

excepcion_de_credenciales = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

class Token(BaseModel):
    access_token: str
    token_type: str

async def obtener_usuario_actual(token: str = Depends(oauth2_scheme)) -> Usuario:
    try:
        payload = jwt.decode(token, LLAVE_SECRETA, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise excepcion_de_credenciales
    except JWTError:
        raise excepcion_de_credenciales
    usuario = obtener_usuario(db, id)
    if usuario is None:
        raise excepcion_de_credenciales
    if usuario.deshabilitado:
        raise HTTPException(status_code=400, detail="Inactive user")
    return usuario

def crear_token(contenido: dict) -> str:
    expiracion = datetime.utcnow() + timedelta(MINUTOS_DE_VALIDEZ_TOKEN)
    contenido.update({"exp": expiracion})
    return jwt.encode(contenido, LLAVE_SECRETA, algorithm=ALGORITHM)

@enrutador.post("/token", response_model=Token)
async def obtener_token(form: OAuth2PasswordRequestForm = Depends()) -> Token:
    usuario = obtener_usuario_con_credenciales(db, form.username, form.password)
    if not usuario:
        raise excepcion_de_credenciales
    return {"access_token": crear_token({"id": usuario.id}), "token_type": "bearer"}