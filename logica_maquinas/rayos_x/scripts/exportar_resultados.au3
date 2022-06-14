#include <Excel.au3>

Sleep(2000)
Send("!mx")
WinWaitActive("Exportar valores")
Send("{TAB}")
Send("{TAB}")
Send("{SPACE}")

Local $oExcel = _Excel_Open()
Local $oWorkbook = _Excel_BookNew($oExcel, 2)

WinWaitActive("Asistente para la activación de Microsoft Office", 5000)
WinClose("Asistente para la activación de Microsoft Office")

Sleep(2000)
Send("^v")

Send("!a")
Sleep(2500)
Send("v")
Sleep(2500)
Send("1")
WinWaitActive("Guardar como")
Send("{SPACE}")
Send("{LEFT}{SPACE}")