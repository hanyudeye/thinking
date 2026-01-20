import time

varA = 99
varB = 100
# 变量操作
# print(f"varA {varA} 和 var B {varB} 的 和是 {varA+varB}!") 

# 控制流程

if varA > varB:
    print(f"varA {varA} 大于 var B {varB} !")
else:
    print(f"varA {varA} 小于等于 var B {varB} !")

 # 循环   
for i in range(5):  
    time.sleep(1)
    # print(f"循环第 {i+1} 次")

def acction():
    print("执行了 action 函数")

acction()

# 异常处理，用于调试
try:
    result = 10 / 0  # 故意制造一个除零错误 
except ZeroDivisionError as e:
    print(f"发生了一个错误: {e}")
finally:
    print("无论如何都会执行的代码块")





