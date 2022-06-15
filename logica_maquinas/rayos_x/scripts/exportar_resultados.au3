#include <Excel.au3>

Send("!mx")
WinWaitActive("Exportar valores")
Send("{ENTER}")

Local $oExcel = _Excel_Open()
Local $oWorkbook = _Excel_BookNew($oExcel, 1)

; Por la razón que quieras esto recibe por parámetro segundos y no milisegundos.
WinWaitActive("Asistente para la activación de Microsoft Office", "", 5)
WinClose("Asistente para la activación de Microsoft Office")

Sleep(2000)
Send("^v")

Send("!a")
Sleep(2500)
Send("v")
Sleep(2500)
Send("ç")
WinWaitActive("Guardar como")
Send("+{TAB}")
Send("+{TAB}")
Send("{DOWN}{UP}")
Send("{ENTER}")
Sleep(2500)
Send("{TAB}{TAB}")
Send("Libro")
Send("{ENTER}")
Send("{LEFT}{ENTER}")
Sleep(2500)
WinClose("Libro - Excel")
Sleep(2500)
WinClose("Phywe measure 4")
Send("{LEFT}{ENTER}")