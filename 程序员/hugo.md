---
layout: default
toc: false
title: 使用 hugo 写博客
date:  2025-08-10T19:39:38+08:00
categories: ['文档']
---

Hugo 是一个用 Go 编写的静态网站生成器，命令行操作非常简洁。
下面是 Hugo 常用的基本命令，适合快速上手：


## **1. 创建新站点**

```bash
hugo new site myblog
```

在当前目录下创建一个名为 `myblog` 的 Hugo 项目文件夹。


## **2. 添加主题**

```bash
cd myblog
git init
git submodule add https://github.com/<主题作者>/<主题名>.git themes/<主题名>
```

然后在 `config.toml` 里指定：

```toml
theme = "<主题名>"
```


## **3. 创建新文章**

```bash
hugo new posts/hello-world.md
```

会在 `content/posts/` 下生成一篇 `hello-world.md`，并自动加上 YAML/TOML 前置元信息（Front Matter）。


## **4. 启动本地预览服务器**

```bash
hugo server -D
```

* `-D`：包含 `draft: true`（草稿） 的文章
* 访问：`http://localhost:1313`


## **5. 构建静态文件**

```bash
hugo
```

* 生成的静态网页会放在 `public/` 文件夹
* 可以部署到 GitHub Pages、Netlify 等服务


## **6. 其他常用选项**

```bash
hugo version          # 查看版本
hugo new              # 创建新内容
hugo list drafts      # 列出所有草稿
hugo server --port 8080  # 指定端口
hugo server --ignoreCache  # 清理 Hugo 缓存 & 资源目录 
rm -rf resources/_gen # 或删除缓存目录

```


