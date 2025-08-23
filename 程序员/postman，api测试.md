---
layout: default
toc: false
title: postman，api测试
date:  2025-08-04T16:42:22+08:00
draft: true
---

## 如何使用 Postman 进行 API 测试

我觉得大致上来说，使用 Postman 进行 API 测试的流程，可以分成以下几个步骤：

- 新增 HTTP 要求 (Add request)
- 先确认可以顺利按下 Send 发出 HTTP 要求
- 切换到 Tests 页签撰写测试案例（ 使用 JavaScript 即可）
- 再次按下 Send 发出 HTTP 要求，并查看测试结果 （ Test Results ）

![](images/2025-08-04-17-02-47.png)
![](../images/2025-08-04-17-02-47.png)

测试脚本如下：

``` js
pm.test("response is ok", function () {
    pm.response.to.have.status(200);
});
```

## postman 如何发送 post参数

在 **Postman** 中发送 **POST 参数**有几种常见方式，取决于你的 API 如何接收数据（`application/json`、`x-www-form-urlencoded`、`form-data`、`raw` 等）。以下是详细方法：

---

### ✅ **1. 选择请求方法和 URL**

* 打开 **Postman**。
* 在左上角选择请求方法为 **POST**。
* 输入 API 的 **URL**。

---

### ✅ **2. 在 Body 中添加参数**

点击 **Body** 选项卡，你会看到几个模式：

#### **(1) form-data**

* 适用于上传文件或表单提交。
* 勾选 **form-data**。
* 在 **Key** 栏填写参数名，在 **Value** 栏填写参数值。
* 如果需要上传文件，选择 **Type** 列中的 **File**。

---

#### **(2) x-www-form-urlencoded**

* 常用于普通表单提交（类似 HTML 表单）。
* 勾选 **x-www-form-urlencoded**。
* 和 form-data 类似，在 Key/Value 中输入参数。

---

#### **(3) raw (JSON 格式)**

* 常用于 REST API。
* 勾选 **raw**，并在右侧选择 **JSON(application/json)**。
* 在文本框中写 JSON，比如：

  ```json
  {
    "username": "test",
    "password": "123456"
  }
  ```

---

#### **(4) binary**

* 用于直接上传文件，通常不用带额外参数。

---

### ✅ **3. 设置 Headers（可选）**

* 如果是 **JSON**，确保 `Content-Type` 为：

  ```
  Content-Type: application/json
  ```
* 如果是表单：

  ```
  Content-Type: application/x-www-form-urlencoded
  ```

（Postman 通常会自动设置）

---

### ✅ **4. 点击 Send 发送请求**

* 查看 **Response** 确认参数是否被正确接收。

---

要不要我给你 **三种常用方式的截图示例**（form-data、x-www-form-urlencoded、JSON raw）？还是想看 **如何用 Postman 发送带文件的 POST 请求**？
