
## 如何让软件不在Windows底部任务栏（taskbar）显示

隐藏窗口：

```
^!h::
WinGet, id, ID, A

WinSet, ExStyle, +0x80, ahk_id %id%     ; WS_EX_TOOLWINDOW
WinSet, ExStyle, -0x40000, ahk_id %id%  ; WS_EX_APPWINDOW

WinMinimize, ahk_id %id%
WinRestore, ahk_id %id%

return
```
