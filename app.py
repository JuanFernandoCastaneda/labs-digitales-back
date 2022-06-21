import asyncio
from fastapi import FastAPI
from uvicorn import Config, Server
from rutas import autenticacion, maquinas, usuarios, rayos_x
from modelos.db import db, ModeloBase, motor
from modelos import reserva, usuario, maquina, departamento
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

ModeloBase.metadata.create_all(bind=motor)

for index in range(4):
    departamento_temporal = departamento.obtener(db, index+1)
    if departamento_temporal is None:
        departamento.crear(db, departamento.Departamento(index+1, "Departamento " + str(index+1)))

usuario_base = usuario.obtener(db, 1)
if usuario_base is None:
    # Aquí en el tercer parámetro estoy poniendo que es del depto 1.
    usuario.crear(db, usuario.Usuario(1, "johndoe@example.com", 1, "johndoe", "John Doe", "secret"))

for index in range(13):
    maquina_temporal = maquina.obtener(db, index + 1)
    if maquina_temporal is None:
        # Estoy poniendo en el segundo parámetro que es el depto 2
        maquina.crear(db, maquina.Maquina(index + 1, 2, "Pendulo", "Física I", "Pendulo para Física I", "https://shop.mohd.it/media/catalog/product/cache/0c1904db32fb51666a8fdb1a39640e3e/p/e/pendulum-suspension-by-cto-lighting.jpg"))

maquina_13 = maquina.obtener(db, 14)
if maquina_13 is None:
    # Parte del depto 1
    maquina.crear(db, maquina.Maquina(14, 1, "Rayos x", "Física intermedia", "Máquina de rayos x para Física I", "https://5.imimg.com/data5/SELLER/Default/2021/3/JE/TN/MW/4917623/digital-x-ray-imaging-machine-500x500.png"))
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
app.include_router(rayos_x.enrutador)

loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)

configuracion = Config(app=app, loop=loop)
server = Server(configuracion)
loop.run_until_complete(server.serve())
