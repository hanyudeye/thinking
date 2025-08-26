---
layout: default
toc: false
title: 网站，前端，front，网页，html
date:  2025-07-07T13:12:53+08:00
draft: true
---

# 前端简述

前端（html,css，javascript)， 它使用这 3个 技术 ，html,css两个技术 简化了 视觉显示 (用简化的代码就能形成样式），javascript 技术是功能执行的核心。

> 前端开发以 HTML 构建结构，以 CSS 美化样式，以 JavaScript 实现交互，是现代网站和Web应用不可或缺的基础。

# 交互式页面开发的一种方法

把 交互做成一个个小页面 进行条状
> 参考 https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/

https://jakearchibald.com/2024/view-transitions-handling-aspect-ratio-changes/


## UTM 参数    

 `utm_source` 是 **UTM 参数**（Urchin Tracking Module，来源追踪模块）的一部分，它用于 **跟踪网站流量来源**，通常在 URL 中以查询字符串的形式出现，用于分析网站的流量来源。

### **`utm_source` 参数的作用**：

- **跟踪流量来源**：`utm_source` 主要用来标识流量的来源，告诉你访问者是通过哪个渠道、平台或网站来到你的网站的。
- **分析营销效果**：它通常与其他 UTM 参数（如 `utm_medium`、`utm_campaign` 等）一起使用，帮助营销人员分析各种营销活动的效果，识别最有效的推广渠道。

### **常见的 UTM 参数**：
- **`utm_source`**：标识流量的来源（例如：google、facebook、newsletter等）。
- **`utm_medium`**：指定流量来源的媒介（例如：cpc（点击付费广告）、email（电子邮件）、social（社交媒体）等）。
- **`utm_campaign`**：指定特定的营销活动名称（例如：summer_sale、new_product_launch等）。
- **`utm_term`**（可选）：用于标识广告中使用的关键词。
- **`utm_content`**（可选）：用于区分广告内容，尤其是在A/B测试中非常有用。

### **例子**：

假设你在 **Facebook 广告** 上做了一次营销活动，并且想要跟踪通过这次广告访问你网站的流量，你可以在广告链接中加入 UTM 参数：

```
https://www.yoursite.com?utm_source=facebook&utm_medium=social&utm_campaign=spring_sale
```

- `utm_source=facebook` 表示访问者是从 **Facebook** 来的。
- `utm_medium=social` 表示流量是通过 **社交媒体** 传来的。
- `utm_campaign=spring_sale` 表示这次访问是由 **spring_sale**（春季促销）活动引发的。

### **`utm_source` 的常见用途**：
1. **广告投放**：当你通过 Google Ads、Facebook Ads 或其他广告平台投放广告时，可以使用 `utm_source` 来追踪流量来源。
2. **社交媒体营销**：使用 `utm_source` 来标识不同社交媒体平台（如 Facebook、Twitter、Instagram）上的流量来源。
3. **电子邮件营销**：在电子邮件营销中，`utm_source` 可以帮助追踪通过电子邮件链接访问网站的用户。
4. **合作伙伴推广**：如果你与其他网站或博主合作进行推广，可以使用 `utm_source` 来标记流量来源，以便了解每个合作伙伴的效果。

### **总结**：
`utm_source` 作为 UTM 参数的一部分，能帮助你 **准确追踪和分析流量来源**，了解你的广告、营销活动或其他推广渠道的效果。它是 **数字营销分析** 中不可或缺的工具之一，有助于优化营销策略
和提高投资回报率。

#### 1.5 **字体**
- sans-serif 无衬线字体 (字体圆润)
- 常用无衬线字体
  - Arial 是一种无衬线（sans-serif）字体
  - Helvetica
  - Segoe UI
  - Open Sans
  - Microsoft YaHei（微软雅黑）


- 有衬线字体（Serif fonts）
- 常用于书籍、报纸、正式文档标题等。
  - 常见有衬线字体
   - Times New Roman
   - Georgia
   - Garamond
   - 宋体（SimSun）在中文里也算有衬线

#### 1.6 **汉字竖排**
- writing-mode: vertical-rl; /* 从右到左的竖排 */
- text-orientation: upright; /* 每个字直立显示 */

