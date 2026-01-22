---
layout: default
toc: false
title: git
date:  2026-01-20T13:11:17+08:00
---

## 如何拉去submodule 的仓库

1. 首次克隆，直接拉取所有子模块
   git clone --recurse-submodlues <主仓库地址>

2. 已克隆主仓库，补拉子模块内容

1. git submodule init
2. git submodule update
     git submodule update --recursive 如果子模块内还嵌套子模块

3. 日常更新

1. cd <子模块目录>
2. git pull origin main 拉取子模块
3. git add <子模块目录名>
4. git commit -m "更新子模块"
5. git push
