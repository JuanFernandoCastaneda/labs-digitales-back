; La combinaci�n de teclas alt + e + a permiten acceder a la pesta�a de "Sensor" y luego elegir la m�quina de "Aparato de rayos". 
; Una posible alternativa es hacer alt  + a de "Archivo" + n de "Nueva medida". Pero creo que es m�s preciso hacerlo a trav�s de sensores.
Send("!mn")

; Esperamos a que la ventana donde se ingresan los par�metros aparezca. 
WinWaitActive("Aparato de rayo") ; INCOMPLETO, TOCA REVISAR CON AUTOIT WINDOWS INFO.