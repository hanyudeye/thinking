from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# print(reg.coef_)

# 加载示例数据集

from sklearn import datasets 
iris=datasets.load_iris()
digits=datasets.load_digits()

# print(iris.data)
# print(digits.data)
print(digits.images[0])
