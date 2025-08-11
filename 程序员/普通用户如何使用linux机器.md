---
layout: default
toc: false
title: 普通用户如何使用linux机器
date:  2025-08-11T20:30:45+08:00
categories: ['文档']
---


在 Linux 系统中，普通用户常用的命令主要集中在**文件管理、系统查看、网络使用、软件安装、压缩解压、文本处理**等方面。
我给你分成几个类别，并说明每个命令的**使用场景**和**简单示例**。

---

## **1. 文件与目录管理**

| 命令                | 使用场景             | 示例                        |
| ----------------- | ---------------- | ------------------------- |
| `ls`              | 查看当前目录下的文件和文件夹   | `ls -l` 查看详细信息            |
| `cd`              | 切换目录             | `cd /home/user/Documents` |
| `pwd`             | 查看当前所在路径         | `pwd`                     |
| `mkdir`           | 创建新文件夹           | `mkdir project`           |
| `rmdir` / `rm -r` | 删除空目录 / 删除目录及内容  | `rm -r old_project`       |
| `cp`              | 复制文件或文件夹         | `cp file.txt backup.txt`  |
| `mv`              | 移动或重命名文件         | `mv old.txt new.txt`      |
| `find`            | 按条件搜索文件          | `find . -name "*.txt"`    |
| `tree`            | 以树形结构查看目录（可能需安装） | `tree /etc`               |

---

## **2. 文件内容查看与编辑**

| 命令              | 使用场景         | 示例                     |
| --------------- | ------------ | ---------------------- |
| `cat`           | 快速查看小文件内容    | `cat notes.txt`        |
| `more` / `less` | 分页查看长文件      | `less /var/log/syslog` |
| `head` / `tail` | 查看文件开头/结尾    | `tail -n 20 log.txt`   |
| `nano` / `vim`  | 在终端编辑文件      | `nano config.txt`      |
| `wc`            | 统计行数、单词数、字节数 | `wc -l file.txt`       |
| `grep`          | 按关键字搜索文件内容   | `grep "error" log.txt` |

---

## **3. 系统信息与进程管理**

| 命令             | 使用场景           | 示例                  |                |
| -------------- | -------------- | ------------------- | -------------- |
| `whoami`       | 查看当前用户名        | `whoami`            |                |
| `id`           | 查看当前用户 UID、组信息 | `id`                |                |
| `df -h`        | 查看磁盘空间         | `df -h`             |                |
| `du -sh`       | 查看文件夹大小        | `du -sh /home/user` |                |
| `top` / `htop` | 查看实时进程占用情况     | `top`               |                |
| `ps aux`       | 查看当前运行的进程      | `ps aux` |
| `kill`         | 结束进程           | `kill 12345`        |                |
| `uptime`       | 查看系统运行时间       | `uptime`            |                |
| `free -h`      | 查看内存使用情况       | `free -h`           |                |

---

## **4. 网络相关**

| 命令                  | 使用场景        | 示例                                 |
| ------------------- | ----------- | ---------------------------------- |
| `ping`              | 测试网络连通性     | `ping baidu.com`                   |
| `curl` / `wget`     | 下载文件或访问网页   | `wget http://example.com/file.zip` |
| `ifconfig` / `ip a` | 查看网络接口信息    | `ip a`                             |
| `netstat -tulnp`    | 查看网络连接      | `netstat -tulnp`                   |
| `scp`               | 通过 SSH 复制文件 | `scp file.txt user@server:/path/`  |

---

## **5. 软件管理（视发行版而定）**

* **Debian/Ubuntu 系列**

  * `sudo apt update` → 更新软件包索引
  * `sudo apt install pkg` → 安装软件
  * `sudo apt remove pkg` → 卸载软件
* **CentOS/RHEL 系列**

  * `sudo yum install pkg`
  * `sudo yum remove pkg`

---

## **6. 压缩与解压**

| 命令              | 使用场景           | 示例                                |
| --------------- | -------------- | --------------------------------- |
| `tar -czvf`     | 打包并压缩          | `tar -czvf backup.tar.gz folder/` |
| `tar -xzvf`     | 解压 tar.gz 文件   | `tar -xzvf backup.tar.gz`         |
| `zip` / `unzip` | 压缩 / 解压 zip 文件 | `zip archive.zip file1 file2`     |

---

## **7. 权限管理**

| 命令      | 使用场景     | 示例                              |
| ------- | -------- | ------------------------------- |
| `chmod` | 修改权限     | `chmod 755 script.sh`           |
| `chown` | 修改文件所有者  | `sudo chown user:user file.txt` |
| `sudo`  | 以管理员权限执行 | `sudo apt install git`          |

---

## **8. 其他常用小技巧**

* `history` → 查看命令历史
* `clear` → 清屏
* `alias` → 给常用命令设置别名
  例如：`alias ll='ls -l'`
