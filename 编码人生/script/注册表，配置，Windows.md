## 右击通过cursor打开项目

1. 添加到右键菜单

按 Win + R，输入 regedit，打开注册表编辑器。
找到以下路径：
HKEY_CLASSES_ROOT\Directory\Background\shell\
右击 shell，选择 新建 -> 项，命名为 Open with Cursor（这是你在右键菜单中看到的选项名称）。
在刚刚创建的 Open with Cursor 项下，右击 新建 -> 项，命名为 command。

选择 command 项，在右侧窗口中双击 默认 键值，将其值设置为批处理文件的路径。例如：
C:\path\to\exefile "%V"
注意：%V 是当前文件夹路径的占位符。

## 创建符号链接

- 链接一个文件
mklink C:\link.txt D:\real_folder\file.txt
创建一个名为 link.txt 的符号链接，指向真正的 file.txt

- 链接一个文件夹

mklink /D C:\MyLink D:\RealFolder
MyLink 就是对 RealFolder 的一个快捷方式，可当作目录使用

mklink /D C:\Users\Administrator\AppData\Local\npm-cache E:\Users\Administrator\AppData\Local\npm-cache