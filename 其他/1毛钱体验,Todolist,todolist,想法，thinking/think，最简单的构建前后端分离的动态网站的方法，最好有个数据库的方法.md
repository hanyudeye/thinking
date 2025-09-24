---
layout: default
toc: false
title: think，最简单的构建前后端分离的动态网站的方法，最好有个数据库的方法
date:  2025-08-16T09:59:08+08:00
draft: true
---

todo: 做一个个人的留言板

用组装的方式，能更快的搭建功能

## 1️⃣ 技术栈选择（最简单的组合）

* **前端**：HTML + CSS + JavaScript（可以用 React/Vue 进阶）
* **后端**：Node.js + Express（简单、社区多、上手快）
* **数据库**：SQLite 或 MySQL 或 MongoDB

  * **SQLite**：轻量，零配置，非常适合小型项目
  * **MongoDB**：NoSQL，文档化，配合 Node.js 非常流畅

> 如果是初学者，我推荐 **Node.js + Express + SQLite**，最省配置。

## 2️⃣ 项目结构示例

```
myapp/
├── backend/
│   ├── server.js       # 后端入口
│   ├── routes.js       # API 路由
│   └── database.db     # SQLite 数据库
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── package.json
```

## 3️⃣ 后端示例（Node.js + Express + SQLite）

**安装依赖**

```bash
npm init -y
npm install express sqlite3 cors
```

**server.js**

```javascript
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// 连接数据库（没有会自动创建）
const db = new sqlite3.Database('./database.db');

// 创建一个简单表
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)`);

// API: 获取所有用户
app.get('/api/users', (req, res) => {
    db.all("SELECT * FROM users", (err, rows) => {
        if(err) return res.status(500).send(err);
        res.json(rows);
    });
});

// API: 添加用户
app.post('/api/users', (req, res) => {
    const { name } = req.body;
    db.run("INSERT INTO users (name) VALUES (?)", [name], function(err){
        if(err) return res.status(500).send(err);
        res.json({ id: this.lastID, name });
    });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
```

## 4️⃣ 前端示例（HTML + JS）

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>前后端分离 Demo</title>
</head>
<body>
<h1>用户列表</h1>
<ul id="userList"></ul>

<input type="text" id="userName" placeholder="输入用户名">
<button onclick="addUser()">添加用户</button>

<script src="app.js"></script>
</body>
</html>
```

**app.js**

```javascript
const apiUrl = "http://localhost:3000/api/users";

async function fetchUsers(){
    const res = await fetch(apiUrl);
    const users = await res.json();
    const list = document.getElementById('userList');
    list.innerHTML = '';
    users.forEach(u => {
        const li = document.createElement('li');
        li.textContent = u.name;
        list.appendChild(li);
    });
}

async function addUser(){
    const name = document.getElementById('userName').value;
    await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    });
    document.getElementById('userName').value = '';
    fetchUsers();
}

// 初始加载
fetchUsers();
```

## ✅ 总结

* 这是最简单的 **前后端分离**模式：前端页面通过 **API** 与后端通信。
* 数据库使用 **SQLite**，零配置。
* 可拓展：

  * 换 MongoDB 或 MySQL
  * 使用 Vue/React 代替纯 JS
  * 增加用户登录、权限等功能

如果你愿意，我可以帮你做一个 **最小可运行的“前后端分离 + 数据库”项目包**，你一拉下来就能直接运行，省去配置烦恼。

你希望我直接帮你生成这个吗？

# 案例

太好了！我帮你整理一个**最小可运行的前后端分离 + SQLite 数据库项目包**，可以直接运行。下面是完整文件和步骤。

## 1️⃣ 项目目录结构

```
myapp/
├── backend/
│   ├── server.js
│   ├── database.db    (首次运行自动创建)
├── frontend/
│   ├── index.html
│   └── app.js
└── package.json
```

---

## 2️⃣ 后端部分（Node.js + Express + SQLite）

**package.json**

```json
{
  "name": "myapp",
  "version": "1.0.0",
  "main": "backend/server.js",
  "scripts": {
    "start": "node backend/server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "sqlite3": "^5.1.6",
    "cors": "^2.8.5"
  }
}
```

**backend/server.js**

```javascript
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const db = new sqlite3.Database('./backend/database.db');

// 创建表
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)`);

// 获取用户列表
app.get('/api/users', (req, res) => {
    db.all("SELECT * FROM users", (err, rows) => {
        if(err) return res.status(500).send(err);
        res.json(rows);
    });
});

// 添加用户
app.post('/api/users', (req, res) => {
    const { name } = req.body;
    db.run("INSERT INTO users (name) VALUES (?)", [name], function(err){
        if(err) return res.status(500).send(err);
        res.json({ id: this.lastID, name });
    });
});

app.listen(3000, () => console.log('Server running at http://localhost:3000'));
```

---

## 3️⃣ 前端部分（HTML + JS）

**frontend/index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>前后端分离 Demo</title>
</head>
<body>
<h1>用户列表</h1>
<ul id="userList"></ul>

<input type="text" id="userName" placeholder="输入用户名">
<button onclick="addUser()">添加用户</button>

<script src="app.js"></script>
</body>
</html>
```

**frontend/app.js**

```javascript
const apiUrl = "http://localhost:3000/api/users";

async function fetchUsers(){
    const res = await fetch(apiUrl);
    const users = await res.json();
    const list = document.getElementById('userList');
    list.innerHTML = '';
    users.forEach(u => {
        const li = document.createElement('li');
        li.textContent = u.name;
        list.appendChild(li);
    });
}

async function addUser(){
    const name = document.getElementById('userName').value;
    if(!name) return alert("请输入用户名");
    await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    });
    document.getElementById('userName').value = '';
    fetchUsers();
}

// 初始加载
fetchUsers();
```

---

## 4️⃣ 运行步骤

1. 安装 Node.js（确保版本 >= 16）
2. 在项目根目录执行：

```bash
npm install
```

3. 启动后端：

```bash
npm start
```

4. 打开 `frontend/index.html`（直接在浏览器打开即可）

> 注意：如果浏览器有跨域问题，可以用 VS Code 插件 Live Server 或者把前端放在 Express 静态目录下。

这样就有一个**最小可运行的前后端分离动态网站**，支持数据库增删查用户列表。

我可以帮你**改进一下，让前端也能直接通过 Express 访问**，避免跨域问题，这样只要打开 `http://localhost:3000/` 就能看到网页。

 -->
