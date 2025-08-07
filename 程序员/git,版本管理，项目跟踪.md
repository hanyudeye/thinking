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

