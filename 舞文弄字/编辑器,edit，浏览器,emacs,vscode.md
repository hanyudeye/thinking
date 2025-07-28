---
layout: default
toc: false
title: 编辑器,edit，浏览器,emacs,vscode
date:  2025-07-03T04:35:44+08:00
categories: ['']
---

# 关于编辑器的能力的思考

编辑器 要有编辑和浏览的 能力，然后这两种模式 可以快速切换
> 就像 vim 中 使用 i/Esc 键

在编码中，有自动补全函数，类，属性的能力

有插入 代码片段 snippets 的能力

执行代码的能力 （run code，preview)

折叠大纲 outline，函数 的能力

快速定位到某处  查找

# 浏览器

要有多标签的能力:  T 标签切换，<< 移动标签

历史功能 :  H	后退 L	前进

跳转到文本框  gi

快速跳转到某处  使用查找 search 

## vimium 

[done] 把 t 按键 映射到 T 同样的功能
``` 
map t Vomnibar.activateTabs
```
# vim

```.vimrc
inoremap kj <ESC>   kj 按键绑定<ESC> 键
```
> 在 windows 中是 _vimrc 文件

# spacemacs
## 小片段，模板，snippet


经常使用的 **小片文字** 可以存储为一个模板，使用时直接嵌入

``` lisp
把自定义的 snippet 放到配置 config 项目中
(setq my-snippet-path "F:/me/config/emacs/script/")

(add-to-list 'yas-snippet-dirs my-snippet-path)

完成 
```

## epub

| ~H~ or ~[~  | Previous chapter    |
| ~L~ or ~]~  | Next chapter        |
| ~K/u~       | Scroll up           |
| ~J/d~       | Scroll down         |
| ~g t~       | Table of contents   |

Hint: use ~SPC w c~ to center the buffer.



# vscode 编辑器
同 emacs 一样，也是配置灵活，但更快更官方

## 配置 折叠文件所有大纲 快捷键

完成
``` js
// settings.json
"vim.normalModeKeyBindingsNonRecursive": [
        {
            "before": [
                "z",
                "c"
            ],
            "commands": [
                "editor.fold"
            ]
        },
        {
            "before": [
                "z",
                "u"
            ],
            "commands": [
                "editor.unfold"
            ]
        },
        {
            "before": [
                "z",
                "m"
            ],
            "commands": [
                "editor.foldAll"
            ]
        },
        {
            "before": [
                "z",
                "o"
            ],
            "commands": [
                "editor.unfoldAll"
            ]
        }
]
```

# cursor

## 解决 CTRL-L 在 Terminal 窗口中调用 "add to chat" 而不是 clear the terminal screen 的 question

> 重新配置键盘快捷键 keybindings.json
```
// Place your key bindings in this file to override the defaults
[
    {
        "key": "ctrl+l",
        "command": "aichat.newchataction",
        "when": "!terminalFocus"
    },
    {
        "key": "ctrl+l",
        "command": "-aichat.newchataction"
    },
    {
        "key": "ctrl+l",
        "command": "workbench.action.terminal.selectCurrentLine",
        "when": "terminalFocus"
    }
]
```