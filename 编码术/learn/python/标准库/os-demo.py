# 操作系统接口
import os

print(os.getcwd())  # 获取当前工作目录
os.chdir('..')  # 切换到上级目录
print(os.getcwd())  # 获取当前工作目录

import glob
# glob.glob('*.py')  # 获取当前目录下所有的.py文件
print(glob.glob('*'))  # 获取当前目录下所有的文件



