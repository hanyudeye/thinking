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

## 怎么发送 json 类型的数据
 
### 1. **打开 Postman 并创建一个新的请求**
- 启动 Postman 应用。
- 点击左上角的 **"New"** 按钮，选择 **"Request"**。
- 在弹出的窗口中，给你的请求命名并选择一个合适的集合（Collection）来保存请求。

### 2. **设置请求类型为 POST 或 PUT**
- 在请求窗口的左侧，有一个下拉框，默认值是 **GET**。点击它并选择 **POST** 或 **PUT**，这通常是发送数据时使用的请求方法。
- 如果你需要向某个 API 发送数据，通常是 POST 或 PUT。

### 3. **设置请求头（Headers）**
- 在请求窗口中，切换到 **Headers** 标签。
- 在 **Key** 列中输入 `Content-Type`，在 **Value** 列中输入 `application/json`。这样，Postman 会告诉服务器，你发送的数据是 JSON 格式。
  
  示例：
  ```
  Key: Content-Type
  Value: application/json
  ```

### 4. **在 Body 中添加 JSON 数据**
- 切换到 **Body** 标签。
- 选择 **raw** 选项，然后在右侧的下拉框中选择 **JSON**。这将告诉 Postman 你要发送的是 JSON 格式的数据。
  
  示例：
  ```
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
  }
  ```

### 5. **发送请求**
- 在输入完 JSON 数据后，点击 **Send** 按钮，Postman 会将请求发送到你指定的 URL，并显示响应结果。

### 完整的流程：
1. **选择请求类型**（POST/PUT）。
2. **设置请求头**：`Content-Type: application/json`。
3. **在 Body 中输入 JSON 数据**。
4. **点击 Send 发送请求**。

### 例子：

假设你要发送以下 JSON 数据到某个 API：

```json
{
  "username": "testuser",
  "password": "mypassword"
}
```

#### 在 Postman 中：
- **Method**：POST
- **Headers**：
  ```
  Key: Content-Type
  Value: application/json
  ```
- **Body**：
  ```
  {
    "username": "testuser",
    "password": "mypassword"
  }
  ```

通过这个流程，你就能够向服务器发送 JSON 格式的数据了。

