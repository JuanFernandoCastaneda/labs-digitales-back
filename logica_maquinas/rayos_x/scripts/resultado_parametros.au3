; Tipo de medida. Se puede no enviar nada, o enviar 1 a 3 {RIGHT}. Como generalmente se trabaja "Espectros", no vamos a enviar nada.
Send("{TAB}")

; Datos en X. Se puede enviar nada o un {DOWN}. Generalmente se usa �ngulo de cristal, entonces no vamos a enviar nada.
Send("{TAB}")

; Corriente de emis. Se ingresa un double como par�metro. Creo que los valores van de 0.1 a 1 mA.
Send(1)
Send("{TAB}")

; Tiempo de integraci�n. Se ingresa un integer como par�metro.
Send(2)
Send("{TAB}")

; Tensi�n. Se puede elegir constante o variable, lo cual var�a con un {UP} o nada. Si se pone un {UP} de variable, hay que ingresar 3 par�metros que son:
; tensi�n m�nima, tensi�n m�xima e incremento de tensi�n. Toca verificar que el incremento sea congruente con el resto.

Send("{UP}")
Send("{TAB}")
Send("30")
Send("{TAB}{TAB}")
Send("0.5")
Send("+{TAB}")
Send("35")
Send("{TAB}")
Send("1")

; Opci�n 1 tensi�n (constante):
; Send("{TAB}")
; Send(10)

; Opci�n 2 tensi�n (variable):
; Send("{UP}")
; Send("{TAB}")
; Send(5)
; Send("{TAB}")
; Send(35)
; Send("{TAB}")
; Send(3)

Send("{TAB}")

; Modo rotaci�n. Siempre es el mismo as� que solo se da tab. Se mueve con {UP} y {DOWN}.
Send("{TAB}")

; Hecho para que ángulo de arranque y de parada no se puteen.
Send("{TAB}")
Send("{TAB}")
Send("0.1")
Send("+{TAB}")
Send("+{TAB}")

; �ngulo de arranque. En grados.
Send(5)
Send("{TAB}")

; �ngulo de parada. En grados.
Send(55)
Send("{TAB}")

; Incremento. En grados.
Send(10)
Send("{TAB}")

; Cristal siempre es LIF. Es un men� desplegable que hay que ver c�mo se modifica.
Send("{TAB}")

; Nunca se pone absorbedor.
Send("{TAB}")

; Nunca se pone filtro.
Send("{TAB}")

; Opciones para modificar los tres par�metros anteriores. No tocar xd.
Send("{TAB}")

; Opciones de "Indicar". Parece que nunca se tocan. Se navergar�a entre ellas con {UP}. Supongo que se activan con enter.
Send("{UP}")
Send("{TAB}")

; Opci�n de continuar, terminamos :D. Supongo yo que es con enter que funciona.
Send("{ENTER}")

; Iniciar medida.
WinWaitActive("Aparato de rayos X - Registro", "Iniciar medida")

Sleep(7000)
Send("{TAB}")
Send("{ENTER}")

; Tiempo que se debe esperar para que se ejecute la operación. Básicamente es el tiempo que dura en cada ángulo.
; Multiplicado por la cantidad de veces que va a cambiar, sumado a por ahí 20 segundos de configuración.
Sleep(20000)
Sleep(186000.0)

; CLICS_TENSION_CONSTANTE
