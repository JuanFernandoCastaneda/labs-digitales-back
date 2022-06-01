
from fastapi import FastAPI
from rutas import autenticacion, maquinas, usuarios
from modelos.db import db, ModeloBase, motor
from modelos import reserva, usuario, maquina
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

ModeloBase.metadata.create_all(bind=motor)

usuario_base = usuario.obtener(db, 1)
if usuario_base is None:
    usuario.crear(db, usuario.Usuario(1, "johndoe@example.com", "johndoe", "John Doe", "secret"))

for index in range(12):
    maquina_temporal = maquina.obtener(db, index + 1)
    if maquina_temporal is None:
        maquina.crear(db, maquina.Maquina(index + 1, "fisica", "Pendulo", "Física I", "Pendulo para Física I", "https://shop.mohd.it/media/catalog/product/cache/0c1904db32fb51666a8fdb1a39640e3e/p/e/pendulum-suspension-by-cto-lighting.jpg"))

maquina_13 = maquina.obtener(db, 13)
if maquina_13 is None:
    maquina.crear(db, maquina.Maquina(13, "quimica", "Rayos x", "Química I", "Máquina de rayos x para Química I", "https://5.imimg.com/data5/SELLER/Default/2021/3/JE/TN/MW/4917623/digital-x-ray-imaging-machine-500x500.png"))
    reserva_1 = reserva.obtener(db, 1)
    if reserva_1 is None:
        reserva.crear(db, reserva.Reserva(1, 1, 13, datetime.today()))

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
app.include_router(maquinas.enrutador)
app.include_router(usuarios.enrutador)
