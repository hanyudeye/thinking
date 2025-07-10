---
layout: default
toc: false
title: 网络,tcp，服务器,www
date:  2025-07-07T13:12:32+08:00
draft: true
---


# 网络

没网的人就只能在家里做事，有网可以看网络上其他计算机里面的数据(服务器)


## 实现 (数据分层协议)

> 本质 就是 **两个或多个互联的终端** 间 通过 **中间件** 连接。

### 应用层 (HTTP ,FTP)     [打包快递]
### 传输层 TCP/UDP          [运给快递站]
### 网络层 IP                       [快递站间分拣]
### 链路层 MAC，以太网    [司机拉货到下一个站点]



# 服务器 [应用]
服务器：要有安全属性，限制 哪个机器（IP），发送哪种协议（端口）的数据



## http 协议

![](images/2025-06-22-07-37-28.png)
![](../images/2025-06-22-07-37-28.png)

所谓幂等，就是该API执行多次和执行一次的结果是完全一样的，没有副作用。


## 流量代理/流量转发

### 系统代理

- 通过设置操作系统的“代理服务器”参数（如HTTP/HTTPS/SOCKS5代理），让浏览器、部分应用等遵循系统代理设置，将流量转发到代理服务器。
- 只对支持代理设置的应用生效
- 不支持命令行工具，系统级流量


### TUN (虚拟网络隧道)

- 通过创建虚拟网卡（TUN、TAP），将指定流量重定向到代理程序
- 可以实现全局代理

# CNAME

CNAME记录的设计目的是让一个域名成为另一个域名的别名。

如果你需要将多个子域名指向不同的目标，你可以为每个子域名设置不同的CNAME记录。例如：

```
www.example.com.  IN  CNAME  example.com.
blog.example.com. IN  CNAME  anotherdomain.com.
```

## 如果你想让多个域名都指向你的 GitHub Pages 站点，你应该：

1. **在 DNS 里配置多个 CNAME/A 记录** 指向 GitHub 的服务器。
2. **`CNAME` 文件中只保留一个“主域名”**，作为 GitHub Pages 的绑定域。

> 例如你可以：
> - DNS 添加：`www.example.com` 和 `alias.example.org` 都指向 GitHub Pages IP 或 `yourusername.github.io`
> - `CNAME` 文件只写：
>   ```
>   www.example.com
>   ```

这样访问 `alias.example.org` 也会跳转到你的站点，或者你通过域名服务商设置 URL 转发。
> ! 注意，因为 github 可以配置多个站点了，所以要在github custom 域名里重新设置


> 历史记录： www	CNAME	cname.vercel-dns.com 