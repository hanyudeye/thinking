---
layout: default
toc: false
title: python编程语言
date:  2025-08-05T14:25:24+08:00
draft: true
---

## 🧠 一、Python 编程语言学习大纲（从零到进阶）

### 1. Python 基础语法

* Python 简介与安装
* Hello World & 交互式解释器
* 变量与数据类型
* 字符串与编码
* 运算符与表达式
* 注释

📘 推荐教材：
**《Python编程：从入门到实践》（作者：Eric Matthes）**

---

### 2. 控制流程

* 条件语句（if-else）
* 循环语句（for / while）
* range 与枚举
* break / continue / pass

---

### 3. 函数与作用域

* 定义函数与调用
* 参数传递
* 返回值
* 局部变量与全局变量
* Lambda 表达式

---

### 4. 数据结构

* 列表 List
* 元组 Tuple
* 字典 Dict
* 集合 Set
* 列表推导式

---

### 5. 文件操作

* 文件读取与写入
* 文件上下文管理（with open）
* JSON 文件处理

---

### 6. 异常处理

* try-except-finally
* 自定义异常

---

### 7. 面向对象编程

* 类与对象
* 构造方法 `__init__`
* 继承与多态
* 魔术方法 `__str__`, `__len__` 等
* 类属性与实例属性

---

### 8. 模块与包

* 模块导入
* 自定义模块
* 第三方包使用（pip）
* Python 标准库概览

---

### 9. Python 高级特性

* 迭代器与生成器
* 装饰器
* 上下文管理器（with）
* 反射与动态属性
* 多线程与多进程（基础）

---

## 🔧 二、Python 通用库学习大纲（按用途分类）

---

### 📊 数据分析类

#### 1. NumPy

* ndarray 数据结构
* 数组索引与切片
* 广播机制
* 数学函数与线性代数
  📘 教材推荐：《利用Python进行数据分析（第2版）》 作者：Wes McKinney

#### 2. Pandas

* Series 与 DataFrame
* 数据读取与清洗
* 分组 groupby
* 数据透视表与统计
* 合并与连接

#### 3. Matplotlib / Seaborn

* 折线图、柱状图、散点图等
* 子图与样式设置
* Seaborn 高级可视化接口

---

### 📈 机器学习/深度学习类

#### 4. Scikit-learn

* 分类、回归、聚类算法
* 数据预处理（StandardScaler 等）
* 模型选择与调参（GridSearchCV）

#### 5. TensorFlow / PyTorch（任选其一）

* 张量操作
* 自动求导
* 神经网络构建
* 训练与优化

📘 教材推荐：《深度学习入门：基于Python的理论与实现》

---

### 🌐 网络爬虫与数据采集类

#### 6. Requests

* GET / POST 请求
* 请求头、Cookies、Session

#### 7. BeautifulSoup / lxml

* HTML 解析
* 标签查找与内容提取

#### 8. Selenium

* 动态页面抓取
* 模拟点击、输入、滚动

📘 教材推荐：《Python网络数据采集（第2版）》

---

### 🔧 自动化与工具开发类

#### 9. OpenPyXL / Pandas Excel

* Excel 文件读写、格式化
* 多表单处理

#### 10. OS / shutil / pathlib

* 文件夹创建、遍历、删除
* 路径操作与文件管理

#### 11. re（正则表达式）

* 模式匹配
* 提取、替换、分割字符串

#### 12. logging / argparse

* 日志模块
* 命令行参数解析工具

📘 教材推荐：《Python自动化运维：技术与最佳实践》

---

### 🕸️ Web 开发类（可选）

#### 13. Flask / Django

* 路由、视图、模板
* 表单处理与验证
* 数据库 ORM
  📘 教材推荐：《Flask Web开发实战》

---

## 📚 附：配套教材清单（每类各一本）

| 类别        | 教材名称                    | 适合阶段 |
| --------- | ----------------------- | ---- |
| Python 基础 | 《Python编程：从入门到实践》       | 新手入门 |
| 数据分析      | 《利用Python进行数据分析（第2版）》   | 中高级  |
| 爬虫        | 《Python网络数据采集（第2版）》     | 中级   |
| 深度学习      | 《深度学习入门：基于Python的理论与实现》 | 中高级  |
| 自动化       | 《Python自动化运维：技术与最佳实践》   | 中高级  |
| Web 开发    | 《Flask Web开发实战》         | 中高级  |

