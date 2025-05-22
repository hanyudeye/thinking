from matplotlib import pyplot as plt 
 
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] 
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] 
 
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体（Windows/Linux 常见）
plt.rcParams['axes.unicode_minus'] = False   # 正确显示负号


# 创建一幅线图，x轴是年份，y轴是gdp 
plt.plot(years, gdp, color='green', marker='o', linestyle='solid') 
 
# 添加一个标题 
plt.title("名义GDP") 
 
# 给y轴加标记 
plt.ylabel("十亿美元") 
plt.show()