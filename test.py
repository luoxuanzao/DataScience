# matplotlib模块绘制直方图
# 读入数据
from matplotlib import pyplot as plt
array = [10,20,30,40]
# 绘制直方图
plt.hist(x = array, # 指定绘图数据
         bins = 20, # 指定直方图中条块的个数
         color = 'steelblue', # 指定直方图的填充色
         edgecolor = 'black' # 指定直方图的边框色
         )
# 添加x轴和y轴标签
plt.xlabel('年龄')
plt.ylabel('频数')
# 添加标题
plt.title('乘客年龄分布')
# 显示图形
plt.show()
