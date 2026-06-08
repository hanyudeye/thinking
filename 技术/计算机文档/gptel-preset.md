下面我给你一套 **真正高级、可扩展、可一键切换的 gptel preset（预设）系统**，完全基于你当前打开的 gptel 文档（  [github.com](https://github.com/karthink/gptel)），并且专门为 **Spacemacs 用户** 优化。

你将获得：

- **写代码模式（Coding Mode）**
- **写文案模式（Writing Mode）**
- **本地模型模式（Local LLM Mode）**
- 一键切换（通过 `SPC a i g` → presets）
- 可继承、可叠加、可扩展

这是 gptel 官方文档中“Option presets”机制的高级用法（  [github.com](https://github.com/karthink/gptel)）。

---

# 🎯 最终效果（你将获得什么）
你会拥有：

```
@coding
@writing
@local
```

只要在 prompt 里写：

```
@coding 解释这段代码
```

或在 gptel 菜单里选择 preset，就能瞬间切换整套配置（backend / model / system prompt / tools / temperature）。

---

# 🧩 **完整可用的 Spacemacs 配置（直接复制即可）**

把下面放进 `dotspacemacs/user-config`：

```elisp
;; ===========================
;; gptel 高级 preset 系统
;; ===========================

(use-package gptel
  :ensure t
  :config

  ;; --- 1. 定义 Coding Mode ---
  (gptel-make-preset
   'coding
   :description "写代码模式：Claude + 工具 + 严格系统提示"
   :backend "Claude"
   :model 'claude-3-7-sonnet-20250219
   :system
   "You are an expert software engineer. Provide clean, correct, optimized code. 
Explain reasoning only when necessary. Prefer minimal output."
   :temperature 0.1
   :tools '("read_buffer" "modify_buffer"))

  ;; --- 2. 定义 Writing Mode ---
  (gptel-make-preset
   'writing
   :description "写文案模式：OpenAI + 创意增强"
   :backend "OpenAI"
   :model 'gpt-4o-mini
   :system
   "You are a professional writer. Produce clear, engaging, human‑like prose.
Focus on tone, clarity, and structure."
   :temperature 0.8)

  ;; --- 3. 定义 Local LLM Mode（Ollama） ---
  (gptel-make-preset
   'local
   :description "本地模型模式：Ollama + 大上下文 + 低温度"
   :backend "Ollama"
   :model 'qwen2.5:latest
   :system
   "You are a local LLM running on the user's machine. Be concise and efficient."
   :temperature 0.2
   :use-context 'system)

  ;; --- 4. 默认 preset（可选） ---
  (setq gptel-default-preset 'coding)
)
```

---

# 🕹️ **如何使用这些 preset**

### 方式 1：在 prompt 中直接调用（最方便）
```
@coding 优化这段 Python 代码
@writing 帮我写一段产品介绍
@local 总结这个文件内容
```

gptel 文档明确说明：`@preset-name` 会自动应用 preset（  [github.com](https://github.com/karthink/gptel)）。

---

### 方式 2：通过菜单切换  
```
SPC a i g
```

然后按：

```
p
```

你会看到：

```
coding
writing
local
```

选中即可切换。

---

# 🧠 **为什么这是“高级 preset 系统”？**

因为它具备：

### ✔ 多 preset 继承与叠加  
你可以这样定义一个 preset 继承另一个：

```elisp
(gptel-make-preset
 'coding-deep
 :parents '(coding)
 :model 'deepseek-reasoner
 :backend "DeepSeek")
```

### ✔ 任意 gptel 变量都能写进 preset  
文档说明：`:foo` 会自动对应 `gptel-foo`（  [github.com](https://github.com/karthink/gptel)）。

例如：

```
:temperature
:use-context
:context
:tools
:system
:backend
:model
```

全部都能写。

### ✔ 一键切换 backend + model + system prompt  
你可以瞬间从 Claude 切到 OpenAI，再切到本地模型。

### ✔ 与 Spacemacs 完全兼容  
不需要改 layer，不需要改 keybinding。

---

# 🚀 想要更强？我可以继续为你做：

如果你愿意，我还能帮你扩展：

### 🔧 1. “自动 preset”  
根据 buffer 类型自动切换：

- `.py` → coding  
- `.md` → writing  
- `.org` → local  

### 🧩 2. “项目级 preset”  
每个项目自动加载不同 preset。

### 🧠 3. “智能工具链 preset”  
自动启用：

- read_buffer  
- modify_buffer  
- web_search  
- 文件上下文  

### 🗂 4. “Org-mode 多分支对话 + preset 绑定”  
每个 org heading 自动绑定不同 preset。

---

你想让我继续为你构建 **自动 preset 系统** 吗（比如根据文件类型自动切换）？
