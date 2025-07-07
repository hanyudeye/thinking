---
layout: default
toc: false
title: 手机，安卓，ios，android应用开发
date:  2025-07-07T13:12:15+08:00
draft: true
---


# 网页

## 手机端预览 (局域网)

### vscode  Live Server 设置监听所有网址

搜索 liveServer.settings.host
把它设置为：

"liveServer.settings.host": "0.0.0.0"
这样 Live Server 就会监听所有网络接口，包括局域网
> npm run dev  / vite --host 
> 使用这些开发服务器，也要监听所有接口


使用 ipconfig/ ip address 查找服务器地址，手机连接同一网络，然后在手机上进行访问

# android
## 应用图标

1. 设计 1024*1024
2. 生成  Image Asset Studio 
