
from fastapi import FastAPI
from rutas import autenticacion, rayos_x, usuarios
from modelos.db import db, ModeloBase, motor
from modelos.usuario import Usuario, obtener_usuario, crear_usuario
from fastapi.middleware.cors import CORSMiddleware


ModeloBase.metadata.create_all(bind=motor)

usuario_base = obtener_usuario(db, 1)
if usuario_base is None:
    crear_usuario(db, Usuario(1, "johndoe@example.com", "johndoe", "John Doe", False, "secret"))

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autenticacion.enrutador)
app.include_router(rayos_x.enrutador)
app.include_router(usuarios.enrutador)
