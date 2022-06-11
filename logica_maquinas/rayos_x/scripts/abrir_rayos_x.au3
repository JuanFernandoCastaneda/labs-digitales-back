; La combinación de teclas alt + e + a permiten acceder a la pestaña de "Sensor" y luego elegir la máquina de "Aparato de rayos". 
; Una posible alternativa es hacer alt  + a de "Archivo" + n de "Nueva medida". Pero creo que es más preciso hacerlo a través de sensores.
Send("!mn")

; Esperamos a que la ventana donde se ingresan los parámetros aparezca. 
WinWaitActive("Aparato de rayo") ; INCOMPLETO, TOCA REVISAR CON AUTOIT WINDOWS INFO.