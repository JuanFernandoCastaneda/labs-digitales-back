; Abrir el programa.
Run("C:\Program Files (x86)\PHYWE\measure\MEASURE.EXE")

; Esperar a que la ventana del programa aparezca y esté activa.
WinWaitActive("Phywe measure 4")

; Esperar a que la ventana de novedades aparezca. Puede trabar todo si no existe.
WinWaitActive("Novedades")

; Cerrar la ventana de novedades.
WinClose("Novedades")