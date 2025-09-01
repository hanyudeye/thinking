---
layout: default
toc: false
title: git,版本管理，项目跟踪
date:  2025-07-09T10:50:58+08:00
draft: true
---


## git  [历史追踪/项目管理]

### 配置

``` sh
 #配置用户名 
git config --global user.name "你的新用户名"
# 查看配置
git config list
```


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


### 子模块操作

``` sh
# 添加
git submodule add <子模块仓库地址> <子模块路径>
# 拉取
git submodule update

```

# 在 wsl 中 处理 git 项目，如何和windows 下统一，因为在 windows 环境 换行符不同

你遇到的是 **Windows (CRLF)** 和 **Linux/WSL (LF)** 换行符不一致的问题，这在 Git 项目里很常见。
如果不统一，可能会导致 Git 反复提示文件被修改、代码 diff 杂乱等情况。

下面是让 WSL 和 Windows 统一换行符的推荐做法：

---

## 1. 明确目标

如果你是在 **跨 Windows + WSL** 工作，并且多人协作时还有其他系统参与，通常建议：

* **仓库内统一用 LF（`\n`）** → 跨平台最通用
* **Windows 编辑器自动转换显示为 CRLF**（但不影响 Git 提交内容）

---

## 2. 设置 Git 的换行符规则

### 方法 A（推荐）

在 **Git 全局配置** 中设置：

```bash
# 在 WSL 和 Windows 都执行
git config --global core.autocrlf input
```

意思：

* 提交到 Git 时：把 CRLF 转换成 LF
* 检出到本地时：保持文件原本的换行符，不强制改回 CRLF

### 方法 B（如果一定要本地 CRLF）

在 Windows 下：

```powershell
git config --global core.autocrlf true
```

在 WSL 下：

```bash
git config --global core.autocrlf input
```

这样 Windows 会检出 CRLF，WSL 会保持 LF，但提交时都会统一成 LF。

---

## 3. 用 `.gitattributes` 统一项目规则

在项目根目录创建 `.gitattributes`，例如：

```
* text=auto eol=lf
```

意思：所有文本文件提交到 Git 时都用 LF。
如果某些文件确实需要 CRLF，可以单独指定：

```
*.bat text eol=crlf
*.sh  text eol=lf
```

这样即使不同人系统不同，仓库里也会统一。

---

## 4. 修正已有换行符

如果仓库里已经有混乱的 CRLF/LF，可以一次性修正：

```bash
git add --renormalize .
git commit -m "Normalize line endings"
```

---

💡 **小建议**

* 在 VS Code 里启用 `files.eol: \n`（LF），这样无论在 WSL 还是 Windows 都能保持一致。
* 如果你频繁在 WSL 和 Windows 切换同一份工作区，最好使用 `.gitattributes`，这样规则是项目级的，不依赖个人配置。

---

如果你愿意，我可以帮你画一张 **WSL + Windows + Git 换行符工作流程图**，让整个过程一目了然。这样更容易理解为什么要这么配。
你要我直接画出来吗？

## 某个文件，原先没有加入 .gitignore 文件，后来加入了，但修改后还是需要提交，怎么把它忽略

你的问题是典型的 **文件已经被 Git 追踪（tracked），后来才被加入 `.gitignore`，但仍然会出现在 `git status` 里**。

原因：
`.gitignore` 只对 **未被追踪（untracked）** 的文件有效。
已经被提交过的文件，Git 会继续跟踪它，即使它出现在 `.gitignore` 中。

### ✅ 解决方案

你有两个选择：

---

### **方案 1：彻底不再跟踪该文件（忽略后不再提交）**

如果你希望 **以后完全不再提交这个文件**，用：

```bash
git rm --cached <文件路径>
```

例如：

```bash
git rm --cached config.json
```

然后提交：

```bash
git commit -m "Stop tracking config.json"
```

之后，`.gitignore` 才会真正生效。

---

### **方案 2：文件仍要保留追踪，但不想每次修改都提交**

这种情况 `.gitignore` 不起作用，因为文件仍然被追踪。
解决办法是使用 **assume-unchanged** 或 **skip-worktree** 标记。

#### 方法 A：`assume-unchanged`

```bash
git update-index --assume-unchanged <文件路径>
```

作用：告诉 Git “假装这个文件没变”。
如果需要恢复：

```bash
git update-index --no-assume-unchanged <文件路径>
```

#### 方法 B：`skip-worktree`

更常用，用于本地修改但不影响版本库：

```bash
git update-index --skip-worktree <文件路径>
```

取消：

```bash
git update-index --no-skip-worktree <文件路径>
```

---

### **区别**

* **`assume-unchanged`**：适合大型文件、本地调试不想频繁检测变化，但如果文件变大 Git 仍会检测。
* **`skip-worktree`**：适合配置文件，每个人本地不同，但不希望版本库记录这些差异。

---

✅ 总结：

* **不再跟踪** → `git rm --cached` + `.gitignore`
* **继续跟踪但忽略本地修改** → `skip-worktree`

---

要不要我帮你整理一个 **最佳实践场景对比表**，比如“配置文件”、“日志文件”、“临时调试文件”，该用哪种方法？

