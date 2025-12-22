---
layout: default
toc: false
title: 终端提高效率，zsh，终端,环境优化,tmux,vim,终端,sh,bash
date:  2025-08-11T21:00:05+08:00
categories: ['']
---


# 终端，命令行

命令行中，程序一般都没有外观的，除了一些编辑工具，或交互程序。一般执行命令程序后，下面接着会显示命令执行的结果。

# 如何动态查找文件，并编辑

在 **Zsh** 环境中，要将 **Ctrl + F** 设置为一个动态查找的命令，通常我们会配置为 **fzf**（一个基于模糊搜索的命令行查找工具）。通过这个工具，可以实现按键输入动态查找文件或历史命令。

下面是配置 **Ctrl + F** 使其能动态查找文件或命令的步骤。

### 1. **安装 `fzf`**
首先，需要安装 `fzf`，它是一个常用的命令行查找工具，支持模糊搜索。

如果你还没有安装 `fzf`，可以通过以下命令安装：

- **通过 Homebrew（macOS/Linux）安装：**
  ```bash
  brew install fzf
  ```

- **通过 Git 安装（适用于所有操作系统）：**
  ```bash
  git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
  ~/.fzf/install
  ```

### 2. **配置 `Ctrl + F` 快捷键来启动 `fzf`**
接下来，我们配置 **Ctrl + F** 快捷键在 Zsh 中启动 `fzf` 进行动态查找。

编辑你的 **Zsh 配置文件**（通常是 `~/.zshrc`）并添加以下内容：

```bash
# 配置 Ctrl + F 快捷键来启动 fzf 进行文件查找
bindkey -s '^F' 'fzf\n'
```

这个配置会将 **Ctrl + F** 快捷键绑定为运行 `fzf` 命令，并模拟回车。

### 3. **配置 `fzf` 实现动态查找**
`fzf` 本身支持模糊搜索，你可以将其与不同的查找目标结合使用。

例如：

- **文件查找：**
  使用 `fzf` 查找当前目录下的文件：
  ```bash
  bindkey -s '^F' 'fzf --preview "cat {}"\n'
  ```

- **历史命令查找：**
  使用 `fzf` 查找历史命令：
  ```bash
  bindkey -s '^F' 'history | fzf\n'
  ```

### 4. **保存并重启 Zsh**
完成配置后，保存并重新加载你的 **Zsh 配置**，你可以通过以下命令来使修改生效：

```bash
source ~/.zshrc
```

### 5. **测试**
现在，按下 **Ctrl + F** 快捷键，你应该能够触发 `fzf` 来进行动态查找，无论是查找文件还是历史命令，`fzf` 都会提供模糊匹配的实时搜索体验。

### 其他 `fzf` 用法：
- 查找文件路径，并使用 vim 编辑选中的文件（如果你希望在目录中查找文件）：
  ```bash
  bindkey -s '^F' 'fzf --preview "cat {}" --bind "enter:execute(vim {})"\n'
  ```

- 查找命令历史并执行（输入历史命令并执行）：
  ```bash
  bindkey -s '^F' 'history | fzf | sed "s/^[ ]*[0-9]\+  //" | eval\n'
  ```

这样，通过 `fzf` 和 `bindkey` 的配合，
**Ctrl + F** 快捷键就能够实现动态模糊查找的功能，极大提升命令行效率。

# tmux

窗口管理软件，可以把终端切割成不同窗口，多窗口执行不同命令

# 定时任务 cron 

cron 本身是基于分钟级别的调度工具，**最小的时间粒度是 1 分钟**，所以直接用 cron 没办法实现“每 10 秒”这种间隔。
如果你只是想测试，可以用两种思路：

### **1. 编辑定时任务**

在终端输入：

```bash
crontab -e
```

这是当前用户的定时任务编辑器。

---

### **2. 按格式写入任务**

cron 的格式是：

```
分 时 日 月 星期  命令
```

* **分**：0–59
* **时**：0–23
* **日**：1–31
* **月**：1–12
* **星期**：0–7（0 和 7 都表示星期天）
* **命令**：你要执行的脚本或命令

例子：

```bash
# 每天凌晨 2 点执行备份脚本
0 2 * * * /home/user/backup.sh

# 每隔 5 分钟执行一次脚本
*/5 * * * * /home/user/task.sh

# 每周一上午 8 点执行命令
0 8 * * 1 echo "Weekly report generation"
```

### **3. 保存并退出**

* 如果是 `vi` 或 `vim`，按 `ESC`，输入 `:wq` 回车
* 如果是 `nano`，按 `Ctrl+O` 保存，`Ctrl+X` 退出

