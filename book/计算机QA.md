## vscode 如何查看字符的编码

快捷键  ga 

## vscode 关闭自动补全

最常见的做法 （直接关闭自动补全）
1. 打开设置 Ctrl+, 或 cmd+,
2. 搜索 editor.quicksuggestions false

``` json
"editor.quickSuggestions": {
    "other": false,
    "comments": false,
    "strings": false
}
```

彻底关闭所有自动建议
如果你想关闭弹窗补全
``` json
"editor.suggestOnTriggerCharacters": false,
"editor.quickSuggestions": false,
"editor.wordBasedSuggestions": false,
"editor.parameterHints.enabled": false
```

关闭特定语言的补全
``` json
"[python]": {
    "editor.quickSuggestions": false,
    "editor.suggestOnTriggerCharacters": false
}

```


关闭来自插件（如 Pylance / IntelliCode）的补全
1. Pylance 自动补全
```
Pylance > Editor: Auto Import Completions
```
2. IntelliCode 自动补全（AI 提示）
打开扩展（Ctrl+Shift+X）
搜索 “IntelliCode”
点击 禁用

3. git copilot
在命令面板执行 
github copilot : disable globally
!测试以后这个有效果，可以全局关闭下，因为这个只关闭一个文件
对某个语言关闭，可以用下面的语法
``` json
"github.copilot.enable": {
        "*": false,
        "plaintext": false,
        "markdown": true,
        "scminput": false,
        "python":false,
    }
```

4.Tabnine 设置->搜索Tabnine -> 关闭 "Enable Autocomplete"
