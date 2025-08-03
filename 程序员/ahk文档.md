---
layout: default
toc: false
title: ahk文档
date:  2025-08-01T10:21:00+08:00
draft: true
---

在 AutoHotkey 中，**控制快捷键（修饰键）**使用的是一套**特殊符号表示法**，用于组合热键或热字符串。这些符号可以和普通按键一起构成触发快捷键。

---

## 🔑 AutoHotkey 修饰键写法速查表

| 键名称           | 符号  | 示例                              | 含义            |
| ------------- | --- | ------------------------------- | ------------- |
| Ctrl          | `^` | `^c::MsgBox You pressed Ctrl+C` | Ctrl+C        |
| Alt           | `!` | `!a::MsgBox Alt+A pressed`      | Alt+A         |
| Shift         | `+` | `+b::MsgBox Shift+B pressed`    | Shift+B       |
| Win（Windows键） | `#` | `#e::Run explorer`              | Win+E 打开资源管理器 |

---

## ⌨️ 组合热键示例

```ahk
^!r::MsgBox 你按了 Ctrl + Alt + R
#+t::MsgBox 你按了 Win + Shift + T
^+!x::MsgBox 你按了 Ctrl + Shift + Alt + X
```

---

## 🔘 常见功能键写法

| 键名称       | 写法                         | 示例                            |
| --------- | -------------------------- | ----------------------------- |
| 回车（Enter） | `Enter`                    | `Enter::Send Hello`           |
| 空格（Space） | `Space`                    | `Space::MsgBox 空格被按了`         |
| Tab       | `Tab`                      | `Tab::Send {Tab}`             |
| Esc       | `Esc`                      | `Esc::ExitApp`                |
| Backspace | `Backspace`                | `Backspace::Send 删除`          |
| Delete    | `Delete`                   | `Delete::Send 删除键`            |
| ↑ ↓ ← →   | `Up` `Down` `Left` `Right` | `Up::MouseMove, 0, -10, 0, R` |

---

## 🧩 特殊符号写法说明

* `{}`：用于表示特殊键（如 `{Enter}`、`{Tab}`、`{Esc}`）
* `::`：用于绑定热键（左边是热键，右边是动作）
* `R`：相对坐标（用于鼠标移动）

---

## 📌 特殊示例合集

```ahk
; Ctrl + Shift + Esc 退出脚本
^+Esc::ExitApp

; Win + Left 键将鼠标左移
#Left::MouseMove, -50, 0, 0, R

; Alt + Space 输出 Hello
!Space::Send Hello

; 鼠标左键点击
z::Click

; 鼠标右键点击
x::Click right
```

---

## ✅ 快速记忆口诀

| 组合    | 符号  | 记法            |
| ----- | --- | ------------- |
| Ctrl  | `^` | "C帽子"         |
| Alt   | `!` | "感叹Alt"       |
| Shift | `+` | "加号是Shift"    |
| Win   | `#` | "#"像Win键的窗口符号 |

---

如你想，我可以帮你写一张图表或备忘清单，甚至为你量身定制一个快捷键控制脚本。需要吗？
