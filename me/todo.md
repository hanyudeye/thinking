---
layout: default
toc: false
title: todo
date:  2026-05-29T10:13:39+08:00
categories: ['']
draft: true
---

- 删除 订阅，慢慢学习 语言（英语，日语），读懂新闻内容，并减少内容输入

# todo 做 X 账号，做博客总结，附上博客链接

给我一个能 总结网页内容并能发布到 X 的提示词，我没有开会员，而且X博文能插入网页链接吗

可以。
X（原 Twitter）当然能插入网页链接，而且：

```text id="m2thhs"
直接粘贴 URL 即可
```

X 会自动：

* 抓标题
* 抓摘要
* 抓预览图（Open Graph）

所以很多 AI 内容号都是：

```text id="3n38w9"
总结 + 评论 + 链接
```

这种模式。

---

# 适合你的 Prompt（核心版）

你可以直接给：

* ChatGPT
* Claude
* Gemini
* 本地模型

使用。

---

# 通用网页总结 + X发帖 Prompt
请把下面内容改写成适合 X（Twitter）发布的中文短帖：

要求：
1. 信息密度高
2. 有传播感
3. 不像营销号
4. 控制在 120 字左右
5. 保持真人表达感


```text id="9efx9g"

你是一个专业科技/效率/AI 自媒体编辑。
请把网页内容改写成适合 X（Twitter）发布的中文短帖：
请完成：

1. 提炼最值得普通人关注的信息
2. 不要像 AI 总结
3. 用“真人分享”的口吻
4. 输出适合 X（Twitter）的短内容
5. 保持信息密度高
6. 开头必须吸引人
7. 不要废话
8. 不要营销腔
9. 输出：
   - 1条主推文
   - 3个不同风格版本
   - 1个标题
   - 5个标签（hashtags）
10. 最后附上原网页链接

风格参考：
- Hacker News
- Reddit 高赞评论
- 独立开发者
- AI 工具博主

内容要：
- 有观点
- 有信息差
- 有“我想转发”的感觉



我会给你一篇网页内容。

请完成：

1. 提炼最值得普通人关注的信息
2. 不要像 AI 总结
3. 用“真人分享”的口吻
4. 输出适合 X（Twitter）的短内容
5. 保持信息密度高
6. 开头必须吸引人
7. 不要废话
8. 不要营销腔
9. 输出：
   - 1条主推文
   - 3个不同风格版本
   - 1个标题
   - 5个标签（hashtags）
10. 最后附上原网页链接

风格参考：
- Hacker News
- Reddit 高赞评论
- 独立开发者
- AI 工具博主

内容要：
- 有观点
- 有信息差
- 有“我想转发”的感觉
```

---

# 更适合中文 X 的版本

如果你主要发中文：

```text id="6j2kp6"
请用中文输出。

风格：
- 简洁
- 有洞察
- 不像公众号
- 不要鸡汤
- 不要“震惊”
- 不要过度夸张

控制在：
- 80~220字

优先突出：
- 为什么值得关注
- 为什么普通人会受益
- 为什么这个东西有意思
```

---

# 一个非常重要的技巧

不要：

```text id="jlwm01"
“总结全文”
```

而要：

```text id="jlwm02"
“提炼一个最值得传播的点”
```

因为 X 是：

```text id="jlwm03"
观点平台
```

不是博客平台。

---

# 举个例子（正确方向）

假设网页是：

```text id="jlwm04"
“某 AI 工具支持自动生成 PPT”
```

差的 AI 输出：

```text id="jlwm05"
这个工具可以帮助用户提高效率...
```

没人看。

---

好的输出会像：

很多人还在手动做 PPT。

现在已经能：
输入一句话 → 自动生成完整演示文稿。

更关键的是：
它不是“模板替换”，而是真的会组织内容结构。

AI 正在吃掉大量“办公体力活”。

