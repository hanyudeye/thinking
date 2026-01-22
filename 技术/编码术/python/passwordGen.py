import random

"""_summary_
这个密码生成器： 会先使用3个小写字母，再选择3个数字，再选择2个特定字符，最后选择2个大写字符
这种随机的密码没有一点含义
"""

lChars="abcdefghijklmnopqrstuvwxyz"
uChars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
specialChars="!@#$%^&*-_+="

myPass=""

#Generate 3 lowercase letters
# 生成3个小写的字符
# generate 3 lowercase letters
for _ in range(3):
    myPass+=random.choice(lChars)

# 生成3个数字
# generate 3 digits
for _ in range(3):
    myPass+=random.choice(digits)

# 生成2个特殊字符
# generate 2 special characters
for _ in range(2):
    myPass+=random.choice(specialChars)

# 生成2个大写字符
for  _ in  range(2):
    myPass+=random.choice(uChars)

print(myPass)

# 输出：密码长度 10 个字符 (e.g. "abc123!@AB")