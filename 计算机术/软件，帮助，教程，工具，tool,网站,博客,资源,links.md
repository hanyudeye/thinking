---
layout: default
toc: false
title: 软件，帮助，教程，工具，tool,网站,博客,资源
date:  2025-07-03T07:32:41+08:00
categories: ['']
draft: true
---

## 启动器

- listary
- Raycast 

## 快捷键

- autokey/autohotkey 
- hammerspoon

## 翻译 
- sdcv  翻译单词
- translate-shell 翻译句子


## 下载字幕、视频
- yt-dlp 

``` sh
# youtube 字幕下载
yt-dlp --write-sub --sub-lang en VIDEO_URL
m3u8视频下载  windows 下是 N_m3u8DL-CLI
b 站视频下载 downKyi
``` 

## 应用/文件查找

- Everything: Windows下强大的文件搜索工具
- Listary:  Windows 下的文件搜索和应用启动工具
- ulauncher: Linux 下具有同Listary 相似功能的工具

## 激活工具、破解

- AdobeGenP : Windows 平台的 Adobe 产品激活

## 分离人声 [行业软件]

- Ultimate vocal remover gui

## Secure Copy 远程拷贝 [文件远程操作]
``` sh
scp /path/to/file user@server:/path/to/destination # Copy file from local to server

scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary
或
scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary/tt.txt
``` 

## 翻译 mtranserver
## ssh [登录验证]

密钥： 就是一串 看不懂的东西，用来验证用。
> 就像密码一样，用来核实身份用。
> 公钥和私钥验证：用公钥签名，私钥进行解密

``` sh
# 生成密钥
ssh-keygen -t rsa -C "youremail@example.com"
```
要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

## [直播录制 StreamCap](https://github.com/ihmily/StreamCap)

一个桌面应用（支持 Windows 和 Mac），基于 FFmpeg 进行直播录制，覆盖40+国内外主流直播平台

## 文字识别

