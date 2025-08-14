---
layout: default
toc: false
title: django,python
date:  2025-08-14T14:07:39+08:00
draft: true
---

## web 服务器

打开 开关后， 不停监控 web 服务端口，并进行分析后 执行相应的 指令。

## web 客户端

打开 开关后 ，可以发送 不同的 请求，并 接收 反馈信息。

# django 创建网站的基本命令

在 Django 中创建一个网站（或项目）通常涉及以下基本命令和步骤：

### **1. 安装 Django**

确保你有 Python 环境，然后安装 Django：

```bash
pip install django
```

检查版本确认安装成功：

```bash
django-admin --version
```

### **2. 创建 Django 项目**

用 `django-admin` 创建项目：

```bash
django-admin startproject mysite
```

这会生成一个项目目录结构，比如：

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### **3. 进入项目目录**

```bash
cd mysite
```

### **4. 启动开发服务器**

运行开发服务器，确保一切正常：

```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000/`，应该能看到 Django 欢迎页面。

### **5. 创建应用 (app)**

Django 项目由多个应用组成。用 `startapp` 创建一个应用：

```bash
python manage.py startapp blog
```

生成结构：

```
blog/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

然后到 `mysite/settings.py` 里，把 `blog` 添加到 `INSTALLED_APPS` 列表中。


### **6. 创建数据库并应用迁移**

Django 默认使用 SQLite 数据库，可以运行：

```bash
python manage.py migrate
```

### **7. 创建超级用户**

为了使用 Django 的后台管理：

```bash
python manage.py createsuperuser
```

<!-- 账号: aming -->
<!-- 密码: 12345678 -->

### **8. 开发过程常用命令**

* **创建模型迁移文件**：

```bash
python manage.py makemigrations
```

* **应用迁移到数据库**：

```bash
python manage.py migrate
```

* **查看可用命令**：

```bash
python manage.py help
```

* **打开 Django shell**：

```bash
python manage.py shell
```

要不要我帮你整理一张 **Django 基础命令速查表（含命令+用途）**？这样你写项目的时候可以直接参考。

## 定义模型 [models.py]

``` py
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

 @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

   @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
```

将在数据库 创建 **Blog** 和 **Category** 表

get_absolute_url 响应：/blog/view/how-to-create-a-basic-blog-in-django.html

有过时了！

