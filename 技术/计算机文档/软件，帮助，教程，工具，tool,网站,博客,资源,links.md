---
title: 软件，帮助，教程，工具，tool,网站,博客,资源
date:  2025-07-03T07:32:41+08:00
categories: ['']
draft: true
---

## 离线翻译

pip install argostranslate argostranslategui
argos-translate-gui

## 鼠标手势

https://github.com/yingDev/WGestures/releases

## ssh 

私钥加密验证

1. 服务器出题
2. 你用私钥盖章
3. 服务器用公钥验章

``` sh
# 生成密钥
ssh-keygen -t rsa -C "youremail@example.com"
```
要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

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



