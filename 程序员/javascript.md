---
layout: default
toc: false
title: javascript
date:  2025-08-04T14:38:47+08:00
draft: true
---





# 包装信息
## package.json 与 package-lock.json

- package.json 描述项目的基本信息、依赖与版本、脚本 (非精确版本号，而是版本范围)
- package-lock.json 锁定项目，记录所有包的精确版本信息

尽量通过 npm install [package-name]@[version] 来安装套件，这样可以确保 package.json 中的版本范围与 package-lock.json 中的版本一致。

package-lock.json 档案应该加入 Git 版控，避免任何人可以更新

对于依赖冲突，可以删除 package-lock.json

对于过时的包，可以手动删除 pakcage.json 文件内的包，然后安装新的包，避免 **npm uninstall  包** 的时候依赖报错。