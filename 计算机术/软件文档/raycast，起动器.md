---
layout: default
toc: false
title: raycast，起动器
date: 2025-12-31T02:48:00+08:00
categories: ['']
draft: true
---

 在 **Raycast** 中查找文件非常简单高效，它内置了强大的 **File Search**（文件搜索）功能，利用 macOS 的 Spotlight 索引，支持模糊搜索、预览和快速操作。以下是详细步骤和技巧：

### 基本使用方法
1. **启动 Raycast**：
   - 默认快捷键是 `Option + Space`（或你自定义的快捷键）。
   - 打开后，直接在搜索框中输入文件名的一部分，Raycast 会优先显示应用、命令等结果。

2. **进入文件搜索模式**：
   - 在 Raycast 主搜索框中输入关键词如 `Search Files` 或简写 `sf`（如果你设置了别名），然后按回车进入专用文件搜索界面。
   - 或者直接设置一个全局热键（Hotkey）给 **Search Files** 命令（推荐：在 Raycast 设置中搜索 "Search Files"，为其分配如 `Cmd + Shift + F`）。
   - 进入后，直接输入文件名、路径或关键词，即可实时显示匹配的文件列表。
     - 支持模糊搜索（fuzzy search），比如输入 "report2025" 就能匹配 "Annual_Report_2025.pdf"。
     - 默认显示最近打开的文件，便于快速访问。

3. **搜索结果操作**：
   - 选中文件后，按 `回车` 直接打开。
   - 按 `Cmd + K` 打开动作面板（Action Panel），可以：
     - 在 Finder 中显示文件。
     - 复制路径/文件名。
     - Quick Look 预览（按空格键快速预览内容，而不打开应用）。
     - 移动、复制、删除文件等。
   - 右侧会显示文件预览和元数据（如大小、修改日期）。

### 高级搜索技巧
- **自然语言搜索**：支持如 ".txt in ~/Desktop"（搜索 Desktop 中的 txt 文件）。
- **过滤范围**：
  - 在搜索界面右上角有过滤器，可以选择 "User Files"（仅用户文件，避免系统文件干扰）或 "All Files"。
- **优化搜索准确性**：
  - 默认可能同时搜索文件名和内容，导致结果过多。建议调整：
    - 去 Raycast 设置（`Cmd + ,`） → Extensions → File Search → 将搜索模式改为 "Name"（仅文件名），这样更快更准。
- **搜索隐藏文件或外部驱动器**：
  - Raycast 支持隐藏文件。
  - 对于外部盘，需要在系统设置 → 隐私与安全性 → 完全磁盘访问权限 中授予 Raycast。

### 如果搜索不到文件
- 检查 Spotlight 索引：Raycast 依赖 Spotlight。
  - 系统设置 → Spotlight → 隐私标签：临时添加问题文件夹后再移除，可重建索引。
- 授予权限：首次使用 File Search 时，Raycast 会提示授予文件访问权限。
- 重启 Raycast 或 Mac，有时索引需要时间更新。

### 推荐扩展（在 Raycast Store 中搜索安装）
- **Folder Search**：专门搜索和管理文件夹，支持快速移动文件。
- **Fuzzy File Search**：更强大的模糊路径搜索，适合深层嵌套文件夹。
- 其他如特定工具的搜索（e.g., Figma 文件搜索），根据需求安装。

Raycast 的文件搜索比系统 Spotlight 更智能、动作更多，用习惯后效率大幅提升。如果你常搜文件，强烈建议为 **Search Files** 设置别名（如 "wj" 为文件）或热键，一步直达！如果有具体问题，可以再描述场景。

