import os
from pydoc import doc
import subprocess
from typing import Optional

RUTA_SCRIPTS = "logica_maquinas/rayos_x/scripts/"
RUTA_ABRIR_PROGRAMA = "abrir_programa.au3"
RUTA_ABRIR_RAYOS_X = "abrir_rayos_x.au3"
RUTA_INGRESAR_PARAMETROS = "ingresar_parametros.au3"
RUTA_RESULTADO_PARAMETROS = "resultado_parametros.au3"
RUTA_EXPORTAR_RESULTADOS = "exportar_resultados.au3"
RUTA_SCRIPT1 = "script1.au3"

tension_variable = False

# Función para correr los diferentes scripts y saber si terminaron de manera exitosa.
def correr_script(script) -> bool:
    p1 = subprocess.run(["Autoit3", RUTA_SCRIPTS + script])
    return p1.returncode == 0

def abrir_programa():
    correr_script(RUTA_ABRIR_PROGRAMA)

def abrir_interfaz_maquina():
    correr_script(RUTA_ABRIR_RAYOS_X)

# Siempre elegir tensión variable para que el resto funcione.
def ingresar_parametros(corriente: float, tiempo: int, tension_arranque: int, 
                        tension_parada: Optional[int], tension_incremento: Optional[int], 
                        angulo_arranque: int, angulo_parada: Optional[int], 
                        angulo_incremento: Optional[float]):
    global tension_variable

    with open(RUTA_SCRIPTS + RUTA_INGRESAR_PARAMETROS, "r") as f:
        archivo = f.readlines()

    espera = (tiempo + 1.5)*1000

    archivo[archivo.index('; CORRIENTE\n')] = "Send({})\n".format(corriente)
    archivo[archivo.index('; TIEMPO\n')] = "Send({})\n".format(tiempo)

    archivo[archivo.index('; ANGULO_ARRANQUE\n')] = "Send({})\n".format(angulo_arranque)
    if angulo_parada != None and angulo_incremento != None:
        archivo[archivo.index('; ANGULO_PARADA\n')] = "Send({})\n".format(angulo_parada)
        archivo[archivo.index('; ANGULO_INCREMENTO\n')] = "Send({})\n".format(angulo_incremento)
        if angulo_incremento != 0:
            espera *= ((angulo_parada-angulo_arranque)/angulo_incremento + 1)
    
    tension = ""
    if tension_variable:
        tension += 'Send("{UP}")\n'
        tension_variable = False
    if tension_parada != None and tension_incremento != None:
        tension += ('Send("{UP}")\n'\
            + 'Send("{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_arranque)\
            + 'Send("{TAB}{TAB}")\n'\
            + 'Send("{}")\n'.format(0.5)\
            + 'Send("+{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_parada))\
            + 'Send("{TAB}")\n'\
            + 'Send("{}")\n'.format(tension_incremento)
        tension_variable = True
        espera += 10000 # Como 10 segundos dura en volver al puesto, pues
        if tension_incremento != 0:
            espera *= ((tension_parada-tension_arranque)/tension_incremento + 1)
    else:
        tension += ('Send("{TAB}")\n'\
            + "Send({})\n".format(tension_arranque))
        archivo[archivo.index('; CLICS_TENSION_CONSTANTE\n')] = 'Send("{TAB}")\n'\
            + 'Send("{TAB}")\n'\
            + 'Send("{TAB}")\n'\
            + 'Send("{TAB}")\n'\
            + 'Send("{SPACE}")\n'
    archivo[archivo.index('; TENSION\n')] = tension

    archivo[archivo.index('; ESPERA\n')] = "Sleep({})\n".format(str(espera))
    
    with open(RUTA_SCRIPTS + RUTA_RESULTADO_PARAMETROS, "w") as f:
        f.write("".join(archivo))

def ejecutar_parametros():
    correr_script(RUTA_RESULTADO_PARAMETROS)

def exportar_resultados():
    correr_script(RUTA_EXPORTAR_RESULTADOS)

#abrir_programa()
#abrir_interfaz_maquina()
#ingresar_parametros(1, 3, 15, 35, 10, 5, 15, 10)
#ejecutar_parametros()
#exportar_resultados()

# p1.returncode == 0 es que fue exitoso. p1.stderr es para imprimir error.
# check=True hace que Python también bote excepción.     