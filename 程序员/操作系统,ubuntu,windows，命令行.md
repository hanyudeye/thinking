---
layout: default
toc: false
title: 操作系统,ubuntu,windows，命令行
date:  2025-07-03T05:51:11+08:00
categories: ['']
---

操作系统给了你一个控制计算机的 友好的方式和界面
> 没有操作系统的计算机 就像 没有思维的尸体一样，一动不动。

# 计算机操作系统

## 抽象设计，抽象理论

不管 是 **工厂里的机器**，或者 是 **计算机**，都提供了一个 友好的 **人机交互**的面板，方便人控制。

> **机器** 使用各种 **实体**控制开关，开关上会标注功能；**计算机**  现在因为是可编程的，界面虽然 **花哨**，但 **本质**还是提供各种 **功能**

## 操作系统提供了操作计算机的最基本的功能

- 开机，启动机器
- 文件系统，访问或修改文件
- 打开软件
- 设备管理，开关设备
- 网络管理
- 界面定制，环境定制
- 多任务， 同时打开多个软件

## 具体实现

处理器: 用来执行程序，时间分片或多核可以一次执行多个程序(进程中再分片给线程)

主板上的 BIOS 可以在 载入操作系统时 先 对硬件检测

中断模块可以变更执行轨道 到其他程序

外部IO 可以向外 输出数据/信息，或向内 输入数据/信息

用户级的应用 使用硬件需要调用 操作系统级API


# 流行操作系统

现在流行的操作系统，如 windows ，mac，ubuntu 都做的很复杂，功能很多。

## ubuntu 免费开源操作系统

### 软件管理

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

### 查看打开的端口

``` sh
ss -tuln
-t：显示 TCP 端口
-u：显示 UDP 端口
-l：仅显示监听（listening）状态
-n：显示数字（不解析域名/服务名）

# 快速看所有监听端口 + 进程名
sudo ss -tulpn
```

lsof 查看某个端口被谁占用
```
sudo lsof -i :80
```

### service
手动运行服务

``` sh
#显示服务
ls /etc/init.d


```

### systemctl
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

## windows

### 创建符号链接

``` powershell
mklink /D "C:\Users\Alice" "D:\Users\Alice"
```
C 是符号链接，D 是实际存储位置

## wsl

```sh
# 在wsl中设置子系统的默认用户
ubuntu.exe config --default-user {username}
```

## i3wm

### 应用程序在高分辨率屏幕进行2倍缩放
``` desktop
Exec=netease-cloud-music --force-device-scale-factor=2 %U
```

## wayland
