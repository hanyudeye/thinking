打开模型服务
ollama run llama3

curl http://172.27.224.1:11434/api/tags
返回模型列表

我的本地地址是 http://10.0.0.10:11434/api/tags

测试
curl http://10.0.0.10:11434/api/tags
返回成功


所以再spacemacs 里的配置为
``` org
;; OPTIONAL configuration
(setq
 gptel-model 'llama3:latest
 gptel-backend (gptel-make-ollama "Ollama"
                 :host "10.0.0.10:11434"
                 :stream t
                 :models '(llama3:latest)))
```



