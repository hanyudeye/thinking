 # 加载库
import numpy as np
# 创建一个矩阵
matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
# 返回最大的元素
print(np.max(matrix))

# 返回最小的元素
print(np.min(matrix))

# 找到每一行最大的元素
print(np.max(matrix, axis=1))

# 找到每一列最大的元素
print(np.max(matrix, axis=0))

#计算平均值
print(np.mean(matrix)) # 5.0

# 返回方差
print(np.var(matrix)) # 6.666666666666667

# 返回标准差
print(np.std(matrix)) # 2.581988897471611

