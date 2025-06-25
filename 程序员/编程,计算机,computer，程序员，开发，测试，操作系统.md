!我们人类生存需要一个环境，提供吃喝玩乐，工作。操作系统也提供了这个环境


# 计算机操作系统

## 概述
不管 是 **机器**，或者 是 **计算机**，都要有 一个 **人机交互**的面板，方便人控制。

> **机器** 使用各种 **实体**控制开关，开关上会标注功能；**计算机**  现在因为是可编程的，界面虽然 **花哨**，但 **本质**还是提供各种 **功能**

## 功能

### 机器启动开关

### 资源访问

1. 文件访问
2. 设备，网络访问

### 多任务带来的任务处理

### over

# ubuntu 系统 和 其环境下的 功能软件

# windows

## 创建符号链接
``` powershell
mklink /D "C:\Users\Alice" "D:\Users\Alice"
```
这会创建一个符号链接，使得 Windows 认为用户的文件夹仍然在 C:\Users\Alice，但实际存储位置在 D:\Users\Alice

## 软件资源 管理

apt : 管理 deb 包
snap: 集成度高，依赖库放一块了

### apt

``` sh
apt list  - 根据名称列出软件包
sudo apt remove linux-image-5.15 linux-headers-5.15 linux-modules-5.15
apt search - 搜索软件包描述
apt show - 显示软件包细节
apt edit-sources - 编辑软件源信息
```

## nginx 网站资源服务软件

``` sh
sudo apt install -y nginx-full
# 创建站点资源
sudo mkdir -p /var/www/WEB.com
sudo chown -R ubuntu:ubuntu /var/www/WEB.com
sudo chown -R www-data:www-data /var/www/WEB.com
sudo chmod -R 755 /var/www/WEB.com

# 创建配置文件
sudo vim /etc/nginx/sites-available/WEB.com

# 激活虚拟主机配置
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/lisz.me lisz.me

# 检查语法
sudo nginx -t

# 重载配置文件使虚拟主机生效
sudo nginx -s reload
sudo systemctl reload nginx

# 上传本地 _site 文件夹内容到远程主机
scp -r _site/* /var/www/lisz.me/

```

``` conf
# 配置文件内容

server {
    listen 80;  # 监听 80 端口
    server_name example.com www.example.com;  # 配置域名

    # 网站根目录
    root /var/www/example.com;  

    # 默认主页
    index index.html index.htm index.php;

    # 访问日志
    access_log /var/log/nginx/example.com.access.log;

    # 错误日志
    error_log /var/log/nginx/example.com.error.log;

    # 配置文件路径
    location / {
        try_files $uri $uri/ =404;  # 如果文件不存在，则返回 404 错误
    }

    # 配置 PHP 支持（如果需要）
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;  # 根据 PHP 版本调整
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME /var/www/example.com$document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}

```
## tmux 多个终端操作

``` tmux
PREFIX + c  创建工作区
PREFIX + | 或 -  创建水平或垂直终端 vertical
```

## vim 文本操作

``` vim

:w !sudo tee %  - 执行 sudo 保存文件
> :w !{cmd} 让 Vim 将当前缓冲区的内容作为标准输入传递给外部命令 {cmd}
> tee 命令将标准输入的内容写入指定文件（这里是当前文件）。
> % 是 Vim 中表示当前编辑文件路径的寄存器。
```

## service
手动运行服务

``` sh
#显示服务
ls /etc/init.d


```
## systemctl
!自动运行很多服务

``` sh
# 安装
sudo apt install systemd

# 重启生效
sudo reboot

# 检查初始化系统
ps -p 1 -o comm=
ps -p 1


```

## php-fpm

``` sh
# 前台运行
sudo php-fpm7.4 -F
# 后台运行
nohup php-fpm7.4 -F > /var/log/php-fpm.log 2>&1 &

# 查看是否运行
sudo systemctl status php7.4-fpm
ps aux | grep php-fpm

# 配置文件
/etc/php/7.4/fpm/pool.d/www.conf

# 日志
tail -f /var/log/php7.4-fpm.log

```

# python
## 创建虚拟环境
``` sh
python3 -m venv myenv
```

## 自动激活虚拟环境


``` sh
cd ~/your_project && source venv/bin/activate
```

# bug 追踪
## 设计原则
1. 每个任务都要列入bug追踪
2. Bug有多种状态，非 "打开" 或"关闭" 两种
3. 

# 怎么发送 json 类型的数据
 
在 Postman 中发送 JSON 类型的数据是非常简单的，以下是详细的步骤：
![](images/2025-01-10-14-09-21.png)
![](../images/2025-01-10-14-09-21.png)

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