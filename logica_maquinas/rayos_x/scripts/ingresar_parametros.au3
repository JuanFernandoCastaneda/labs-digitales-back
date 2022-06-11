; Tipo de medida. Se puede no enviar nada, o enviar 1 a 3 {RIGHT}. Como generalmente se trabaja "Espectros", no vamos a enviar nada.
Send("{TAB}")

; Datos en X. Se puede enviar nada o un {DOWN}. Generalmente se usa �ngulo de cristal, entonces no vamos a enviar nada.
; Send("{DOWN}")
Send("{TAB}")

; Corriente de emis. Se ingresa un double como par�metro. Creo que los valores van de 0.1 a 1 mA.
; CORRIENTE
Send("{TAB}")

; Tiempo de integraci�n. Se ingresa un integer como par�metro.
; TIEMPO
Send("{TAB}")

; Tensi�n. Se puede elegir constante o variable, lo cual var�a con un {UP} o nada. Si se pone un {UP} de variable, hay que ingresar 3 par�metros que son:
; tensi�n m�nima, tensi�n m�xima e incremento de tensi�n. Toca verificar que el incremento sea congruente con el resto.

; TENSION

; Opci�n 1 tensi�n (constante):
; Send(10)

; Opci�n 2 tensi�n (variable):
; Send("{DOWN}")
; Send("{TAB}")
; Send(5)
; Send("{TAB}")
; Send(35)
; Send("{TAB}")
; Send(3)

; Modo rotaci�n. Siempre es el mismo as� que solo se da tab. Se mueve con {UP} y {DOWN}.
Send("{TAB}")

; �ngulo de arranque. En grados.
; ANGULO_ARRANQUE
Send("{TAB}")

; �ngulo de parada. En grados.
; ANGULO_PARADA
Send("{TAB}")

; Incremento. En grados.
; ANGULO_INCREMENTO
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
Send("{TAB}")

; Opci�n de continuar, terminamos :D. Supongo yo que es con enter que funciona.
Send("{SPACE}")