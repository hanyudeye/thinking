hello,world

ToggleQuakeWindow(identifier, type = "class")
{
    ; 根据类型查找窗口
    if (type = "class")
        WinGet, windowID, ID, ahk_class %identifier%
    else if (type = "exe")
        WinGet, windowID, ID, ahk_exe %identifier%
    else
        WinGet, windowID, ID, %identifier%

    ; 如果窗口存在，就激活
    if (windowID)
    {
	  WinGet, windowState, MinMax, ahk_id %windowID%
        if (windowState)
	{
            WinRestore ahk_id %windowID%
            WinWait,%windowT%
            WinActivate
	}   else
            WinMinimize ahk_id %windowID%
      } 
}
