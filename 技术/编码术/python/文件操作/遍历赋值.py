a=[[12, 'biancaa', 100.0], [6, 'Biancaa', 100.0], [7, 'bia', 100.0], [5, 'binkoo', 100.0], [1, 'Bia', 100.0]]

# 条件赋值数组

b=[i for i in a if i[0] != 12]
c=[i for i in a if i[0] < 6]
print(b)
print(c)