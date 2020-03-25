import pandas as pd
import numpy as np

# 每次随机数之前如果不加这个函数，随机数就是根据时间系统自动选取，如果两个随机数生成函数之前的seed一样，
# 则生成的随机数列也是一模一样的
np.random.seed(123)


df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))

df.plot()

pd.tools.plotting.scatter_matrix(df)
# 输出一个图表，横轴为index，纵轴为各列

df.plot('A','B', kind = 'line');
# 以df中的A为横坐标，B为y值画图，kind :
# 'line' : line plot (default)
# 'bar' : vertical bar plot
# 'barh' : horizontal bar plot
# 'hist' : histogram
# 'box' : boxplot
# 'kde' : Kernel Density Estimation plot
# 'density' : same as 'kde'
# 'area' : area plot
# 'pie' : pie plot
# 'scatter' : scatter plot
# 'hexbin' : hexbin plot

df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='magma')
# 绘制散点图，横轴为A列，纵轴为C列，生成的colormap比对图的size是B列，colormap的颜色选择类型是magma。
# 其他颜色数组 [ 'viridis', 'plasma', 'inferno', 'magma', 'cividis']

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
# 强制绘制后的图像宽高比相等，从而更好的看出横纵坐标之间范围的差距


pd.tools.plotting.scatter_matrix(df)
# 假设iris有四列数据，这个函数输出一个 4*4的散点图，用来展示相互之间的关系