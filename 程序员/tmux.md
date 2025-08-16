---
layout: default
toc: false
title: tmux
date:  2025-08-16T10:46:03+08:00
draft: true
---

使用 [gpakosz/.tmux](https://github.com/gpakosz/.tmux.git) 配置后，tmux 的快捷键发生了一些变化，主要体现在以下几个方面：

### 1. **双前缀键支持（`C-b` 和 `C-a`）**

默认情况下，tmux 的前缀键是 `C-b`（即按住 `Ctrl` 键并按 `b`）。([GitHub][1])

而在 `.tmux` 配置中，添加了对 `C-a` 的支持，使其成为第二个前缀键。([GitHub][2])

这意味着你可以使用以下任意组合来执行 tmux 命令：

* `C-b` 后跟命令键，例如 `C-b c` 创建新窗口。
* `C-a` 后跟命令键，例如 `C-a c` 创建新窗口。([GitHub][1])

这种双前缀键的设计旨在提高操作的灵活性和舒适度。

### 2. **常用快捷键**

以下是一些常用的快捷键：

* **创建新窗口**：`<prefix> c`
* **关闭当前窗口**：`<prefix> &`
* **切换到下一个窗口**：`<prefix> C-h`
* **切换到上一个窗口**：`<prefix> C-l`
* **水平分割窗格**：`<prefix> -`
* **垂直分割窗格**：`<prefix> +`
* **切换窗格**：`<prefix> o`
* **进入复制模式**：`<prefix> [`
* **退出复制模式**：`q`
* **重载配置文件**：`<prefix> r`
* **编辑本地配置文件**：`<prefix> e`
* **恢复窗格（unzoom）和 最大化窗格（zoom）**：`<prefix> z`

其中，`<prefix>` 可以是 `C-b` 或 `C-a`。

### 3. **其他增强功能**

* **鼠标支持**：启用鼠标支持，允许使用鼠标选择窗格、调整窗格大小等。
* **自定义配置文件**：提供 `.tmux.conf.local` 文件，方便用户进行个性化配置。
* **美化主题**：提供美观的配色方案和状态栏样式。

如果你想查看所有可用的快捷键，可以按下 `<prefix> ?`，tmux 会显示所有绑定的快捷键列表。

希望这些信息能帮助你更好地使用 tmux！

[1]: https://github.com/tmux/tmux/wiki/Getting-Started?utm_source=chatgpt.com "Getting Started · tmux/tmux Wiki - GitHub"
[2]: https://github.com/gpakosz/.tmux?utm_source=chatgpt.com "Oh my tmux! My self-contained, pretty & versatile tmux configuration ..."
[3]: https://unix.stackexchange.com/questions/294956/how-do-i-get-a-default-tmux-configuration-file?utm_source=chatgpt.com "How do I get a default tmux configuration file?"
[4]: https://github.com/gpakosz/.tmux/blob/master/.tmux.conf.local?utm_source=chatgpt.com ".tmux/.tmux.conf.local at master · gpakosz/.tmux · GitHub"
