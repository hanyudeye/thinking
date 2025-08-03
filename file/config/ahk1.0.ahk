; 使用箭头键移动鼠标
#Up::MouseMove, 0, -10, 0, R
#Down::MouseMove, 0, 10, 0, R
#Left::MouseMove, -10, 0, 0, R
#Right::MouseMove, 10, 0, 0, R
#^k::MouseMove, 0, -10, 0, R
#^j::MouseMove, 0, 10, 0, R
#^h::MouseMove, -10, 0, 0, R
#^;::MouseMove, 10, 0, 0, R

; #Z 键左键点击，#X 键右键点击
#z::
#u::Click
#x::Click right

; 使用 3 个键控制，^; 作为前缀键
^;::
Input, key1, L1 T1
if (key1 = "a") {
        Run, notepad.exe
}
return


; 把 CapsLock 定义为 Ctrl 键
CapsLock::Ctrl


!j:: Send {Down}
!k:: Send {Up}
!h:: Send {Left}
!l:: Send {Right}

; Alt + D 定义为 delete 键
!d::  
Send, {Delete}  ; 模拟按下 Delete 键
return

;切换虚拟桌面
;#^;::Send #^{Right}
;#^j::Send #^{Left}

Active(t){
;     IfWinActive,%t%
;   {
;     WinMinimize
;     return
;   }

;    IfWinExist,%t%
;   {
;     WinShow
;     WinActivate           
;     return 1
;   }
 WinActivate,ahk_exe %t%
 return
}

Match(){
SetTitleMatchMode, 2
; 使用正则表达式匹配窗口标题并激活
RegexPattern := "WinActivate.*"
 
; 检查是否存在匹配窗口标题的窗口
;ahk_class Chrome_WidgetWin_1 ahk_exe msedge.exe 
if WinExist( RegexPattern)
{
    ; 如果存在，则激活窗口
    WinActivate
MsgBox hello
}

return
 }


;弹出式切换窗口
ToggleQuakeWindow(identifier, type = "class")
{
    ; 根据类型查找窗口
    if (type = "class")
        WinGet, windowID, ID, ahk_class %identifier%
    else if (type = "exe")
        WinGet, windowID, ID, ahk_exe %identifier%
    else
        WinGet, windowID, ID, %identifier%

   ; 如果窗口存在，则隐藏/显示
    if (windowID)
    {

        WinGet, windowState, MinMax, ahk_id %windowID%
        if (windowState) ;如果最小化
	{
            WinRestore ahk_id %windowID%
            WinWaitActive ahk_id %windowID%, , 2
            WinActivate ahk_id %windowID%
	}
        else ; 否则最小化
        {
            WinMinimize ahk_id %windowID%
}
    }
 else
    {
        MsgBox, 未找到窗口: %identifier%
    }
}

;切换窗口2,这种如果窗口存在，就激活，不再最小化窗口了
ToggleQuakeWindow(identifier, type = "class")
{
    ; 根据类型查找窗口
    if (type = "class")
        WinGet, windowID, ID, ahk_class %identifier%
    else if (type = "exe")
        WinGet, windowID, ID, ahk_exe %identifier%
    else
        WinGet, windowID, ID, %identifier%
    ; 如果窗口存在，则激活
    if (windowID)
    {
        	  WinGet, windowState, MinMax, ahk_id %windowID%
        if (windowState)
	{
            WinRestore ahk_id %windowID%
            WinWait,ahk_id %windowID%
            WinActivate ahk_id %windowID%
	}   else{
             WinActivate ahk_id %windowID%
      } 
}
}


;弹出式 窗口，像Quake那种的
ToggleQuakeWindowQuake(identifier, type = "class")
{
    ; 根据类型查找窗口
    if (type = "class")
        WinGet, windowID, ID, ahk_class %identifier%
    else if (type = "exe")
        WinGet, windowID, ID, ahk_exe %identifier%
    else
        WinGet, windowID, ID, %identifier%
    ; 如果窗口存在，则激活
    if (windowID)
    {
        	  WinGet, windowState, MinMax, ahk_id %windowID%

        if (windowState) ;如果窗口隐藏，则激活
	{
            WinRestore ahk_id %windowID%
            WinWait,ahk_id %windowID%
            WinActivate ahk_id %windowID%
	}  else {

            WinWait,ahk_id %windowID%
            WinMinimize ahk_id %windowID%
    } 
}
}




;激活资源管理器
#e::ToggleQuakeWindowT("ahk_class CabinetWClass")
;#e::Active("Explorer.EXE")
;#a::WinActivate, EasyChat
;#w::Active("msedge.exe")
#a::
#w::ToggleQuakeWindowT("ahk_exe msedge.exe")

f1::ToggleQuakeWindowT("ahk_exe Code.exe")
#c::ToggleQuakeWindowT("ahk_exe Cursor.exe")
#i::ToggleQuakeWindowT("ahk_exe WindowsTerminal.exe")
#o::ToggleQuakeWindowT("ahk_exe okular.exe")
#s::ToggleQuakeWindowT("ahk_exe chrome.exe")
;#s::Active("chrome.exe")
#y::Active("copytranslator.exe")
;#a::ToggleQuakeWindowT("ahk_exe Postman.exe")
#x::WinActivate,Telegram

;激活Code Shijian
#+s::
WinTitle=ahk_class Chrome_WidgetWin_1
main:
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"Shijian")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return


;激活Code Lilun
#+l::
WinTitle=ahk_class Chrome_WidgetWin_1
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"blog")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return