[pdf-craft](https://github.com/oomol-lab/pdf-craft) 

命令行 Python 工具，用来将扫描的 PDF 文件转为 Markdown 和 EPUB，并通过 AI 进行 OCR。

##  文本搜索
- ripgrep

# 资源网站
## 视频、字幕资源 

- https://www.pexels.com/zh-cn/search/videos/{query}
- https://search.bilibili.com/all?keyword={query}
- https://4khdr.cn/
- https://www.aliyundrive.com/s/McXw86wJaBU/folder/649489ae5421e049b19242feb641b7415488a43e
- https://www.cilixiong.org/
- 网络电视台  https://tv.garden/
- 种子 https://thepiratebaye.org/search.php?q={query}
- 电影字幕下载 : https://yts.mx/
- 字幕转换 https://converter.app/cn/vtt-srt/
- 搜电影种子 https://en.rarbg-official.is/movies?search={query}
- 搜电影种子2 https://www.yts-official.cc/browse-movies?keyword={query}
## 图片 [图片网站]

https://cn.bing.com/images/search?q={query}&form=HDRSC2&first=1
https://www.pexels.com/zh-cn/search/{query}
# 工具网站

## 图片去背景 [图像处理]
https://remove.photos/zh-cn/

## video to gif 
视频转gif 文件

## 照片处理
ashampoo

## 白板 [笔记软件]

https://excalidraw.com/

## 查找相似图片 [图片网站，相似图片查找]
- https://tineye.com/how
- https://www.google.com/

## 什么值得买 [购物比对网站]

https://search.smzdm.com/?c=faxian&s={Query}&order=time&v=b

## github [开源仓库]

https://github.com/search?q={query}

## tts 文本转语音 [行业软件]

https://ai.bingal.com/cn/ai-tts/

## 音效下载 [行业软件]

https://sc.chinaz.com/yinxiao/

## 实用小工具

- 二维码 https://cli.im/
- IP 地址  https://tool.lu/ip/
- 站长之家 https://tool.chinaz.com/
- [HTML to JSX](https://transform.tools/html-to-jsx)
- [文件或文本共享Pastebin](https://paste.c-net.org/)
- [Scoop - Apps](https://scoop.sh/#/apps)
- https://scoop.sh/#/apps?q={query}
- [云鸽 - 文件传输助手网页版](https://yunge.in/)

## 免登录文件中转站
- https://www.airportal.cn/
- https://www.wenshushu.cn/

## huggingface [大模型、人工智能]

https://huggingface.co/

## 短视频 [视频网站，社交媒体]

- [快手]https://cp.kuaishou.com/profile
- [Facebook](https://www.facebook.com/)
- [头条号](https://mp.toutiao.com/profile_v4/index)
- [小红书创作服务平台](https://creator.xiaohongshu.com/creator/home)
- [抖音创作服务平台](https://creator.douyin.com/creator-micro/home)
- [西瓜创作平台](https://studio.ixigua.com/content)
- [创作中心 - 哔哩哔哩弹幕视频网 - ( ゜- ゜)つロ 乾杯~](https://member.bilibili.com/platform/upload-manager/article)


## 数学 ,物理，英语 [教学网站]

### 数学
- [Desmos | 图形计算器](https://www.desmos.com/calculator?lang=zh-CN)
- [计算器套件 - GeoGebra](https://www.geogebra.org/calculator)
- [Wolfram|Alpha：计算型智能](https://www.wolframalpha.com/)

### 物理
[Filter - PhET Simulations](https://phet.colorado.edu/en/simulations/filter?subjects=physics&type=html)

### 学习外语
- [🌐 italki - 最好的语言学习应用，有认证的导师和小组课程](https://www.italki.com/zh-cn)
- [Learn with the best online language tutors - Preply](https://preply.com/)
- [Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.](https://inky-fold-a31.notion.site/a658257f925d45a8a0a4c3422dad1ddb?p=1f27423904b542aa91f41288e13b0ec5&pm=s)
- [Notion笔记](https://www.notion.so/c1795493060d4edc9829f2cbcfa3d83f)

## 投资 [金融网站]

- [财报SEC.gov | Home](https://www.sec.gov/)
- [做独立开发前，你应该先了解 FIRE 运动 | 鸟飞鱼跃](https://sunnyd.top/blog/why-indie-devs-need-financial-management)
- [POLOXUE's BLOG](https://www.poloxue.com/)
- [Innomad一挪迈](https://innomad.io/)
- [吕小荣](https://mednoter.com/)

## 版权 [行业网站，版权]

[CC Search Portal](https://search.creativecommons.org/)

## 名人名言 [知识分享网站]

[名人名言Inspirational Quotes at BrainyQuote](https://www.brainyquote.com/)

## 生活经验 [日常实用网站]
[有用经验](https://yyjingyan.com/)

## 英文 [行业网站]

### 招聘

- [SEEK - Australia's no. 1 jobs, employment, career and recruitment site](https://www.seek.com.au/)
- [boss直聘](https://www.zhipin.com/)

### 电子手工

- [Adafruit Industries, Unique & fun DIY electronics and kits](https://www.adafruit.com/)
- [blog.arduino.cc](https://blog.arduino.cc/2025/03/17/arduino-days-2025-is-almost-here/)
- [您的制作 - Instructables --- Yours for the making - Instructables](https://www.instructables.com/)
- [Etsy - Shop for handmade, vintage, custom, and unique gifts for everyone](https://www.etsy.com/)
- [Craftsy.com | Express Your Creativity! | Craftsy](https://www.craftsy.com/)
- [Arts & Crafts, Frames, Seasonal Décor | DIY & Inspiration | Michaels](https://www.michaels.com/)
- [SparkFun Electronics](https://www.sparkfun.com/)

## links

- [有道翻译](https://dict.youdao.com/result?word={Argument}&lang=en)
- [抖音搜索](https://www.douyin.com/root/search/小狗)
- [tiktok搜索](https://www.tiktok.com/search?q=)
- [youtube搜索](http://youtube.com/results?q={query})
- [google地图](http://maps.google.com/?q={query})


## 数据统计

### 指数

- [google index](https://trends.google.com/trends/explore?q=UNH)
- [google 指数](https://trends.google.com/trends/explore?q=gpt&date=now%201-d&geo=US&hl=zh-CN)

## 图片型pdf 文字识别
``` sh
# 中英文识别
ocrmypdf -l chi_sim+eng input.pdf output.pdf
```

## acc 音频文件批量转mp3
批处理脚本
``` bat 
@echo off
for %%a in (*.aac) do (
    ffmpeg -i "%%a" "%%~na.mp3"
)
pause
```

## 屏蔽网站
ipconfig /flushdns
macbook： sudo dscacheutil -flushcache

