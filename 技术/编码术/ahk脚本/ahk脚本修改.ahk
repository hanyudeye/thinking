;弹出式 窗口，像Quake那种的
ToggleQuakeWindowQuake(identifier, type := "class") {
    ; 根据类型查找窗口
    if (type = "class"){
        if WinExist("ahk_class " identifier){
            windowID := WinGetID("ahk_class " identifier)
        }
    }
    else if (type = "exe"){
        if WinExist("ahk_exe " identifier){
            windowID := WinGetID("ahk_exe " identifier)
        }
    }
    else{
            windowID := WinGetID(identifier)
    }
      

    ; 如果窗口不存在，则退出函数
    
    if  !IsSet(windowID){
        Exit
    }

}

;发送热键
SendDownQuiet(hwnd) {
    if !WinExist("ahk_id " hwnd)
        return false

    ; 保存当前激活窗口
    prev := WinExist("A")

    ; 后台发送
    WinActivate("ahk_id " hwnd)
    ControlSend("{j}",, "ahk_id " hwnd)

    ; 切回原来窗口
    WinActivate("ahk_id " prev)
    return true
}

F8:: {
    hwnd := WinExist("Microsoft​ Edge")
 SendDownQuiet(hwnd)
}

