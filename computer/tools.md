

##  youtube 字幕下载

yt-dlp --write-sub --sub-lang en VIDEO_URL

## ollama Web UI 控制端

浏览器插件： Page Assist - 本地 AI 模型的 Web UI

##  查找工具 (按文件名)

- Everything: Windows下强大的文件搜索工具
- Listary:  Windows 下的文件搜索和应用启动工具
- ulauncher: Linux 下具有同Listary 相似功能的工具

## 资源下载

- m3u8视频下载  windows 下是 N_m3u8DL-CLI
- b 站视频下载 downKyi

## 激活工具

- AdobeGenP : Windows 平台的 Adobe 产品激活

## 分离人声

- Ultimate vocal remover gui

## 文本编辑

### VIM 配置

```.vimrc
inoremap kj <ESC>   kj 按键绑定<ESC> 键
```

> 在 windows 中是 _vimrc 文件

## 在wsl中设置子系统的默认用户

```sh
ubuntu.exe config --default-user {username}
```

## 应用程序在高分辨率屏幕进行缩放

Exec=netease-cloud-music --force-device-scale-factor=2 %U

## 远程拷贝

scp /path/to/file user@server:/path/to/destination # Copy file from local to server

scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary
或
scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary/tt.txt

## ssh

```
$ ssh-keygen -t rsa -C "youremail@example.com"
```
要用 ssh 无密码登录，要把本地公钥 ~/.ssh/id_rsa.pub 配置到服务器 的 ~/.ssh/authorized_keys 认证文件中，服务器才能接受您的认证。

## 直播录制  StreamCap

https://github.com/ihmily/StreamCap
一个桌面应用（支持 Windows 和 Mac），基于 FFmpeg 进行直播录制，覆盖40+国内外主流直播平台

## [pdf-craft](https://github.com/oomol-lab/pdf-craft)

命令行 Python 工具，用来将扫描的 PDF 文件转为 Markdown 和 EPUB，并通过 AI 进行 OCR。