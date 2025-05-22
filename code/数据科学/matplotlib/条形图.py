from matplotlib import pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体（Windows/Linux 常见）
plt.rcParams['axes.unicode_minus'] = False   # 正确显示负号

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"] 
num_oscars = [5, 11, 3, 8, 10] 
# 条形的默认宽度是0.8，因此我们对左侧坐标加上0.1 
# 这样每个条形就被放置在中心了 
xs = [i + 0.1 for i, _ in enumerate(movies)] 
# 使用左侧x坐标[xs]和高度[num_oscars]画条形图 
plt.bar(xs, num_oscars) 
plt.ylabel("所获奥斯卡金像奖数量") 
plt.title("我最喜爱的电影") 
# 使用电影的名字标记x轴，位置在x轴上条形的中心 
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies) 
plt.show()