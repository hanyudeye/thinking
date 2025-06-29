软件，可以因为不同的行为，分为不同的类型
如有： 功能软件，游戏软件，编辑软件，浏览软件，行业软件....

# 功能软件

## git  [历史追踪/项目管理]
### 分支管理
``` sh
# 删除远程分支
git branch -r -d branch-name
git push origin :branch-name
# 删除本地分支
git branch -D origin/branch-name
```

### git windows 下文件名显示中文

``` sh
# 关闭 Git 对文件名的引号转义，保证文件名以原始方式显示
 git config --global core.quotepath off
 # 设置 Git 使用 UTF-8 编码来处理提交信息和文件名
 git config --global i18n.commitencoding utf-8
```

## scoop [软件管理]

``` sh
#ripgrep 文本搜索
scoop install main/rga
```

## i3wm，tmux [窗口管理] 

每个软件占用窗口的一部分
 
## autokey/autohotkey [快捷键管理]

## 翻译 [特定行业]

## yt-dlp [视频/字幕下载]

``` sh
# youtube 字幕下载
yt-dlp --write-sub --sub-lang en VIDEO_URL
m3u8视频下载  windows 下是 N_m3u8DL-CLI
b 站视频下载 downKyi
```

##  everything/启动器/grep [应用/文件查找工具]

- Everything: Windows下强大的文件搜索工具
- Listary:  Windows 下的文件搜索和应用启动工具
- ulauncher: Linux 下具有同Listary 相似功能的工具

## 激活工具、破解

- AdobeGenP : Windows 平台的 Adobe 产品激活

## 分离人声 [行业软件]

- Ultimate vocal remover gui

## 远程拷贝 [文件远程操作]
``` sh
scp /path/to/file user@server:/path/to/destination # Copy file from local to server

scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary
或
scp /home/zhao/data/test.txt zw@10.150.69.247: /C:/Users/zw/Desktop/summary/tt.txt
```
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

## [pdf-craft](https://github.com/oomol-lab/pdf-craft) [行业软件，图像识别]

命令行 Python 工具，用来将扫描的 PDF 文件转为 Markdown 和 EPUB，并通过 AI 进行 OCR。

# 网站
## 视频资源 [视频网站]

https://www.pexels.com/zh-cn/search/videos/{query}

https://search.bilibili.com/all?keyword={query}

https://4khdr.cn/
https://www.aliyundrive.com/s/McXw86wJaBU/folder/649489ae5421e049b19242feb641b7415488a43e
https://www.cilixiong.org/


网络电视台  https://tv.garden/
电影字幕下载 : https://yts.mx/
字幕转换 https://converter.app/cn/vtt-srt/

## 图片 [图片网站]

https://cn.bing.com/images/search?q={query}&form=HDRSC2&first=1
https://www.pexels.com/zh-cn/search/{query}

## 图片去背景 [图像处理]
https://remove.photos/zh-cn/

## 白板 [笔记软件]

https://excalidraw.com/

## 查找相似图片 [图片网站，相似图片查找]
https://tineye.com/how
https://www.google.com/

## 什么值得买 [购物比对网站]

https://search.smzdm.com/?c=faxian&s={Query}&order=time&v=b

## github [开源仓库]

https://github.com/search?q={query}

## tts 文本转语音 [行业软件]

https://ai.bingal.com/cn/ai-tts/

## 音效下载 [行业软件]

https://sc.chinaz.com/yinxiao/

## 小工具

二维码 https://cli.im/
IP 地址  https://tool.lu/ip/
站长之家 https://tool.chinaz.com/