[https://example.com](https://example.com)

#AI #效率工具 #ChatGPT

---

# 你最适合的方向

你其实非常适合：

```text id="jlwm06"
“信息过滤型账号”
```

即：

* 我帮你发现值得看的东西
* 我帮你节省时间
* 我帮你提炼重点

而不是：

```text id="jlwm07"
纯原创人生IP
```

---

# 推荐你的自动化流

非常适合：

```text id="jlwm08"
RSS → AI总结 → X发布
```

---

# 技术栈（很成熟）

## 1. RSS 抓取

### [RSSHub](https://rsshub.app?utm_source=chatgpt.com)

---

## 2. 自动化

### [n8n](https://n8n.io?utm_source=chatgpt.com)

---

## 3. AI总结

调用：

* OpenAI API
* Claude API
* Gemini API

---

## 4. 自动发 X

X 官方 API：

[X Developer Platform](https://developer.x.com?utm_source=chatgpt.com)

---

# 一个现实问题

很多人以为：

```text id="jlwm09"
自动化 = 自动赚钱
```

实际上：

```text id="jlwm10"
真正难的是“筛选什么值得发”
```

所以你更应该训练：

* 信息嗅觉
* 标题感
* 什么值得转发

而不是疯狂生成。

# chrome 浏览器开启 genimi

1. 找到这个文件：

C:\Users\你的用户名\AppData\Local\Google\Chrome\User Data\Local State

2. 备份

3. 找到这三个字段并修改：

"is_glic_eligible": true
"variations_country": "us"

// 注意这一项不是把值完全改成us，是把国家简称改成us
"variations_permanent_consistency_country": "us"
如果找不到就手动加进去，注意JSON格式别写错。

保存，关闭。

第五步：重启Chrome

重新打开浏览器，右上角应该就能看到Gemini图标了。

## 自媒体

# 现在主流 AI 内容工厂结构

基本都是：

```text
热点抓取
    ↓
选题筛选
    ↓
AI生成脚本
    ↓
AI生成标题
    ↓
AI生成封面
    ↓
自动发布
```

---

# 我推荐你看的几个方向

---

# 1. 自动抓热点

## GitHub Trending

[GitHub Trending](https://github.com/trending?utm_source=chatgpt.com)

适合：

* AI工具号
* 程序员号
* 科技号

---

## Hacker News

[Hacker News](https://news.ycombinator.com?utm_source=chatgpt.com)

很多科技博主内容源头。

---

## Reddit

[Reddit](https://www.reddit.com?utm_source=chatgpt.com)

真正的大量选题来源。

例如：

* r/ChatGPT
* r/SideProject
* r/selfhosted
* r/productivity

---

# 2. 自动生成脚本工具

## [Dify](https://dify.ai?utm_source=chatgpt.com)

目前非常适合：

```text
低代码 AI 工作流
```

你可以做：

* 自动生成短视频文案
* 自动总结热点
* 自动翻译
* 自动改写

很多 AI 工作流博主都在用。

---

## [Flowise](https://flowiseai.com?utm_source=chatgpt.com)

LangChain 可视化版。

适合：

* 本地部署
* 自动 Agent

---

# 3. 自动发布系统

## [n8n](https://n8n.io?utm_source=chatgpt.com)

这个非常强。

你可以：

```text
RSS → GPT → 自动发推特/公众号/Notion
```

很多 AI 内容农场核心就是它。

---

# 4. 一键生成视频

## [CapCut](https://www.capcut.com?utm_source=chatgpt.com)

现在大量 AI 自媒体：

* 配音
* 字幕
* 剪辑

都用它。

---

## [HeyGen](https://www.heygen.com?utm_source=chatgpt.com)

AI数字人。

很多“AI讲新闻”账号用它。

---

# 真正重要的部分：选题

AI 最大的问题：

```text
不会判断什么值得发
```

---

# 什么内容容易火

你现在应该优先做：

---

## A. “低信息差”

例如：

```text
3个99%的人不知道的网站
```

```text
Windows隐藏效率技巧
```

```text
ChatGPT还能这么用
```

---

## B. “强实用”

例如：

* 免费资源站
* AI工具
* 自动化
* 翻译
* 学英语

---

## C. “情绪价值”

例如：

* 打工人
* 孤独
* 赚钱焦虑
* 普通人生活

这种在小红书/抖音很强。

---

# 你目前最大优势

其实是：

```text
你会主动研究工具
```

很多人根本不会。

你聊天记录里已经有很多可做内容：

* WSL
* Emacs
* AHK
* AI工具
* 翻译
* 投资
* 英语
* 离线知识库

这些都能做。

---

# 我不建议你做的

## 1. 纯 AI 洗稿

现在已经严重过剩。

---

## 2. 新闻搬运

版权+平台限流严重。

---

## 3. 鸡汤

竞争太大。

---

# 最推荐你的路线

## “工具 + 效率 + AI”

因为：

* 生命周期长
* 可积累
* 可多平台分发
* 不依赖真人出镜

---

# 一个现实情况

真正赚钱的 AI 自媒体：

```text
不是靠内容本身
```

而是：

* 卖课
* 卖社群
* 接广告
* Affiliate
* 软件分销
* 知识付费

内容只是流量入口。

---

# 如果你愿意，我还能继续帮你：

* “一个人 AI 内容工厂完整方案”
* “GitHub 上真正能用的 AI 自媒体项目”
* “自动抓热点 + 自动生成文案”
* “适合普通人的 10 个 AI 账号方向”
* “低成本 AI 视频流水线”
* “适合中文平台的内容结构”
* “如何判断什么选题会火”
* “如何避免 AI 味太重”
