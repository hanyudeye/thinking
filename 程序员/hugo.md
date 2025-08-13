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

## 添加描述 

在 **Hugo** 中为页面或站点添加 **description**（描述）和 **link**（通常指 canonical link 或 meta 链接）有几种常见方式，取决于是针对整站还是单个页面。下面详细说明方法：

---

### ✅ 1. **在站点配置文件中添加默认 description 和 link**

编辑你的 `config.toml`（或 `config.yaml`、`config.json`），添加全局参数：

**TOML 示例：**

```toml
baseURL = "https://example.com/"
title = "我的Hugo站点"
languageCode = "zh-cn"

[params]
  description = "这是我的网站描述"
```

**作用：**

* `params.description` 可以在模板中调用 `{{ .Site.Params.description }}`。
* `baseURL` 会用于 `<link rel="canonical" href="...">` 生成。

---

### ✅ 2. **在页面 front matter 中添加 description**

每个内容文件（如 `content/posts/my-post.md`）可以在 **front matter** 里设置 `description` 和 `link`。

**YAML 示例：**

```yaml
---
title: "文章标题"
date: 2025-08-13
description: "这是这篇文章的描述"
---
```

**TOML 示例：**

```toml
+++
title = "文章标题"
date = "2025-08-13"
description = "这是这篇文章的描述"
+++
```

---

### ✅ 3. **在模板中输出 description**

在 `layouts/_default/baseof.html` 或你的模板里，添加 meta 标签：

```html
<meta name="description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
```

**逻辑解释：**

* 如果页面有 `.Description`（即 front matter 里 `description`），优先使用。
* 否则 fallback 到站点的全局 `params.description`。

---

### ✅ 4. **添加 link 标签（canonical 或自定义）**

通常 canonical link 用 `.Permalink` 或 `.RelPermalink`：

```html
<link rel="canonical" href="{{ .Permalink }}">
```

如果你想加自定义的 link（比如 RSS、CSS 等），可以写在 `head` 部分：

```html
<link rel="alternate" type="application/rss+xml" title="{{ .Site.Title }}" href="{{ .Site.BaseURL }}index.xml">
```

---

### ✅ 5. **检查 Hugo 内置变量**

* `.Description` → 来自 front matter 或自动生成摘要。
* `.Permalink` → 页面绝对 URL。
* `.Site.Params.description` → 配置文件定义的全局描述。

---

要不要我帮你 **直接写一个完整的 `head` 模板示例**，里面包含 **description + canonical link + favicon + Open Graph**？这会让你的 Hugo 站点更 SEO 友好。