[HTML to JSX](https://transform.tools/html-to-jsx)
[文件或文本共享Pastebin](https://paste.c-net.org/)
[Scoop - Apps](https://scoop.sh/#/apps)
https://scoop.sh/#/apps?q={query}

[云鸽 - 文件传输助手网页版](https://yunge.in/)

免登录文件中转站
https://www.airportal.cn/
https://www.wenshushu.cn/



## huggingface [大模型、人工智能]

https://huggingface.co/

## 短视频 [视频网站，社交媒体]

[快手]https://cp.kuaishou.com/profile

[Facebook](https://www.facebook.com/)

[头条号](https://mp.toutiao.com/profile_v4/index)

[小红书创作服务平台](https://creator.xiaohongshu.com/creator/home)

[抖音创作服务平台](https://creator.douyin.com/creator-micro/home)

[西瓜创作平台](https://studio.ixigua.com/content)

[创作中心 - 哔哩哔哩弹幕视频网 - ( ゜- ゜)つロ 乾杯~](https://member.bilibili.com/platform/upload-manager/article)


## 数学 ,物理，英语 [教学网站]

数学
[Desmos | 图形计算器](https://www.desmos.com/calculator?lang=zh-CN)
[计算器套件 - GeoGebra](https://www.geogebra.org/calculator)
[Wolfram|Alpha：计算型智能](https://www.wolframalpha.com/)

物理
[Filter - PhET Simulations](https://phet.colorado.edu/en/simulations/filter?subjects=physics&type=html)

学习外语
[🌐 italki - 最好的语言学习应用，有认证的导师和小组课程](https://www.italki.com/zh-cn)

[Learn with the best online language tutors - Preply](https://preply.com/)
[Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.](https://inky-fold-a31.notion.site/a658257f925d45a8a0a4c3422dad1ddb?p=1f27423904b542aa91f41288e13b0ec5&pm=s)

[Notion笔记](https://www.notion.so/c1795493060d4edc9829f2cbcfa3d83f)

## 投资 [金融网站]

[财报SEC.gov | Home](https://www.sec.gov/)

[做独立开发前，你应该先了解 FIRE 运动 | 鸟飞鱼跃](https://sunnyd.top/blog/why-indie-devs-need-financial-management)

[POLOXUE's BLOG](https://www.poloxue.com/)

[Innomad一挪迈](https://innomad.io/)
[吕小荣](https://mednoter.com/)

## 版权 [行业网站，版权]

[CC Search Portal](https://search.creativecommons.org/)

## 名人名言 [知识分享网站]

[名人名言Inspirational Quotes at BrainyQuote](https://www.brainyquote.com/)

## 生活经验 [日常实用网站]
[有用经验](https://yyjingyan.com/)

## 英文 [行业网站]

### 招聘

[SEEK - Australia's no. 1 jobs, employment, career and recruitment site](https://www.seek.com.au/)

### 电子手工

[Adafruit Industries, Unique & fun DIY electronics and kits](https://www.adafruit.com/)

[blog.arduino.cc](https://blog.arduino.cc/2025/03/17/arduino-days-2025-is-almost-here/)

[您的制作 - Instructables --- Yours for the making - Instructables](https://www.instructables.com/)

[Etsy - Shop for handmade, vintage, custom, and unique gifts for everyone](https://www.etsy.com/)

[Craftsy.com | Express Your Creativity! | Craftsy](https://www.craftsy.com/)

[Arts & Crafts, Frames, Seasonal Décor | DIY & Inspiration | Michaels](https://www.michaels.com/)

[SparkFun Electronics](https://www.sparkfun.com/)


# Docker 虚拟机 

提供隔离的环境

## 应用

### 跑Hugo 博客

``` sh
docker run --rm -it -v $(pwd):/src -p 1313:1313 klakegg/hugo server
```
把 markdown 放到 **content/**目录

## 端口映射

Docker 端口映射是一种将容器内部的端口映射到主机上的特定端口的机制。这样可以使得容器内运行的服务可以通过主机的特定端口对外提供访问，从而实现容器与外部网络的通信。

要进行端口映射，可以使用 Docker 命令行工具或 Docker Compose 文件中的端口映射配置。下面是一些常用的方法：

### 使用 Docker 命令行工具
```bash
docker run -p 主机端口:容器端口 image_name
```
这条命令会将容器内部的 `容器端口` 映射到主机上的 `主机端口`，这样就可以通过主机的 `主机端口` 访问容器内的服务。

### 使用 Docker Compose 文件
在 Docker Compose 文件中，可以使用 `ports` 关键字来进行端口映射配置。示例：
```yaml
services:
  my_service:
    image: image_name
    ports:
      - "主机端口:容器端口"
```
这样配置后，使用 `docker-compose up` 启动容器时，端口映射就会生效。

### 多个端口映射
如果需要映射多个端口，可以在命令行工具或 Docker Compose 文件中使用多个 `-p` 参数或多个端口映射配置。

### 动态端口映射
有时候，也可以使用动态端口映射，让 Docker 自动选择一个未被占用的主机端口进行映射，例如：
```bash
docker run -p 容器端口 image_name
```

端口映射在 Docker 中是非常常见且重要的操作，它使得容器内的服务可以通过主机的端口与外部进行通信，提供了更加灵活和便捷的容器化应用部署方式。


## 提交容器副本使之成为一个新的镜像

docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名:[标签名]

### 运行 Linux 容器

#### 启动 Ubuntu 容器：
```bash
docker run -it ubuntu
```

这个命令会：
- 启动一个新的 Ubuntu 容器。
- 使用 `-it` 参数启动容器，并分配一个伪终端（Interactive Terminal），让你能够进入容器进行操作。

如果你拉取的是 **Debian** 或 **Alpine**，只需要将镜像名称替换为相应的名称即可：
```bash
docker run -it debian
docker run -it alpine
```

### 5. **运行容器时挂载卷（可选）**
如果你想将宿主机的某个目录挂载到容器中以便于数据共享，可以使用 `-v` 参数。例如，将宿主机的 `/host/path` 目录挂载到容器的 `/container/path` 目录：

```bash
docker run -it -v /host/path:/container/path ubuntu
```

### 6. **持久化容器数据**
默认情况下，Docker 容器是无状态的，一旦容器停止或删除，容器内的数据将会丢失。如果你需要持久化数据，可以使用 Docker 卷（volumes）或挂载宿主机目录到容器内。

```bash
docker run -it -v my_volume:/container/data ubuntu
```

这个命令会创建一个名为 `my_volume` 的 Docker 卷，并将其挂载到容器的 `/container/data` 目录下。

### 7. **退出容器**
当你完成对容器的操作后，可以使用以下命令退出容器：

```bash
exit
```

如果你只是想停止容器，但不退出容器，可以使用以下命令：
```bash
docker stop <container_id>
```

你可以通过 `docker ps -a` 查看所有容器的状态，包括运行中的和停止的容器。

### 8. **查看容器日志**
如果你需要查看容器的日志，可以使用以下命令：
```bash
docker logs <container_id>
```

### 9. **删除容器**
如果你不再需要某个容器，可以将其删除：
```bash
docker rm <container_id>
```

如果你想删除对应的镜像，可以使用：
```bash
docker rmi <image_name>
```
### 2. 配置国内镜像

由于 Docker Hub 在中国的访问速度较慢，可以配置使用国内的镜像源。

#### 2.1 使用 Docker Desktop GUI 配置镜像

1. **打开 Docker Desktop**。
2. **点击设置（Settings）**：
   - 在 Docker Desktop 的右上角，点击齿轮图标进入设置页面。
3. **选择 "Docker Engine"**：
   - 在左侧菜单中选择 "Docker Engine"。
4. **修改配置**：
   - 在 JSON 配置中，将 `registry-mirrors` 添加国内镜像地址。以下是一些常用的国内 Docker 镜像源：
     - **阿里云**：`https://<你的阿里云账号>.mirror.aliyuncs.com`
     - **网易**：`https://hub-mirror.c.163.com`
     - **腾讯云**：`https://mirror.ccs.tencentyun.com`
   - 修改后的配置示例：
     ```json
     {
       "registry-mirrors": [
         "https://hub-mirror.c.163.com"
       ]
     }
     ```
5. **点击 "Apply & Restart"** 以应用更改并重启 Docker。


