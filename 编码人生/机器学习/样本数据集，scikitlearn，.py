# mglearn 机器学习库 start
import mglearn


# 生成数据集
# X, y = mglearn.datasets.make_forge()

# 可视化：
# import matplotlib.pyplot as plt
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)

# 显示图形
# plt.show()

# mglearn 机器学习库 end


import sys
# print("Python version: {}".format(sys.version))

import pandas as pd
# print("pandas version: {}".format(pd.__version__))

import sklearn
# print("sklearn version:{}".format(sklearn.__version__))


# 鸢尾花(Iris)数据集
from sklearn.datasets import load_iris
iris_dataset =load_iris()
# print("keys of iris_data:\n{}".format(iris_dataset.keys()))

# Out: dict_keys(['target_names', 'feature_names', 'DESCR', 'data', 'target'])
# DESCR 键对应的值是数据集的简要说明。
# 输出描述的前面部分
# print(iris_dataset['DESCR'][:193] + "\n...")
# print(iris_dataset['DESCR'] + "\n...")

# 波士顿房价数据集，在version 1.0.2 之后被移除
# from sklearn.datasets import load_boston
# boston_dataset = load_boston()


# 乳腺癌数据集
from sklearn.datasets import load_breast_cancer
breast_cancer_dataset = load_breast_cancer()
# print("keys of breast_cancer_dataset:\n{}".format(breast_cancer_dataset.keys()))
print("Shape of cancer data: {}".format(breast_cancer_dataset.data.shape))
# Out[5]:
# Shape of cancer data: (569, 30)
# 这个数据集共包含 569 个数据点，每个数据点有 30 个特征

