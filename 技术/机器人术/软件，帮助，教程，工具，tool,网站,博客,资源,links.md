---
title: 软件，帮助，教程，工具，tool,网站,博客,资源
date:  2025-07-03T07:32:41+08:00
categories: ['']
draft: true
---

反思：计算机中的好用的工具

## 离线翻译

pip install argostranslate argostranslategui
argos-translate-gui

## 鼠标手势

反思： 我操作鼠标的唯二场景就是 ps中作图 和 浏览器中选择文本，其他地方都别用

https://github.com/yingDev/WGestures/releases

## ssh [登录验证]

> 我用某身份会见某AI，AI要对比我的签章，是否与公钥配对，配对后接见我
> 验证方法用 做题而不是回答密码的方式

1. 服务器出题
2. 你用私钥盖章
3. 服务器用公钥验章

``` sh
# 生成密钥
ssh-keygen -t rsa -C "youremail@example.com"
```
要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

