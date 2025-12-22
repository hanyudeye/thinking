import numpy as py

#创建一个 4 x 3 的矩阵
matrix = py.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9],
                     [10, 11, 12]])

print(matrix)

# 将矩阵转置 2x 6
print(matrix.reshape(2, 6))

