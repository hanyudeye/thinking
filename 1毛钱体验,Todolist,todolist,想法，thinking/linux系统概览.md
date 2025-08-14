---
layout: default
toc: false
title: linux源码解析
date:  2025-07-24T07:10:39+08:00
categories: ['']
draft: true
---


Linux 系统的整体运行流程可以大致分为以下几个阶段，每个阶段都有核心源码模块对应。下面我会 **先给出整体流程图式总结**，然后针对 **每个关键阶段做源码解析（基于 Linux 内核源码）**。

## **一、Linux 系统整体启动流程概览**

1. **Bootloader 阶段**

   * 典型工具：`GRUB`、`LILO`
   * 作用：加载内核镜像到内存，切换到保护模式，并跳转到内核入口地址。

2. **内核初始化阶段**

   * 核心步骤：

     1. 设置内核页表、内存管理
     2. 初始化中断、异常处理
     3. 初始化设备驱动、文件系统
     4. 挂载根文件系统

3. **启动第一个用户态进程 (`init`)**

   * `kernel_init()` 创建 PID 1 进程，加载 `/sbin/init` 或 systemd

4. **用户空间初始化**

   * 读取 `/etc/inittab` 或 systemd 单元文件
   * 启动基本服务、登录程序

5. **进入多用户运行级别**

   * 启动守护进程、网络服务、Shell

### **整体流程图：**

```
硬件上电 -> BIOS/UEFI -> Bootloader (GRUB) -> 加载内核 -> 内核初始化 ->
挂载根文件系统 -> 启动 init/systemd -> 用户空间服务 -> 登录 Shell
```

## **二、源码解析（基于 Linux 内核）**

### **1. 内核入口：`start_kernel()`**

* 文件位置：`init/main.c`
* 入口函数 `start_kernel()` 负责整个内核初始化流程。

关键源码片段（简化注释）：

```c
asmlinkage __visible void __init start_kernel(void)
{
    setup_arch(&command_line);   // 架构相关初始化（内存映射等）
    setup_command_line(command_line);
    mm_init();                   // 内存管理初始化
    sched_init();                // 调度器初始化
    init_IRQ();                  // 中断初始化
    timekeeping_init();          // 时钟初始化
    console_init();              // 控制台初始化
    rest_init();                 // 创建第一个进程
}
```

### **2. 第一个用户态进程：`rest_init()`**

* 文件位置：`init/main.c`
* 作用：启动 **PID 1 的 init 进程** 和内核线程 `kthreadd`。

源码片段：

```c
static noinline void __ref rest_init(void)
{
    kernel_thread(kernel_init, NULL, CLONE_FS);
    pid = kernel_thread(kthreadd, NULL, CLONE_FS | CLONE_FILES);
    schedule(); // 进入调度
}
```

这里 `kernel_init` 会最终调用 `run_init_process()`，尝试执行 `/sbin/init` 或 `systemd`。

### **3. init 进程的执行逻辑**

* 如果找不到 `/sbin/init`，会尝试 `/bin/sh`。
* 源码：

```c
static int run_init_process(const char *init_filename)
{
    return do_execve(getname_kernel(init_filename), (const char __user *const __user *)argv_init, envp_init);
}
```

### **4. 用户空间初始化**

* **Systemd** 或 **SysVinit**：

  * 挂载 `/proc` `/sys`
  * 启动基本守护进程（如 `udevd`）
  * 启动网络、图形界面

## **总结关键源码调用链**

```
start_kernel()
 ├── setup_arch()
 ├── mm_init()
 ├── init_IRQ()
 ├── console_init()
 └── rest_init()
      ├── kernel_init()
      │    └── run_init_process("/sbin/init")
      └── kthreadd
```
