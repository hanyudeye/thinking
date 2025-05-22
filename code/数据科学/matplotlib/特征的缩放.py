# 加载库 
import numpy as np 
# from scikit-learn import preprocessing 
from  sklearn import preprocessing 
# 
# 创建特征 
feature = np.array([[-500.5], 
                    [-100.1], 
                    [0], 
                    [100.1], 
                    [900.9]])

# 创建缩放器 
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1)) 
# 缩放特征的值 
scaled_feature = minmax_scale.fit_transform(feature)

print(scaled_feature)

# scikit-learn