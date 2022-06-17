; Abrir el programa.
Run("C:\Program Files (x86)\PHYWE\measure\MEASURE.EXE")

; Esperar a que la ventana del programa aparezca y est� activa.
WinWaitActive("Phywe measure 4", "", 5)
Sleep(1000)
Send("!{TAB}")
Sleep(1000)
Send("!{TAB}")
Sleep(1000)
