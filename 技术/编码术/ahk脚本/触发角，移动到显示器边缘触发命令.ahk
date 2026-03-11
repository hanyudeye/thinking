

#Persistent
SetTimer, CheckCorner, 50

cornerSize := 5
hoverTime := 500   ; 停留500ms才触发
startTime := 0
triggered := false

CheckCorner:
MouseGetPos, x, y

if (x <= cornerSize && y <= cornerSize)
{
    if (startTime = 0)
        startTime := A_TickCount

    if (!triggered && (A_TickCount - startTime > hoverTime))
    {
        triggered := true
        ;Run, notepad.exe
        ToggleQuakeWindowQuake("ChatGPT.exe","exe")
    }
}
else
{
    startTime := 0
    triggered := false
}

return