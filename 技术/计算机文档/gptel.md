提示词： 你是一个全能专家，回答问题专业简洁


todo: 配置多个后端

在 ~/.authinfo 文件

 machine api.deepseek.com login apikey password KEY
 
在 .spacemacs 配置后端
``` elisp

   (gptel-make-deepseek "DeepSeek"
    :stream t
    :models '(deepseek-v4-flash)
    :key (gptel-api-key-from-auth-source :host "api.deepseek.com")

    )
  ;; (gptel-make-preset 'deepseek-coding
  ;;   :backend "DeepSeek"
  ;;   :model 'deepseek-v4-flash
  ;;   :system "你是一个专业代码助手"
  ;;   )

  (gptel-make-ollama "Ollama"
    ;; :host "192.168.110.162:11434"
    :host "localhost:11434"
    :stream t
    :models '(gemma4:e4b)
    )

  (setq
   ;; gptel-model 'gemma4:e4b
   gptel-backend (gptel-get-backend "DeepSeek")
   gptel-model 'deepseek-v4-flash
   gptel-include-reasoning nil
   )
```

---



# 🧩 一套可直接复制的 Spacemacs 配置（支持多个 provider）

把下面内容放进 `~/.spacemacs` 的 `dotspacemacs/user-config`：

```elisp
;; ===========================
;; gptel 多 LLM provider 配置
;; ===========================

(use-package gptel
  :ensure t
  :config
  ;; 1. OpenAI
  (gptel-make-openai "OpenAI"
    :key (auth-source-pick-first-password :host "api.openai.com")
    :models '(gpt-4o-mini gpt-4o gpt-5.5))

  ;; 2. Anthropic Claude
  (gptel-make-anthropic "Claude"
    :key (auth-source-pick-first-password :host "api.anthropic.com")
    :stream t)

  ;; 3. Google Gemini
  (gptel-make-gemini "Gemini"
    :key (auth-source-pick-first-password :host "generativelanguage.googleapis.com")
    :models '(gemini-2.0-flash gemini-2.0-pro))

  ;; 4. DeepSeek
  (gptel-make-openai "DeepSeek"
    :host "api.deepseek.com"
    :key (auth-source-pick-first-password :host "api.deepseek.com")
    :models '(deepseek-chat deepseek-reasoner))

  ;; 5. 本地 Ollama
  (gptel-make-ollama "Ollama"
    :host "localhost:11434"
    :stream t
    :models '(qwen2.5:latest mistral:latest llama3.1:latest))

  ;; 默认 backend（可选）
  (setq gptel-backend "Claude"
        gptel-model 'claude-3-7-sonnet-20250219))
```

---

# 🔐 API Key 建议放在 `~/.authinfo`  
gptel 文档也推荐这样做（  [github.com](https://github.com/karthink/gptel)）：

```
machine api.openai.com login apikey password YOUR_KEY
machine api.anthropic.com login apikey password YOUR_KEY
machine generativelanguage.googleapis.com login apikey password YOUR_KEY
machine api.deepseek.com login apikey password YOUR_KEY
```

这样 Emacs 会自动读取，不需要把 key 写进配置文件。

