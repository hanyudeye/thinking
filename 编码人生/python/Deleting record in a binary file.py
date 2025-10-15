import pickle
"""
pickle 库是用来序列化 (seralize ) 和反序列化 (deserialize) python 对象的。简单说，它可以把 python
对象（如列表、字典、自定义类的实例等）转换成一种可以存储到文件或通过网络传递的二进制
格式；之后再恢复成原来的对象

一句话解释：
pickle 就像一个 打包机；能把python 对象打包成字节流（bytes)，再解包回来。

主要用途
1. 保存程序运行状态
比如把训练好的机器学习模型，计算结果或配置数据保存到磁盘

data={"number",12,"name":"Alice","age":25,"scores",[90,88,98]}

# 序列化（保存文件）
with open("data.pkl","wb") as f:
    pickle.dump(data,f)

# 反序列化（从文件读取）

with open("data.pkl","rb") as f:
    loaded_data=pickle.load(f)
print(loaded_data)
    # 格式化打印列表
    for ch in loaded_data:
        print(ch) #prints one of the chosen 列表记录

        rno=ch[0]  #记录编号
        rname=ch[1] #记录名称 学生名字
        rage=ch[2] # 年龄


2.在进程之间传递python对象
某些并行计算或网络通信场景中（比如 multiprocessing 模块），需要通过 pickle 把对象转成
字节流后传递
3. 缓存复杂数据结构
如果某个数据计算起来很慢，可以计算一次后用pickle 存储，下次直接加载。

注意事项（非常重要）
1. 安全风险
不要反反序列话(pickle.load()) 不可信的文件或网络数据，因为 pickle 数据中可能包含恶意代码，会被执行。
- 安全替代方案：
  - 纯数据可以用 json,csv
  - 模型保存可以用  joblib  或框架自带方法 torch.save()
2. 跨版本兼容性差

"""
path = "file/studrec.dat"
wpath = "file/studrec1.dat"
def bdelete():
    # 打开文件
    with open(path,"rb") as F:
        stud = pickle.load(F)
        print(stud)

    # 删除
    rno=int(input("请输入需要删除的列编号"))
    with open(wpath,"wb") as F:
        # 删除 编号对应的数组
        rec=[i for i in stud if i[0] != rno]
        # print(rec)
        # 保存文件
        pickle.dump(rec,F)

bdelete()