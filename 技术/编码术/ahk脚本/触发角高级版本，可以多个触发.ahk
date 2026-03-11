; 正式开始
; AutoHotkey v2: #NoEnv removed, scripts are persistent by default
; #Persistent removed
;SetBatchLines -1    ; command-style to avoid Warn about unused global
CoordMode("Mouse", "Screen")

; ===== 配置区 =====

checkInterval := 50
cornerSize := 8
edgeSize := 3
hoverTime := 400
cooldown := 1000

; 触发区开关
zones := {}

zones["TopLeft"] := {enabled:1}
zones["TopRight"] := {enabled:1}
zones["BottomLeft"] := {enabled:1}
zones["BottomRight"] := {enabled:1}
zones["TopEdge"] := {enabled:0}
zones["BottomEdge"] := {enabled:0}
zones["LeftEdge"] := {enabled:0}
zones["RightEdge"] := {enabled:0}

; ===== 状态区 =====

zoneState := {}

for k,v in zones
{
    zoneState[k] := {
        hoverStart:0,
        lastTrigger:0,
        triggered:false
    }
}

SetTimer("WatchHotCorners", checkInterval)
return ; keep for structure though not strictly needed

; ===== 主检测 =====

WatchHotCorners:

MouseGetPos(&mx, &my)

VirtualLeft := SysGet(76)
VirtualTop := SysGet(77)
VirtualWidth := SysGet(78)
VirtualHeight := SysGet(79)

left := VirtualLeft
top := VirtualTop
right := left + VirtualWidth
bottom := top + VirtualHeight

CheckZone("TopLeft",
(mx <= left+cornerSize && my <= top+cornerSize))

CheckZone("TopRight",
(mx >= right-cornerSize && my <= top+cornerSize))

CheckZone("BottomLeft",
(mx <= left+cornerSize && my >= bottom-cornerSize))

CheckZone("BottomRight",
(mx >= right-cornerSize && my >= bottom-cornerSize))

CheckZone("TopEdge",
(my <= top+edgeSize))

CheckZone("BottomEdge",
(my >= bottom-edgeSize))

CheckZone("LeftEdge",
(mx <= left+edgeSize))

CheckZone("RightEdge",
(mx >= right-edgeSize))

return

; ===== 触发逻辑 =====

CheckZone(name, inside)
{
    global zones, zoneState, hoverTime, cooldown

    if (!zones[name].enabled)
        return

    state := zoneState[name]

    if (inside)
    {
        if (state.hoverStart == 0)
            state.hoverStart := A_TickCount

        if (!state.triggered) {
            if (A_TickCount - state.hoverStart > hoverTime) {
                if (A_TickCount - state.lastTrigger > cooldown) {
                    state.triggered := true
                    state.lastTrigger := A_TickCount

                    DoAction(name)
                }
            }
        }
    }
    else
    {
        state.hoverStart:=0
        state.triggered:=false
    }
}

; ===== 动作绑定 =====

DoAction(zone)
{
    if (zone == "TopLeft") {
        ; 显示桌面
        WinMinimizeAll()
    }
    else if (zone == "TopRight") {
        ; 打开终端
        Run "wt.exe"
    }
    else if (zone == "BottomLeft") {
        ; 锁屏
        DllCall("LockWorkStation")
    }
    else if (zone == "BottomRight") {
        ; 任务管理器
        Run "taskmgr.exe"
    }
    else if (zone == "TopEdge") {
        ; 虚拟桌面左
        Send "^#{Left}"
    }
    else if (zone == "BottomEdge") {
        ; 虚拟桌面右
        Send "^#{Right}"
    }
    else if (zone == "LeftEdge") {
        Run "notepad.exe"
    }
    else if (zone == "RightEdge") {
        Run "explorer.exe"
    }
}
