# 数据结构 start

# 列表结构 
li=[]
li.append("牛奶")
list.append(li,"面包")
li[len(li):]=["鸡蛋","黄油"  ]
li[3]="面粉"
print(li[len(li)-1])  # 获取最后一个元素
# print(li.index("牛奶"))
print(li)
li.extend(["糖","盐"])  # 扩展列表
print(li)


# 堆栈结构
stack = [3,4,5]
stack.append(6)  # 压栈
stack.append(7)

print(stack)
current=stack.pop()  # 弹栈
print(current)

# 队列结构 (先进先出，就像排队一样，先到先得)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # 入队
queue.append("Graham")  # 入队
print(queue.popleft())  # 出队
print(queue.popleft())  # 出队
print(queue)  # 队列剩余元素


