---
layout: default
toc: false
title: command，工具，命令
date:  2026-03-08T05:41:45+08:00
categories: ['']
draft: true
---

## 文件校验

### md5/SHA256

```powershell
Get-FileHash WeChatSetup.exe -Algorithm MD5
Get-FileHash WeChatSetup.exe -Algorithm SHA256
```

## 打开系统剪切板

```powershell
Win+v
Get-Clipboard
```

## tmux

命令:

select-layout even-horizontal 左右布局
select-layout even-vertical 上下布局