保存后，`cron` 会自动加载新任务。

### **4. 查看当前定时任务**

```bash
crontab -l
```

### **5. 检查是否运行**

* 查看 `cron` 服务状态（不同系统命令不同）：

```bash
systemctl status cron   # Debian/Ubuntu
systemctl status crond  # CentOS/RHEL
```

* 查看执行日志：

```bash
grep CRON /var/log/syslog    # Debian/Ubuntu
grep CRON /var/log/cron      # CentOS/RHEL
```

### **1. 标准 cron（分钟级）示例**

比如每分钟在文件末尾加一行：

```bash
* * * * * echo "测试 $(date '+\%F \%T')" >> /tmp/test.log
```

意思：每分钟执行一次，把当前时间追加到 `/tmp/test.log`。

---

### **2. 每 10 秒一次（用 shell 循环模拟）**

因为 cron 做不到秒级，可以让它启动一个脚本，脚本内部用 `sleep` 控制：

```bash
#!/bin/bash
for i in {1..6}  # 6 次，每次间隔 10 秒，总共 1 分钟
do
    echo "测试 $(date '+%F %T')" >> /tmp/test.log
    sleep 10
done
```

保存为 `/home/user/test.sh`，给执行权限：

```bash
chmod +x /home/user/test.sh
```

然后在 cron 里写：

```bash
* * * * * /home/user/test.sh
```

这样就会**每分钟启动一次脚本**，脚本内部会每 10 秒加一行。

---

### **3. 进阶：系统级秒级任务**

如果你真要秒级执行，可以用：

* `systemd` 定时器（`OnCalendar` 或 `OnActiveSec=10`）
* `watch` 命令：

  ```bash
  watch -n 10 'echo "测试 $(date)" >> /tmp/test.log'
  ```
* 后台 `while true` 循环脚本

## cron 的时间格式一般是 5 个字段（有时带第 6 个字段），按顺序是：

```
分   时   日   月   周   [命令]
```

每个字段的含义：

| 字段位置        | 范围   | 含义                 |
| ----------- | ---- | ------------------ |
| 分 (Minute)  | 0-59 | 第几分钟执行             |
| 时 (Hour)    | 0-23 | 第几个小时执行（24 小时制）    |
| 日 (Day)     | 1-31 | 每月的第几天             |
| 月 (Month)   | 1-12 | 第几个月执行             |
| 周 (Weekday) | 0-7  | 星期几执行，0 和 7 都表示星期日 |


### 常用写法规则

* `*`  ：表示“任意值”，比如 `* * * * *` 表示每分钟执行一次
* `,`  ：枚举多个值，比如 `0,15,30,45` 表示每小时的 0、15、30、45 分执行
* `-`  ：范围，比如 `1-5` 表示从 1 到 5
* `/`  ：步长，比如 `*/10` 表示每隔 10 单位执行一次


### 例子

1. **每分钟执行一次**

   ```
   * * * * * command
   ```
2. **每 5 分钟执行一次**

   ```
   */5 * * * * command
   ```
3. **每天凌晨 2 点执行**

   ```
   0 2 * * * command
   ```
4. **每周一凌晨 3 点执行**

   ```
   0 3 * * 1 command
   ```
5. **每月 1 号和 15 号的凌晨 1 点执行**

   ```
   0 1 1,15 * * command
   ```

## 停止任务

`crontab` 任务是由 **cron** 守护进程调度的，所以“停止”它有几种方式，取决于你是要**临时**停止，还是**彻底删除**它。

### 1. 临时停止某个 crontab 任务（推荐）

如果你只是想暂停某个任务：

1. 编辑当前用户的 crontab：

   ```bash
   crontab -e
   ```
2. 找到你想停止的那一行任务，在前面加 `#` 注释掉：

   ```bash
   # 0 5 * * * /path/to/script.sh
   ```
3. 保存退出，任务就不会再执行了。

### 2. 永久删除某个任务

1. 编辑：

   ```bash
   crontab -e
   ```
2. 删除那一行。
3. 保存退出。

### 3. 停止所有当前用户的 crontab 任务

```bash
crontab -r
```

> ⚠ **危险**：这会直接清空当前用户的所有定时任务，不可恢复。

### 4. 停止 `cron` 服务（会影响系统中所有定时任务）

不同系统命令不同：

```bash
# systemd 系统
sudo systemctl stop cron

# 有些系统是 crond 服务
sudo systemctl stop crond
```

> ⚠ 不建议这么做，除非你确实不希望系统中任何 cron 任务运行。

