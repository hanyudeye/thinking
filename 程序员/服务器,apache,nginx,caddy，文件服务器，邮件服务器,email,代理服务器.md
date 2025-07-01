# web服务器，http服务器，富文本服务器 的基本功能

监控协议，监控端口 (http 80，https 443[ 实用SSL 证书])

分析协议内容

返回响应内容到目标客户端



http://example.com        → 实际走的是端口 80
https://example.com       → 实际走的是端口 443



## caddy

### Caddyfile 配置实例
把两个 非 https 请求转发到 https，端口转发
``` json
https://xiaozhou.net
{
	encode gzip
        tls example.mail@gmail.com {
                protocols tls1.2
        }
        root * /usr/share/caddy
        file_server
}

http://www.xiaozhou.net
{
        redir https://xiaozhou.net{url}
}

http://xiaozhou.net
{
        redir https://xiaozhou.net{url}
}
```
shell 脚本
``` sh
docker run -d --restart=always --name caddy -p 80:80 -p 443:443 \
    -v /home/mysite:/usr/share/caddy/ \
    -v $PWD/Caddyfile:/etc/caddy/Caddyfile \
    caddy:2.4.5-alpine
```
容器直接暴露80端口和443端口到宿主机器即可。

### 1. **自动 HTTPS**
   Caddy 的最大亮点之一是它可以自动为你的网站启用 **HTTPS**，而无需你手动配置 SSL/TLS 证书。它会自动为每个站点申请和续期 SSL 证书（默认使用 Let's Encrypt）。这样，你无需担心 HTTPS 证书的管理或更新。

### 2. **简洁的配置文件**
   Caddy 使用非常简洁的 **Caddyfile** 配置文件来配置服务器。Caddyfile 的语法简单且易于理解，适合不需要太多复杂配置的用户。例如，一个典型的 Caddyfile 配置可能如下：
   ```
   example.com {
       root * /var/www/html
       file_server
   }
   ```
   这会告诉 Caddy 为 `example.com` 提供服务，并且服务静态文件。

### 3. **反向代理功能**
   Caddy 2 具有强大的反向代理功能，可以作为 API 网关或负载均衡器使用。你可以使用 Caddy 代理请求到其他应用程序（例如 Nginx、Docker 容器等），并且它支持配置灵活的路由、负载均衡、重定向等。

### 4. **插件扩展系统**
   Caddy 2 引入了一个插件系统，允许用户通过安装插件来扩展其功能。例如，可以添加身份验证、日志记录、监控等功能。Caddy 2 支持通过命令行轻松安装和启用插件。

### 5. **多站点支持**
   Caddy 可以轻松地管理多个站点，每个站点可以有独立的配置。你可以在同一台服务器上运行多个网站，而无需配置复杂的虚拟主机或配置文件。

### 6. **支持 HTTP/2 和 HTTP/3**
   默认情况下，Caddy 2 启用了 **HTTP/2**，并且可以通过配置启用 **HTTP/3**。这为现代 Web 提供了更高效、更快速的传输协议。

### 7. **强大的反向代理和负载均衡**
   Caddy 支持配置反向代理，它允许将请求转发到其他服务器或服务，还可以进行负载均衡，以提高应用的可靠性和性能。

### 8. **集成内建的 WebSocket 支持**
   Caddy 2 具有内建的 WebSocket 支持，简化了实时应用的配置，不需要额外的代理设置。

 Caddy 的网站配置文件叫Caddy 的网站配置文件叫 **`Caddyfile`**，以非常简洁、可读性强的语法著称。下面我将从简单到复杂，教你如何编写一个 Caddy 网站配置文件。

## 📄 1. 最简单的 Caddyfile 示例（自动 HTTPS）

```caddyfile
example.com

root * /var/www/html
file_server
```

### ✅ 解释：
- `example.com`：你的域名（Caddy 会自动申请 HTTPS 证书）
- `root * /var/www/html`：设置网站根目录
- `file_server`：开启静态文件服务器（自动处理目录索引、静态资源等）

---

## 📄 2. 加上反向代理（用于后端服务）

```caddyfile
example.com

reverse_proxy localhost:3000
```

### ✅ 解释：
- 把来自浏览器的请求转发到本地的 3000 端口（比如 Node.js、Python Flask）

---

## 📄 3. 多个站点配置

```caddyfile
# 第一个站点
example.com {
    root * /var/www/html
    file_server
}

# 第二个站点
api.example.com {
    reverse_proxy 127.0.0.1:5000
}
```

---

## 📄 4. 使用 HTTPS + 自定义端口 + 重定向

```caddyfile
https://example.com:8443 {
    root * /var/www/html
    file_server
}

http://example.com {
    redir https://example.com:8443{uri}
}
```


## 📄 5. 配合 Docker 或本地开发（无需域名）

```caddyfile
localhost:8080 {
    root * /app/public
    file_server
}
```


## 📦 常见指令一览：

