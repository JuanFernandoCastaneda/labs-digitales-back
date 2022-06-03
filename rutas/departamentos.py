from pydantic import BaseModel

class Departamento(BaseModel):
    id: int
    nombre: str

