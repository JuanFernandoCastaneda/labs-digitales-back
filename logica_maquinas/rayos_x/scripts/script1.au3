#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.16.0
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here

Run("notepad.exe")

WinWaitActive("Untitled - Notepad")

Send("Oof, papá, gg ez")

WinClose("*Untitled - Notepad")

WinWaitActive("Notepad")

Send("{RIGHT}{ENTER}")