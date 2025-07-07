---
layout: default
toc: false
title: comfyui学习，视频，AI，动画制作
date:  2025-07-08T06:52:43+08:00
categories: ['']
draft: true
---


## 安装启动

可以 从 **桌面端** 或 **浏览器** 等方式打开 comfyUI

## 使用 (文生图)

下载某个模型，加载 **checkpoint**，

比如 [SD1.5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/tree/main) 或者 [Dreamshaper](https://civitai.com/models/4384?modelVersionId=128713)

把下载的模型放到 models 文件夹

```
📁ComfyUI_windows_portable                     // ComfyUI 官方便携版
├── 📁ComfyUI                                  // comfy UI主要文件夹
│  ├──📁 models                                // 模型安装文件夹
│  |  ├── 📁 checkpoints                       // SD 模型的安装位置
│  |  |   ├── 📁 SD1.5                         // 新建SD1.5 版本文件夹（不是必须，但后期随着你是用模型数量的增加，这个文件夹分类有助于你快速查找）
│  |  |   |   ├── dreamshaper_8.safetensors    // 下载到的模型文件
│  |  |   |   └── v1-5-pruned-emaonly.ckpt     // 下载到的模型文件                                      
```

输入提示词，然后进行文生成图像

## 局部重绘