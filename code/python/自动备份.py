# 1. 确认要备份的内容
src="f:/me/hello.txt"


# 2. 确认要备份的路径
dest="f:/me/hello.txt.bak"

# 3. 设置备份时间
# for i in range(1, 6):
#     backup_time = f"{i} day ago"
#     print(f"备份时间: {backup_time}")

# 4. 设置备份文件名
# 5. 执行备份操作
import os
import shutil 
# shutil.copy(src, dest)

shutil.copyfile(src, dest)
