#Persistent
SetTimer, CheckWindow, 1000

Gui, +AlwaysOnTop -Caption +ToolWindow
Gui, Color, 000000
Gui, Font, s16 cFFFFFF Bold
Gui, Add, Text, vStatusText, Loading...
Gui, Show, x10 y10 NoActivate

return

CheckWindow:
WinGet, ProcessName, ProcessName, A

if (ProcessName = "Code.exe")
    status := "工作"
else if (ProcessName = "chrome.exe")
    status := "娱乐"
else if (ProcessName = "msedge.exe")
    status := "娱乐"
else
    status := "未知"

GuiControl,, StatusText, %status%
return