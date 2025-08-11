---
layout: default
toc: false
title: javascript
date:  2025-08-04T14:38:47+08:00
draft: true
---

# 当前前端所用技术，及其详细来源和应用

我们来系统梳理一下**当前前端所用的主要技术**，它们的**历史来源**以及**实际应用场景**。
我会按 **基础 → 框架 → 工具链 → 新兴趋势** 的顺序讲，方便你有一个完整脉络。

---

## 1. 基础层技术

| 技术                                   | 详细来源                                                 | 核心应用                                  |
| ------------------------------------ | ---------------------------------------------------- | ------------------------------------- |
| **HTML (HyperText Markup Language)** | 1991 年由 Tim Berners-Lee 提出，是万维网的标记语言标准，W3C/WHATWG 维护 | 用来定义网页结构和语义，例如标题、段落、表格、表单等            |
| **CSS (Cascading Style Sheets)**     | 1996 年由 Håkon Wium Lie 提出，W3C 标准化                    | 控制网页样式、布局、动画（现代支持 Flexbox、Grid 等高级布局） |
| **JavaScript (JS)**                  | 1995 年 Brendan Eich 在网景公司开发，最初叫 LiveScript           | 提供网页交互、逻辑处理、DOM 操作、事件监听、AJAX 等        |

💡 **应用场景**：
任何 Web 页面都离不开 HTML（骨架）、CSS（外观）、JavaScript（行为）——这是前端的“三驾马车”。

---

## 2. 框架与库（提高开发效率）

| 技术          | 详细来源                                             | 核心应用                                     |
| ----------- | ------------------------------------------------ | ---------------------------------------- |
| **jQuery**  | 2006 年 John Resig 发布                             | 简化 DOM 操作、事件绑定、AJAX 调用；现在用得少，但仍在一些老项目中存在 |
| **React**   | 2013 年 Facebook 发布                               | 基于组件化思想和虚拟 DOM，实现高效 UI 渲染；适合大型单页应用（SPA）  |
| **Vue.js**  | 2014 年尤雨溪发布                                      | 渐进式框架，数据驱动视图，学习曲线低，广泛用于中小型和大型项目          |
| **Angular** | 2010 年 Google 发布（AngularJS），2016 年重写为 Angular 2+ | 完整框架，内置路由、表单、依赖注入等                       |
| **Svelte**  | 2016 年 Rich Harris 发布                            | 编译型框架，无运行时开销，生成更小更快的原生 JS                |

💡 **应用场景**：

* **React**：大公司后台、复杂 UI、跨平台（React Native）
* **Vue**：国内业务型项目、小程序（uni-app）、CMS
* **Angular**：企业级管理系统
* **Svelte**：轻量高性能场景、嵌入式 UI

---

## 3. 工具链与构建系统

| 技术             | 详细来源                         | 核心应用                        |
| -------------- | ---------------------------- | --------------------------- |
| **Webpack**    | 2012 年 Tobias Koppers 发布     | 模块打包、代码分割、热更新               |
| **Vite**       | 2020 年尤雨溪发布                  | 基于 ES Module，开发启动极快，支持现代浏览器 |
| **Babel**      | 2014 年 Sebastian McKenzie 发布 | 将 ES6+ 转译为兼容旧浏览器的 JS        |
| **ESLint**     | 2013 年 Nicholas C. Zakas 发布  | 代码风格与质量检查                   |
| **TypeScript** | 2012 年微软发布                   | 为 JS 添加静态类型系统，提高可维护性        |

💡 **应用场景**：

* Webpack/Vite 用于打包优化和本地开发
* Babel 确保浏览器兼容性
* ESLint/Prettier 保证代码一致性
* TypeScript 在大型项目几乎是标配

---

## 4. 新兴趋势与扩展技术

| 技术                            | 详细来源                   | 核心应用                            |
| ----------------------------- | ---------------------- | ------------------------------- |
| **Next.js**                   | 2016 年 Vercel 发布       | React 服务端渲染（SSR）、静态生成（SSG）、全栈功能 |
| **Nuxt.js**                   | 2016 年发布               | Vue 的 SSR/SSG 框架                |
| **Tailwind CSS**              | 2017 年 Adam Wathan 发布  | 原子化 CSS，快速构建一致 UI               |
| **WebAssembly**               | 2017 年 W3C 发布          | 在浏览器运行接近原生性能的代码（C/C++/Rust 转译）  |
| **PWA (Progressive Web App)** | Google 推广              | 让网页支持离线、消息推送、安装到桌面              |
| **微前端（Micro Frontends）**      | 2016 年 ThoughtWorks 提出 | 将前端拆分为多个独立可部署模块                 |

💡 **应用场景**：

* **Next.js/Nuxt.js**：SEO 要求高、性能优先的站点
* **Tailwind CSS**：设计一致性、快速开发
* **WebAssembly**：视频处理、3D 渲染、数据计算
* **PWA**：移动端增强体验
* **微前端**：大型企业多个团队协作

---

## 5. 生态补充

* **NPM / Yarn / pnpm**：包管理工具
* **Node.js**：JS 运行环境，让前端能写服务端逻辑
* **CI/CD 工具（GitHub Actions、Jenkins）**：自动化构建与部署
* **小程序框架（Taro、uni-app）**：多端统一开发

---

如果你愿意，我可以帮你画一张**前端技术演进时间轴**，从 1991 年的 HTML 到 2025 年最新趋势，这样你能一眼看到技术来源与发展脉络。这样会比文字更直观。

你是想要我直接画这个时间轴吗？



# 包装信息
## package.json 与 package-lock.json

- package.json 描述项目的基本信息、依赖与版本、脚本 (非精确版本号，而是版本范围)
- package-lock.json 锁定项目，记录所有包的精确版本信息

尽量通过 npm install [package-name]@[version] 来安装套件，这样可以确保 package.json 中的版本范围与 package-lock.json 中的版本一致。

package-lock.json 档案应该加入 Git 版控，避免任何人可以更新

对于依赖冲突，可以删除 package-lock.json

对于过时的包，可以手动删除 pakcage.json 文件内的包，然后安装新的包，避免 **npm uninstall  包** 的时候依赖报错。
