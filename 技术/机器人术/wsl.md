# wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理。

要解决 **“检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理”**，核心方法是把 WSL2 网络从 **NAT 模式** 改为 **镜像模式（Mirrored Mode）**，让 WSL 与 Windows 共享 localhost 网络栈。

### 一、前提条件
- **Windows 11 22H2 及以上**
- **WSL2 版本 ≥ 1.2.0**
  检查版本（PowerShell / 终端）：
  ```powershell
  wsl --version
  ```
  如不是 WSL2：
  ```powershell
  wsl --set-default-version 2
  ```

### 二、方法 1：修改 .wslconfig（推荐）
1. 打开 **用户目录**：
   ```
   C:\Users\你的用户名\
   ```
   或在资源管理器地址栏输入：
   ```
   %UserProfile%
   ```
2. 新建/编辑文件：`.wslconfig`（无文件名前缀，直接 `.wslconfig`）
3. 写入：
   ```ini
   [wsl2]
   networkingMode=mirrored  # 核心：开启镜像模式
   autoProxy=true           # 自动同步 Windows 代理到 WSL
   dnsTunneling=true        # DNS 走 Windows 主机
   firewall=true            # 共用 Windows 防火墙
   ```

4. 重启 WSL 生效（PowerShell）：
   ```powershell
   wsl --shutdown
   wsl
   ```

### 三、方法 2：WSL 设置界面（新版 Windows）
1. Win+Q 搜索：**WSL 设置 / WSL Settings**


2. 进入 **网络（Network）**
3. 把 **网络模式** 从 **NAT** 改为 **镜像（Mirrored）**
4. 保存 → 重启 WSL

### 四、验证是否生效
1. 启动 WSL，不再出现代理提示
2. WSL 内直接访问 Windows 代理：
   ```bash
   # 示例：Windows 代理在 127.0.0.1:7890
   curl --proxy http://127.0.0.1:7890 https://www.google.com
   ```
3. 或自动设置环境变量（~/.bashrc / ~/.zshrc）：
   ```bash
   export http_proxy=http://127.0.0.1:7890
   export https_proxy=http://127.0.0.1:7890
   export no_proxy=localhost,127.0.0.1
   ```

### 五、常见问题
- **仍无法连接代理**
  - 确认 Windows 代理软件允许 **LAN/本机** 连接（关闭“仅本机”限制）
  - 检查 Windows 防火墙是否放行代理端口（如 7890）
- **镜像模式后网络变慢/不稳定**
  - 可临时注释 `networkingMode=mirrored` 改回 NAT
  - 或用 **NAT 模式手动指定 Windows IP**（`ipconfig` 看以太网/WLAN IPv4）：
    ```bash
    export http_proxy=http://192.168.1.100:7890
    ```

---

需要我帮你生成一段 **自动检测 Windows IP 并在 WSL 里设置代理的脚本**（加到 .bashrc 永久生效）吗？

互联网企业为了合规报送涉税信息是什么