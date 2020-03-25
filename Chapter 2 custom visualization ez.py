# A challenge that users face is that, for a given y-axis value (e.g. 42,000), 
# it is difficult to know which x-axis values are most likely to be representative, 
# because the confidence levels overlap and their distributions are different 
# (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose 
# for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) 
# and then draw a horizontal line and color bars based on this value. So bars might be colored red if 
# they are definitely above this value 
# (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.



import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

df = df.transpose()
# 将df的行和列呼唤
# df.describe()
# 输出一个matrix，里面包含了 诸如 count数目 max最大值 等每一列数据的基本信息

import math

mean = list(df.mean())# 平均值

std = list(df.std())# 标准差

ye1 = []  # 误差

for i in range (4) :
    ye1.append(1.96*(std[i]/math.sqrt(len(df))))

nearest = 100
Y = 39500

df_p = pd.DataFrame()

df_p['diff'] = nearest*((Y - df.mean())//nearest) # 输出整数部分

df_p['sign'] = df_p['diff'].abs()/df_p['diff'] # 输出符号 正负号

old_range = abs(df_p['diff']).min(), df_p['diff'].abs().max()
# 输出diff这一列中的最大值和最小值

new_range = .5,1
print(type(new_range))

df_p['shade'] = df_p['sign']*np.interp(df_p['diff'].abs(), old_range, new_range)
# 这样做的目的是
# 1. 将diff中的四个值按照线性关系插入到0.5到1之间，最小的对应0.5，最大对应1.0，等比例插入
# 2. 再乘以他们之间的符号（正负号，含0）

shade = list(df_p['shade'])
# print(shade)
from matplotlib import cm

blues = cm.Blues

reds = cm.Reds


# 当diff为正，则用蓝色
# 当diff为负，则用红色
# 当diff为0，则用白色
color = ['White' if  x == 0 else reds(abs(x))
         if x<0 else blues(abs(x)) for x in shade]

import matplotlib.pyplot as plt

plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k')

plt.bar(range(len(df.columns)), height = df.values.mean(axis = 0), yerr=ye1,
         error_kw={'capsize': 10, 'elinewidth': 2, 'alpha':0.7}, color = color)

plt.axhline(y=Y, color = 'black', label = 'Y')
# 绘制平行于x轴的水平参考线

plt.text(3.5, 39000, "39000")

plt.xticks(range(len(df.columns)), df.columns)
# x轴为df的列名

plt.title('Generated Data Between 1992 - 1995')

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off',  right='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()