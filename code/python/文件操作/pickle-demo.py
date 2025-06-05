import pickle

a={'name': 'Alice', 'age': 30, 'city': 'New York'}
# 序列化 - 将对象转换为字节流
# pickle.dump(obj, file)  # 将对象保存到文件
# with open('data.pkl', 'wb') as f:
#     pickle.dump(a, f)

# print(pickle.dumps(a))       # 将对象转换为字节字符串

# 反序列化 - 将字节流转换回对象
# with open('data.pkl', 'rb') as f:
    # print(pickle.load(f) )      # 从文件加载对象
# pickle.loads(bytes)     # 从字节字符串加载对象

# 5. 注意事项
# 安全性：不要 pickle 不信任的数据，因为它可能包含恶意代码
# 兼容性：不同版本的 Python 之间的 pickle 数据可能不兼容
# 文件模式：使用二进制模式('wb', 'rb')打开文件
# 仅用于 Python：pickle 格式是 Python 特有的，不适合与其他语言交换数据
# 使用 pickle 模块是在 Python 中持久化存储数据的常用方法之一，特别适合保存和加载 Python 特有的数据结构。