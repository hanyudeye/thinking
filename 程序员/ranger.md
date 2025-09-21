---
layout: default
toc: false
title: ranger
date:  2025-09-21T15:00:03+08:00
categories: ['']
draft: true
---

<!-- 在 **ranger** 里，默认情况下按回车会用系统里设置的默认程序打开文件（调用 `rifle`）。如果你发现 mp3 文件回车没法直接播放，可以这样处理：

### 1. 检查 rifle.conf

ranger 打开文件是通过 `~/.config/ranger/rifle.conf` 里的规则来决定的。
先确认里面有类似播放音频的规则，比如：

```conf
# Audio
ext mp3,ogg,flac,m4a
    terminal = mpv -- "$@"
    ; aplay -- "$@"  # 或者 mpg123, mplayer 等
```

如果没有，就手动加上。

---

### 2. 设置默认播放器（推荐 mpv）

比如你想用 **mpv** 播放 mp3，可以这样加规则：

```conf
ext mp3,ogg,flac,m4a = mpv -- "$@"
```

---

### 3. 测试是否生效

在 ranger 中按 `Enter` 打开 mp3 文件，应该会自动调用 mpv 播放。

如果你想在 **终端里直接播放**（而不是新窗口），可以加 `terminal` 关键字：

```conf
ext mp3,ogg,flac,m4a
    terminal mpv -- "$@"
```

这样 ranger 会在当前终端里用 mpv 播放。

---

### 4. 临时解决办法

不改配置的话，也可以直接在 ranger 里按 `:open_with mpv` 或 `!mpv %s` 来播放。 -->

<!-- 在 **ranger** 里，所有“回车打开文件”的行为都由 **`rifle`**（配置文件是 `~/.config/ranger/rifle.conf`）控制。
你想让 **jpg 图片**回车就能用指定软件打开，可以这样做：

---

### 1. 打开 rifle.conf

如果你没改过，先复制一份默认配置：

```bash
ranger --copy-config=rifle
```

这会在 `~/.config/ranger/rifle.conf` 里生成一个配置文件。

---

### 2. 添加 jpg 图片规则

比如你想用 `feh` 打开图片，可以在 rifle.conf 里加：

```conf
# Images
ext jpg,jpeg,png,gif,bmp
    feh -- "$@"
```

如果你更喜欢 `sxiv`，就写：

```conf
ext jpg,jpeg,png,gif,bmp
    sxiv -- "$@"
```

---

### 3. 保存并测试

回到 ranger，移动到一个 `.jpg` 文件，按回车 → 就会调用你设定的软件打开。

---

### 4. 临时打开（不用改配置）

在 ranger 中输入：

```
:open_with feh
```

或者

```
!feh %s
```

也能直接用 feh 打开当前文件。 -->

