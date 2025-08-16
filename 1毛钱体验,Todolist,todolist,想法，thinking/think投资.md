---
layout: default
toc: false
title: 投资
date:  2025-08-11T07:06:17+08:00
categories: ['']
draft: true
---

# 基本准则

- 看公司基本面，PE低，市价 是否符合 公司价值，盈利情况
- 迅速投入，不要等低价，持续投入，不断判断投入价值

# 我的配额比率:
* 7  VOO 4 QQQM 3  (定投吃利息)
* 3 个股 (低价好股涨利润，不要买热门股，那也是吃利息，买低价的，涨回去后卖掉特斯拉)
* 1 现金

现在是牛市，少买点，保留 50% 现金？需要等待熊市吗？
> 不需要等熊市，会踏空，失败率很高。保留 10%等回调加仓
> 根据工资收入，每月投600，留2000$，用于回调，不要等熊市了。 
其他低价的，有空再研究
没有熊市，当前就是最低点，短期熊市(1-几个月）迅速加仓。

| 时间 |      金额      |                   想法                   |
| :--- | :------------: | :--------------------------------------: |
| 9月  | SPMO股票5张117 | 因为是跟踪科技头部的，涨的会快些，但不稳 |
|8月|QQQM 3张，英伟达 买2张|英伟达一直涨，而且AI是发展趋势|

# AI 看财报

- ftnt 8月6号的财报概览
- xx 最近财报概览

# 期权

## 引言

本文将详细介绍如何判断期权合约的买卖方向，以及如何区分开仓和平仓。内容参考自 [Unusual Whales 官方文档](https://unusualwhales.com/information/how-to-interpret-types-of-option-transactions)。

## 期权交易的四种基本方式

**你可以通过四种方式交易期权合约：**

-   买入看涨期权（买价方向/在买价）
-   卖出看涨期权（卖价方向/在卖价）
-   买入看跌期权（买价方向/在买价）
-   卖出看跌期权（卖价方向/在卖价）

假设你看好 ABC 公司，可以买入看涨期权。平仓时卖出该看涨期权。若你看空 XYZ 公司，可以买入看跌期权，平仓时卖出该看跌期权。

> 你可以观看 Unusual Whales 的 [期权交易的四种方式](https://www.youtube.com/watch?v=9g74rfdEILA) 视频，了解更详细的讲解和实际 Flow Feed 示例。

## 期权交易的四种类型

1.  买入看涨期权
2.  卖出看涨期权
3.  买入看跌期权
4.  卖出看跌期权

### 买入合约

-   买入开仓（BTO）
-   买入平仓（BTC）

### 卖出合约

-   卖出开仓（STO）
-   卖出平仓（STC）

“开仓"和"平仓"这两个短语为交易增加了更多含义和背景。每一笔期权交易都会是"开仓"或"平仓"之一。

“买入开仓"指的是交易者为自己买入一个新头寸（无论是看涨还是看跌）。当交易者准备卖出（或平仓）时，就是"卖出平仓”。

“卖出开仓"指的是交易者开一个新头寸，但站在空方。比如卖出（或写）备兑看涨/现金担保看跌就是"卖出开仓"交易。要平掉"卖出开仓"的头寸，你需要"买入平仓”。

如何判断一笔交易更可能是买入还是卖出？看买卖价差的哪一侧。

Side（方向）是你会在Unusual Whales flow feed中看到的一个表头。它通常用来指明一笔交易在买卖价差中的位置。你可以通过阅读[这篇文章](https://unusualwhales.com/information/how-is-the-side-of-the-trade-determined-in-the-flow)了解更多关于"方向"的信息。

![Image 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc4uI0Zuxxa-pJ1k13Bp95elu0vKunfRj9idGOVEKskNQ8ySTaAYuqJDswq8Ye2S1kDUZsJHdbAmXOwy6LW-TYkluyGArcO1JQh8x71SgtdJI0nFXlQxWpcltwqGmEwNNBmwXEhAGLCamz7gQ0C_X04aUbE?key=WKASwVLK7h_TndCyb3ltig) 每笔交易都会被标记方向。共有四种可能的方向：

-   **Ask（买价）** - 在买价或更接近买价成交的交易会被标记为ASK。
-   **Bid（卖价）** - 在卖价或更接近卖价成交的交易会被标记为BID。
-   **Mid（中间价）** - 恰好在买卖价差中间成交的交易会被标记为MID。
-   **None（无）** - 前三种标签是指交易在买卖价差中的位置。NONE标签用于买卖价差无关紧要的情况，比如对敲、顺序外或延迟的交易，或被修改或取消的交易。

**需要注意的是：在买价成交并不保证一定是买入，在卖价成交也不保证一定是卖出，只是概率更高而已。后续文章会详细讲解如何判断，但请注意这些知识并不能保证100%准确。**

为什么这些很重要？

理解这些概念对任何想要分析资金流向，尤其是想跟踪"异常期权流"的交易者来说都至关重要。

区分"开仓"和"平仓"交易的难点在于它们并没有明确标注。

比如，一个交易者买入（平仓）100万美元的（备兑）看涨期权，这和另一个交易者买入（开仓）100万美元的看涨期权在表面上看起来很像，但两者的市场情绪却截然不同。

下面我们会举一些"开仓"和"平仓"流动的清晰与不清晰分析的例子。

## 实例解析

### 买入开仓流动

![Image 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXed67MamR4K9dSnivk2x0h53pa3micvZKSCp0GduF83DNX24RVTMYLI0FEiyQFAm9GU93RzIL59h9JJjftaG51XyroII_SDEZk3vHOYpcIDuYDHOBnAjW0EPvZCfmcHge8s4IbuIsYnVdA7Fe7u3FBE8Tbc?key=WKASwVLK7h_TndCyb3ltig) 这里我们看到多笔订单在买价或接近买价成交。以[$EVA](https://unusualwhales.com/stock/EVA/overview?) $0.5C 03/15/2024为例，该合约的买卖价差为$0.15 - $0.20。右侧显示成交价为$0.20，正好在买价。此外，订单数量为470张，而未平仓合约数为0。因此我们知道这是开仓交易（订单量 > 当日总成交量 + 未平仓合约数）。

下方是接近买价成交的开仓例子。以[$CRON](https://unusualwhales.com/stock/CRON/overview?) $4C 1/16/2024为例，买卖价差为$0.25 - $0.35，成交价为$0.33。虽然不是正好在买价，但距离买价远比卖价近；同样，订单量大于当日总成交量和未平仓合约数之和，因此我们也能判断为开仓。

这两笔交易都可能代表看涨情绪。但请注意，这不是精确科学。在买价或接近买价成交并不保证一定是买入，只是概率更高。

### 卖出开仓流动

![Image 4](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfpRr5lhDZNvm9OrrvcUCbbzvh14E7xUHHeCM4RIFVCubf33s7Pqe1W_1OAygrZ2np5bwiI4fpgkerE7xH9WRtSqTzSg26GpR83o39rS-pqJTOPiJf4BCgP92maRIlda1itEU4AAc4Bvv4Qrmksl4qm8dJF?key=WKASwVLK7h_TndCyb3ltig) 判断"卖出开仓"交易的方法和"买入开仓"类似，只不过我们要找的是在卖价或接近卖价成交的交易。以[$CHWY](https://unusualwhales.com/stock/CHWY/overview?) $21.5P 2/2/2024为例，买卖价差为$2.45 - $2.49，成交价正好在卖价$2.45。订单量为175张，未平仓合约数仅67张，且订单量大于当日总成交量和未平仓合约数之和，因此可以判断为开仓。

再看[$LLY](https://unusualwhales.com/stock/LLY/overview?) $617.5P 2/2/2024，买卖价差为$8.15 - $8.80，成交价为$8.20，虽然不是正好在卖价，但考虑到价差较大，已经很接近卖价。同样，订单量大于当日总成交量和未平仓合约数之和，因此也可以判断为开仓。

### 买入平仓

![Image 5](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdGEVIaUA9yk3ZBtWobSM8lMhvdokNzTfbf_nzkB3BBjldTgMu7xun4vy4rXFA0Y6AqvgG1F3BFy6uBL8z09e8gwZNXMWPIK_fqEDJUw4hzEThx533RfocUUNNgmRPKbpEpNFKKJFBy2YOKotN_n5ZaDEE?key=WKASwVLK7h_TndCyb3ltig) 买入平仓的流动和买入开仓类似，只不过这里需要有未平仓合约——只有存在头寸，才有平仓。以[$AAPL](https://unusualwhales.com/stock/AAPL/overview?) $185P 12/29/2023为例，11/16有1.75万张合约大多在卖价成交，11/17未平仓合约增加近1.6万张。该头寸持有两周，直到12/13我们注意到合约在买价成交，成交量几乎与最初建仓时相同。第二天，12/14，未平仓合约大幅下降，证实了部分头寸被平掉。

### 卖出平仓

![Image 6](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOkGPqgnnTnixE88TS5WhKRxFPUvCdcpj3JbM5nrwxnOm1tAVT8f1E8Q_mlSuKGeEl53RV7ujF7eymV-9qiZpgG6vEf4No-G6lO35qdazEP_AWbGICUrWd40MAHrikYhVHVOTruPE72WiABd5cOHWaok4?key=WKASwVLK7h_TndCyb3ltig) 卖出平仓和买入平仓一样，需要有未平仓合约。以[$SPR](https://unusualwhales.com/stock/SPR/overview?) $23C 11/17/2023为例，11/10有5066张合约在卖价$1.46成交，而未平仓合约有10078张。5066张的成交量正好在卖价。我们无法在当天确认是否平仓，需等第二天开盘前未平仓合约更新。结果显示，11/13未平仓合约减少了2324张，证实了部分头寸被平掉。

## 相关文章

-   [期权合约图表解析](https://unusualwhales.com/information/breaking-down-an-option-contract-chart)
-   [如何查看和使用未平仓合约浏览器](https://unusualwhales.com/information/how-to-check-and-use-the-open-interest-explorer)

## 结语

理解期权交易的类型和流向，有助于更好地分析市场情绪和资金流动。希望本文对你有所帮助。

> 原文出处：[How To Interpret Types of Option Transactions - Unusual Whales](https://unusualwhales.com/information/how-to-interpret-types-of-option-transactions)

_非投资建议，仅供学习交流_

___

# 如何 在 reddit 社区找到最近的热门 优质股票

在 Reddit 社区寻找“最近热门的优质股票”可以通过多种方法结合使用来发掘可能的机会。以下是一些常见策略与工具，以及使用它们时的注意点：

## 1. 关注相关的 Subreddits

### **r/wallstreetbets（WSB）**

* 最出名的“梗股”社区，以高风险、高波动和“羊群效应”著称，曾引发 GameStop 效应。([维基百科][1])
* 这里的讨论往往聚焦于短期炒作，追求快速涨幅，公司基本面很少受到重视。

### **r/stocks / r/StockMarket / r/investing / r/pennystocks**

* **r/stocks**：一般讨论股票新闻、买点、投资建议等，适合跟踪讨论热度和观点。([Reddit][2])
* **r/StockMarket**：更偏向交易思路、技术分析、日常市场解读。([Reddit][3])
* **r/investing**：注重的是价值投资思路、长期潜力、公司基本面分析。([Reddit][4])
* **r/pennystocks**：专门讨论 <\$5 的高风险小盘股，但风险提示很明确。([Reddit][5])

---

## 2. 利用外部工具追踪 Reddit 热度

### **ApeWisdom**

* 这类工具可以量化 Reddit 上的讨论热度，比如多个 subreddit（如 WSB、r/stocks 等）中某个股票被提及的频率。适合判断哪些 ticker 正在“发酵”。([apewisdom.io][6])

### **AltIndex**

* 专门追踪 Reddit 上股票提及量，当某支股票突然热起来，它能推送通知，帮助你及时捕捉讨论热度上升。([Reddit][7])

---

## 3. 根据社区建议总结实用方法

下面是 Reddit 用户常分享的实际做法，摘录如下：

> “Go to any website that has ‘most active’ stocks for the day… Sort by most active… biggest gain %, biggest drop %.”
> — 来自 r/wallstreetbets ([Reddit][8])

> “Join as many stock related subreddits as you can and once you start seeing a stock being talked about in more than one, do your DD and determine if it’s actually a company you want to invest in.”
> — 来自 r/TheRaceTo10Million ([Reddit][9])

这说明一个实用思路：**交叉验证**。当某只股票在多个社区持续被讨论时，可能值得进一步了解其基本面、消息面或技术面是否支持后续走势。

---

## Meme Stocks（梗股）的判别标准与风险提示

近期 Reddit 论坛中，Krispy Kreme 和 GoPro 等股票再次成为“梗股”——它们在短期内迎来暴涨，但之后往往快速回落。([The Economic Times][10], [金融时报][11])

**特征可参考来自 Business Insider 的总结**：

1. 有吸引人的故事（pop-culture、反叛叙事）
2. 社交媒体热度持续上升
3. 高做空比例（short interest 高，有可能发生挤压）
4. 期权交易量激增
   比如 American Eagle Outfitters 曾被 AI（ChatGPT）判断具备梗股潜质，因其广告引发线上热度、做空和期权活跃等因素。([Business Insider][12])

**注意风险**：这类股票波动极大、短期买卖频繁，不少 Reddit 用户也坦言这种做法“更像是投机而非投资”。([市场观察][13], [The Economic Times][10])

---

## 总结策略清单

| 方法渠道               | 操作建议                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------- |
| **参与多个 Subreddit** | 如 r/wallstreetbets, r/stocks, r/investing 等，关注“热帖”（Hot/Top/Rising）；对反复出现的 ticker 做交叉验证；避免盲目跟风 |
| **使用工具监控热度**       | ApeWisdom 跟踪提及频次；AltIndex 推送突发热议股票，迅速掌握时机                                                     |
| **结合基本面与技术面判断**    | 热度只是信号，记得做独立调研（DD, Due Diligence），查看财报、负债、产品前景等                                               |
| **警惕梗股风险**         | 快涨快跌、高波动、高短线投机，适合波段交易或短线，但不适合作为长期持有标的                                                         |
| **分散平台检索**         | 交易网站的“Most Active”板块也能提供发现思路，搭配 Reddit 热度增强判断。([Reddit][8])                                   |

---

## 最后提醒

* 这些方法可以帮助你识别“近期被热议”的股票，但并不是财务建议。
* 市场信息变化迅速，请随时关注最新动态、每日交易量、消息面和风险管理。
* 杠铃策略有效：热点短线配合长期优质标的，这样的组合更稳健。

如果你想进一步了解如何使用 ApeWisdom、AltIndex，或想看某支股票在 Reddit 上的具体讨论，我也很乐意帮你继续探索！

---

* [Business Insider](https://www.businessinsider.com/meme-stocks-chatgpt-ai-reddit-short-interest-aeo-dnut-kss-2025-7?utm_source=chatgpt.com)
* [金融时报](https://www.ft.com/content/75a27b2b-fb9f-40fc-8a3d-76b608e600ac?utm_source=chatgpt.com)
* [市场观察](https://www.marketwatch.com/story/im-already-up-45-000-in-about-an-hour-reddit-traders-boast-about-wins-as-meme-stock-mania-returns-18c2829a?utm_source=chatgpt.com)

[1]: https://en.wikipedia.org/wiki/R/wallstreetbets?utm_source=chatgpt.com "R/wallstreetbets"
[2]: https://www.reddit.com/r/stocks/?utm_source=chatgpt.com "Stocks - Investing and trading for all - Reddit"
[3]: https://www.reddit.com/r/StockMarket/?utm_source=chatgpt.com "r/StockMarket - Reddit's Front Page of the Stock Market"
[4]: https://www.reddit.com/r/investing/?utm_source=chatgpt.com "r/Investing - Reddit"
[5]: https://www.reddit.com/r/pennystocks/?utm_source=chatgpt.com "Welcome to /r/pennystocks - Reddit"
[6]: https://apewisdom.io/?utm_source=chatgpt.com "Ape Wisdom | Trending Stocks on Reddit"
[7]: https://www.reddit.com/r/TheRaceTo10Million/comments/1hqw0sx/how_do_you_guys_follow_and_find_the_news_of/?utm_source=chatgpt.com "How do you guys follow and find the news of stocks as soon as they ..."
[8]: https://www.reddit.com/r/wallstreetbets/comments/qflvsy/simplest_and_easiest_way_of_finding_stocks/?utm_source=chatgpt.com "Simplest and easiest way of finding stocks : r/wallstreetbets - Reddit"
[9]: https://www.reddit.com/r/TheRaceTo10Million/comments/1ho9eud/how_do_you_guys_find_these_stocks_with_crazy/?utm_source=chatgpt.com "How do you guys find these stocks with crazy potential before they ..."
[10]: https://economictimes.indiatimes.com/news/international/global-trends/us-news-krispy-kreme-go-pro-join-the-meme-party-what-are-meme-stocks-and-how-do-they-work/articleshow/122862995.cms?utm_source=chatgpt.com "Krispy Kreme, Go Pro join the meme party: What are meme stocks and how do they work?"
[11]: https://www.ft.com/content/75a27b2b-fb9f-40fc-8a3d-76b608e600ac?utm_source=chatgpt.com "Meme stock mania returns as Krispy Kreme and GoPro shares soar"
[12]: https://www.businessinsider.com/meme-stocks-chatgpt-ai-reddit-short-interest-aeo-dnut-kss-2025-7?utm_source=chatgpt.com "Here's ChatGPT's advice on how to spot the next meme stock"
[13]: https://www.marketwatch.com/story/im-already-up-45-000-in-about-an-hour-reddit-traders-boast-about-wins-as-meme-stock-mania-returns-18c2829a?utm_source=chatgpt.com "'I'm already up $45,000 in about an hour' - Reddit traders boast about wins as meme-stock mania returns"
