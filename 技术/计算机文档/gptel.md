我的配置
```
  ;; OPTIONAL configuration
  (gptel-make-deepseek "DeepSeek"
    :stream t
    :models '(deepseek-v4-flash)
    :key "KEY"
    )
  (gptel-make-preset 'deepseek-coding
    :backend "DeepSeek"
    :model 'deepseek-v4-flash
    :system "你是一个专业代码助手"
    )

```
大模型的**精准提示词**通常包含角色、任务、格式、约束等要素。以下是几类常用模板，可直接套用：

---

**1. 角色扮演 + 专业输出**  
> “你是一名资深数据科学家。请用简单易懂的语言解释‘过拟合’，字数不超过200字，并给出一个日常生活中的类比。”

**2. 分步骤推理**  
> “逐步思考：一个班级有30名学生，其中18人喜欢数学，15人喜欢语文，8人两者都喜欢。问只喜欢数学的有多少人？请输出推导过程。”

**3. 结构化输出**  
> “请将以下文本整理成表格：{文本}。表头为：日期、事件、影响。若信息缺失，填‘未知’。”

**4. 反向约束（避免什么）**  
> “写一篇300字的夏日文案，用于社交媒体。**避免**使用‘炎热’‘酷暑’‘汗流浃背’等词，风格要清新治愈。”

**5. 多轮对话中的上下文控制**  
> “基于我们之前讨论的Python代码，请优化它的运行速度。只输出优化后的代码，并添加注释说明改进了哪里。”

**6. 精确格式要求**  
> “生成一封英文商务邮件：收件人为客户John，催促他签署合同。要求：主题含‘URGENT’，正文分三段（提醒/截止日期/行动号召），结尾用‘Best regards’。”

**7. 混合指令（多任务）**  
> “请做三件事：1）总结下面文章的核心观点（50字内）；2）找出3个可能的事实错误；3）为文章起一个更吸引人的标题。”

---

**关键原则**：  
- 指定**角色**（你是谁）  
- 明确**任务**（要干什么）  
- 限定**输出格式**（长度、结构、风格）  
- 加入**负面约束**（不要什么）  
- 必要时**分步骤**（Let's think step by step）  

按需组合即可获得稳定、精准的回复。

你已经打开了 **gptel 的 GitHub 页面**，并且你问的是：

> **gptel-backend 如何创建多个后端？我想创建一个 DeepSeek 后端**

好消息：**gptel 本身就支持创建多个后端**，而且 DeepSeek 官方支持已经写在文档里了（你当前页面也显示了这一段）  [github.com](https://github.com/karthink/gptel)。

下面我给你一个 **最清晰、可直接复制到 Emacs 配置的方案**。

---

# ✅ gptel 中创建多个后端（包含 DeepSeek）

gptel 的后端是通过 `gptel-make-xxx` 系列函数注册的。

你可以注册多个后端，只要名字不同即可。

---

# 🎯 **1. 创建 DeepSeek 后端**

```elisp
(gptel-make-deepseek
 "DeepSeek"                 ;; 后端名称（随便起）
 :stream t                  ;; 是否流式输出
 :key "你的-deepseek-api-key")
```

注册后，你会在 `M-x gptel-menu` → `-m` 看到：

```
DeepSeek:deepseek-chat
DeepSeek:deepseek-reasoner
```

---

# 🎯 **2. 创建多个后端（示例：DeepSeek + OpenAI + Groq）**

你可以像这样注册多个：

```elisp
;; DeepSeek
(gptel-make-deepseek
 "DeepSeek"
 :stream t
 :key "你的-deepseek-key")

;; OpenAI
(gptel-make-openai
 "OpenAI"
 :key "你的-openai-key"
 :stream t)

;; Groq
(gptel-make-groq
 "Groq"
 :key "你的-groq-key"
 :stream t)
```

注册后，gptel 会自动在菜单里列出所有后端的模型。

---

# 🎯 **3. 设置默认后端（可选）**

如果你想默认使用 DeepSeek：

```elisp
(setq gptel-backend
      (gptel-make-deepseek
       "DeepSeek"
       :stream t
       :key "你的-deepseek-key"))

(setq gptel-model 'deepseek-reasoner)
```

---

# 🎯 **4. 在使用时切换后端**

在任意 gptel buffer 中：

```
C-u M-x gptel-send
```

或：

```
M-x gptel-menu → -m
```

你会看到所有后端的模型列表，例如：

```
DeepSeek:deepseek-chat
DeepSeek:deepseek-reasoner
OpenAI:gpt-4o-mini
Groq:llama3-70b
```

---

# 🎯 **5. 多后端最佳实践（推荐）**

如果你经常切换，可以定义 preset：

```elisp
(gptel-make-preset 'deepseek-coding
  :backend "DeepSeek"
  :model 'deepseek-reasoner
  :system "你是一个专业代码助手")

(gptel-make-preset 'deepseek-chat
  :backend "DeepSeek"
  :model 'deepseek-chat)
```

然后在 prompt 里直接写：

```
@deepseek-coding
帮我重构下面这段代码…
```

---

# 如果你愿意，我可以帮你：

- 生成一份 **完整的 gptel 多后端配置模板**
- 根据你的使用习惯（写代码/写文案/翻译）定制 preset
- 配置 Emacs 自动高亮、自动滚动、Org-mode 集成等

你想让我帮你把配置整理成一份可直接复制的 Emacs Lisp 吗。
