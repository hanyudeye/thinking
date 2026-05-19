看书，或pdf，或一个网页 ,系统学习

1. 每个学习周期，看一页书 (25分钟) ,这是合理的学习任务，能按时完成

2. 戴耳机隔离噪音


## 2026-05-02

- [x] 周期1 输入输出
- [x] 周期2 学会使用gptel 进行终端问问题 (这样就可以减少打开网页)，但终端不智能呀，还是要想办法
- [x] 周期4 查看有关 shell 的网页
- [x] emacs 中有什么快捷键可以直接选中一行 , can use ~v j~ do it
- [x] thinking: 为自己的困难找借口是 没有成长吗？ 困难的种类 是的，任何困难都是人解决的，解决的程度看自己的态度
- [x] put translation window to 0.2 
- [x] 周期3 编程往后面再看一页，下一页(page 6)讲的是一些函数的概念说明，不是很复杂，但看着很枯燥还是什么
- [x] 修改tmux底部右侧状态栏的显示 set -g status-right "%H:%M"
- [x] page7 提出了stream 流的 abstract conception 抽象 概念，和函数接近，提供一些东西，会产生另一种东西，这个东西就是不同类型的流，语言开发者创造这种抽象可能是为了给 语言使用者 更方便的使用吧
- [x] page8-9 注释的作用是 作为编码的文档，辅助说明或概括说明编码的用途
- [x] page 10-16 控制结构，分支/重复，分支使功能更灵活，有一种智能感
- [x] page 17-29 类，模块化，工程化，规范
- [x] page 30-68 变量 vars ，可以变化的数据，这种数据一般作为中转吧，maybe,so you can use it to do some operation,like mathematical computation。高级语言的发明者，为了实现自然语言编程，已经做了很多的工作，例如做出图形程序，更容易让计算机知道你的用途，而那些各种应用库的创造者，创造了很多有用的库，所以现在编程已经非常简单了，只要引入库，直接使用，就像搭积木，或购买零件一样
- [x] page 69-95 使用库 iostream , vector ,..
- [x] page 96-120 数组和指针 , 指针是机器相关的对象，表示对象所在的内容地址，因为自然语言中不会用到，但写论文的时候，有一个引用符号，或者网页链接/桌面快捷方式，所以指针一般用于引用，跟变量意思差不多，但因为指针也是一个数字，以前可能会用于计算，但现在都不推荐使用了，因为要很小心
- [x] 表达式：数学计算的表达式，语言科学家把它复用于 数学计算
- [x] page 196: 函数，也是为了规范，把一个<计算机执行功能> 集中到一个块中，组合成库后就可以很方便地复用
- []


在 **完全断网（无外网、无局域网）** 环境下，WSL 与 Windows 仍可通过 **虚拟网卡（Hyper-V 内部网络）** 互相访问服务。核心是利用两者之间默认存在的 **虚拟私有网络**，无需依赖物理网卡或外部网络。

### 一、原理：WSL2 默认 NAT 虚拟网络
WSL2 本质是轻量级虚拟机，默认使用 **NAT 网络模式**：
- Windows 主机：虚拟网关 IP（通常 `172.x.x.1`）
- WSL2 实例：虚拟子网 IP（通常 `172.x.x.x`）
- 两者**始终连通**，与外部网络无关

### 二、方案 1：NAT 模式（默认，无需改配置）
#### 1. Windows → 访问 WSL 服务
**方法 A：localhost 自动转发（推荐）**
WSL 默认开启 `localhostForwarding`：WSL 监听 `0.0.0.0:端口` 或 `127.0.0.1:端口` 的服务，Windows 直接用 `localhost:端口` 访问。
- 验证（WSL内）：确保服务监听 `0.0.0.0`
  ```bash
  # 示例：Python 简易服务器（监听所有地址）
  python3 -m http.server 8080 --bind 0.0.0.0
  ```
- Windows 访问：`http://localhost:8080`

**方法 B：用 WSL 虚拟 IP**
Windows 终端（管理员）查 WSL IP：
```powershell
wsl hostname -i
# 输出示例：172.27.63.123
```
访问：`http://172.27.63.123:8080`

#### 2. WSL → 访问 Windows 服务
**关键：用 Windows 虚拟网关 IP**
WSL 内执行：
```bash
# 获取 Windows 主机IP（虚拟网关）
ip route show | grep default | awk '{print $3}'
# 输出示例：172.27.63.1
```
访问 Windows 服务：
```bash
curl http://172.27.63.1:8080  # 替换为你的端口
```

**防火墙放行（必做）**
Windows 防火墙默认拦截 WSL 访问：
- 临时放行（管理员 PowerShell）：
  ```powershell
  New-NetFirewallRule -DisplayName "WSL2 Access" -Direction Inbound -Action Allow -RemoteAddress 172.16.0.0/12 -Profile Any
  ```
- 或：关闭专用网络防火墙（仅本地安全）

### 三、方案 2：镜像网络模式（Win11 22H2+，双向 localhost）
**最推荐（无网环境最稳）**：共享 `localhost`，彻底打通。
1. 新建/编辑 `C:\Users\你的用户名\.wslconfig`
   ```ini
   [wsl2]
   networkingMode=mirrored  # 镜像模式
   localhostForwarding=true # 自动转发
   ```
2. 重启 WSL（管理员 PowerShell）
   ```powershell
   wsl --shutdown
   ```
3. 无网环境下：
   - Windows ↔ WSL 都用 `localhost:端口` 互访
   - IP 完全一致，无需查 IP、无需防火墙规则

### 四、方案 3：端口转发（兼容旧版 Win10）
Windows 端口转发（断网也生效）：
```powershell
# 监听 Windows 0.0.0.0:8080 → 转发 WSL 172.27.63.123:8080
netsh interface portproxy add v4tov4 listenport=8080 listenaddress=0.0.0.0 connectport=8080 connectaddress=172.27.63.123
```

### 五、无网环境必做：关闭外部依赖
1. **服务绑定 `0.0.0.0`**（不要仅绑 127.0.0.1）
2. **Windows 防火墙放行 WSL 虚拟网段**（`172.16.0.0/12`）
3. **禁用代理/VPN**（避免干扰虚拟网络）
4. **用镜像模式**（Win11）：彻底告别查 IP

### 六、快速验证（断网下）
1. WSL 起服务：`python3 -m http.server 8080 --bind 0.0.0.0`
2. Windows 访问：`http://localhost:8080`
3. Windows 起服务（如 VS Code Live Server: 5500）
4. WSL 访问：`curl http://172.x.x.1:5500`（NAT）或 `curl http://localhost:5500`（镜像）

**结论**：无网时 **镜像模式（Win11）** 最优；旧版用 **NAT + 虚拟IP + 防火墙放行**。两者都不依赖外部网络，纯虚拟互通。

要不要我帮你写一段一键脚本，自动获取 Windows 虚拟 IP 并配置防火墙规则？kj