| 指令            | 作用说明                             |
|-----------------|--------------------------------------|
| `root`          | 设置静态文件根目录                   |
| `file_server`   | 启用静态文件服务器（目录浏览）       |
| `reverse_proxy` | 反向代理请求到另一个服务             |
| `redir`         | 重定向 URL                           |
| `handle`        | 条Caddy 的网站配置文件叫 **`Caddyfile`**，以非常简洁、可读性强的语法著称。下面我将从简单到复杂，教你如何编写一个 Caddy 网站配置文件。


## 📄 1. 最简单的 Caddyfile 示例（自动 HTTPS）

```caddyfile
example.com

root * /var/www/html
file_server
```

### ✅ 解释：
- `example.com`：你的域名（Caddy 会自动申请 HTTPS 证书）
- `root * /var/www/html`：设置网站根目录
- `file_server`：开启静态文件服务器（自动处理目录索引、静态资源等）

---

## 📄 2. 加上反向代理（用于后端服务）

```caddyfile
example.com

reverse_proxy localhost:3000
```

### ✅ 解释：
- 把来自浏览器的请求转发到本地的 3000 端口（比如 Node.js、Python Flask）


## 📄 3. 多个站点配置

```caddyfile
# 第一个站点
example.com {
    root * /var/www/html
    file_server
}

# 第二个站点
api.example.com {
    reverse_proxy 127.0.0.1:5000
}
```


## 📄 4. 使用 HTTPS + 自定义端口 + 重定向

```caddyfile
https://example.com:8443 {
    root * /var/www/html
    file_server
}

http://example.com {
    redir https://example.com:8443{uri}
}
```

## 📄 5. 配合 Docker 或本地开发（无需域名）

```caddyfile
localhost:8080 {
    root * /app/public
    file_server
}
```


## 📦 常见指令一览：

| 指令            | 作用说明                             |
|-----------------|--------------------------------------|
| `root`          | 设置静态文件根目录                   |
| `file_server`   | 启用静态文件服务器（目录浏览）       |
| `reverse_proxy` | 反向代理请求到另一个服务             |
| `redir`         | 重定向 URL                           |
| `handle`        | 条件匹配路径，进行不同处理           |
| `log`           | 启用访问日志                         |
| `encode`        | 启用 gzip 压缩                       |
| `tls`           | 配置 HTTPS 证书/关闭自动 HTTPS       |


## 🛠 示例：更完整的生产级配置

```caddyfile
example.com {
    root * /var/www/html
    encode gzip
    file_server
    log {
        output file /var/log/caddy/access.log
    }
    tls user@example.com
}
```

## 📍Caddyfile 的位置
如之前所说，推荐放在：
```
/etc/caddy/Caddyfile
```

然后重启服务：

```bash
sudo systemctl reload caddy
```


# 本地测试

## ✅ 本地测试环境的常见用途

| 场景                        | 示例配置                          |
|-----------------------------|-----------------------------------|
| 静态网页测试                | HTML、Vue、React 等构建输出       |
| 后端接口调试（反向代理）    | Node.js、Flask、Django、Spring    |
| 模拟生产环境域名 + HTTPS     | 使用 `localhost` + 自签证书       |
| 和 Docker 联动本地服务测试  | Caddy + Docker Compose            |

## 🔧 示例 1：本地部署静态网页

假设你构建了一个 React 项目，构建产物在 `build/` 目录下：

```caddyfile
localhost:8080

root * ./build
file_server
```

启动命令：

```bash
caddy run --config Caddyfile
```

访问地址：[http://localhost:8080](http://localhost:8080)

## 🔧 示例 2：本地反向代理后端服务（如 Flask）

```caddyfile
localhost:3000

reverse_proxy localhost:5000
```

上面这个配置会把浏览器访问的 `localhost:3000` 请求代理到本地运行的 Flask 服务（监听 5000 端口）。


## 🔧 示例 3：配置本地 HTTPS（使用自签证书）

```caddyfile
localhost {
    tls internal
    root * ./build
    file_server
}
```

Caddy 会自动生成并使用本地受信的自签 TLS 证书（仅供开发测试用）。

> ⚠️ 你可能需要在浏览器中手动信任 Caddy 自签的本地 HTTPS 证书，或运行 Caddy 时加上 `--allow-private-imports`。

## 🐳 示例 4：和 Docker 搭配本地测试（Caddy + Docker Compose）

你可以用 Caddy 做前端代理，后端是用容器跑的服务。参考：

```yaml
version: "3"

services:
  web:
    image: caddy
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./site:/srv
    ports:
      - "8080:80"
```

## 🧠 小贴士

- Caddy 本地调试无需 root 权限（非 80/443 端口）
- 配合浏览器调试跨域、缓存问题非常方便
- Caddy 内置 gzip 压缩、日志记录，对开发也有帮助

# 文件传输服务 FTP	21

# 安全远程登录 SSH	22

