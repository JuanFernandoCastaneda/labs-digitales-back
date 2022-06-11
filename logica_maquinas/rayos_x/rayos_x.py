import os
from pydoc import doc
import subprocess
from typing import Optional

RUTA_SCRIPTS = "logica_maquinas/rayos_x/scripts/"
RUTA_ABRIR_PROGRAMA = "abrir_aparato_rayos_x.au3"
RUTA_ABRIR_RAYOS_X = "abrir_rayos_x.au3"
RUTA_INGRESAR_PARAMETROS = "ingresar_parametros.au3"
RUTA_RESULTADO_PARAMETROS = "resultado_parametros.au3"
RUTA_SCRIPT1 = "script1.au3"

# Función para correr los diferentes scripts y saber si terminaron de manera exitosa.
def correr_script(script) -> bool:
    p1 = subprocess.run(["Autoit3", RUTA_SCRIPTS + script], capture_output=False)
    return p1.returncode == 0

def abrir_programa():
    correr_script(RUTA_ABRIR_PROGRAMA)

def abrir_interfaz_maquina():
    correr_script(RUTA_ABRIR_RAYOS_X)

def ingresar_parametros(corriente: float, tiempo: int, tension_arranque: int, 
                        tension_parada: Optional[int], tension_incremento: Optional[int], 
                        angulo_arranque: int, angulo_parada: Optional[int], 
                        angulo_incremento: Optional[float]):
    with open(RUTA_SCRIPTS + RUTA_INGRESAR_PARAMETROS, "r") as f:
        archivo = f.readlines()
    
    archivo[archivo.index('; CORRIENTE\n')] = "Send({})\n".format(corriente)
    archivo[archivo.index('; TIEMPO\n')] = "Send({})\n".format(tiempo)
    if tension_parada != None and tension_incremento != None:
        archivo[archivo.index('; TENSION\n')] = 'Send("{DOWN}")\n'\
            + 'Send("{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_arranque)\
            + 'Send("{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_parada)\
            + 'Send("{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_incremento)
    else:
        archivo[archivo.index('; TENSION\n')] = "Send({})\n".format(tension_arranque)
    archivo[archivo.index('; ANGULO_ARRANQUE\n')] = "Send({})\n".format(angulo_arranque)
    if angulo_parada != None and angulo_incremento != None:
        archivo[archivo.index('; ANGULO_PARADA\n')] = "Send({})\n".format(angulo_parada)
        archivo[archivo.index('; ANGULO_INCREMENTO\n')] = "Send({})\n".format(angulo_incremento)
    
    with open(RUTA_SCRIPTS + RUTA_RESULTADO_PARAMETROS, "w") as f:
        f.write("".join(archivo))

def ejecutar_parametros():
    correr_script(RUTA_RESULTADO_PARAMETROS)

# ingresar_parametros(1.0, 2, 3, 4, 5, 6, 7, 8.0)

# p1.returncode == 0 es que fue exitoso. p1.stderr es para imprimir error.
# check=True hace que Python también bote excepción.