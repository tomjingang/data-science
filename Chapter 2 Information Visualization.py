# %matplotlib notebook
# %matplotlib inline

import matplotlib as mpl

mpl.get_backend()

import matplotlib.pyplot as plt


# 创建一个新的plot，但是不会改变原有的plot
plt.figure()



# -----------------------------------------------------坐标轴
# 得到现在的坐标轴
ax = plt.gca()
# 设置坐标轴参数 [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])
# x轴名称
plt.xlabel('The number of times the child kicked a ball')
# y轴名称
plt.ylabel('The grade of the student')
# 标题名称
plt.title('Relationship between ball kicking and grades')

plt.plot(x, list, '.') # 标注每个点，用 . 标注，这里也可以是别的，比如。

# 下面的三个点，会被视为与上述不同的新的三个data series， 会用不同的颜色表示
plt.plot(1,1,'.')
plt.plot(2,1,'.')
plt.plot(3,1,'.')

# 展示现在的plt
plt.show()

#--------------------------------------------------------------- Scatter Plot

x = np.array([1,2,3,4,5,6,7,8])
y = x

# 创建一个颜色的list
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green']*(len(x)-1)
colors.append('red')

plt.figure()

# 创建一个size时100， 由上述x，y构成的坐标图，颜色就是之前设置的颜色list
plt.scatter(x, y, s=100, c=colors)
# plot a data series 'Tall students' in red using the first two elements of x and y
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
# plot a second data series 'Short students' in blue using the last three elements of x and y 
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')
# 按照上述的label设置图示
plt.legend()
# add the legend to loc=4 (the lower right hand corner), also gets rid of the frame and adds a title
plt.legend(loc=4, frameon=False, title='Legend')




#---------------------------------------------------zip list的解包和给xy分别赋值
# 将两个list转换为两个tuple
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])

print(list(zip_generator))
# the above prints:
# [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# 星号 可以解包这个tuple构成的list
print(*zip_generator)
x, y = *zip_generator
# the above prints:
# (1, 6) (2, 7) (3, 8) (4, 9) (5, 10)
# (1, 2, 3, 4, 5)
# (6, 7, 8, 9, 10)



#----------------------------------------------- line plot

import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
# 用上述数据绘制图像，输出两条折线图
plt.plot(linear_data, exponential_data, '-o')

# 用红色的虚线绘制另一条线
plt.plot([22,44,55], '--r')

# 坐标基本信息
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
# add a legend with legend entries (because we didn't have labels when we plotted the data series)
plt.legend(['Baseline', 'Competition', 'Us'])

# 将两条直线间用蓝色的阴影填充， alpha是透明度， range则是阴影的范围
plt.gca().fill_between(range(len(linear_data)), 
                       linear_data, exponential_data, 
                       facecolor='blue', 
                       alpha=0.25)




# ----------------------------------------------------------------bar chart

plt.bar(x, height, width=0.8, bottom=None, , align='center', data=None, kwargs*)
# x:x坐标， height y的值，条形的高度。width，宽度，默认0.8. align条形的中间位置，lege为边缘
# color为条形颜色。 edgecolor边框颜色。 linewidth，边框宽度。 tick_lagel，下标的标签。
# log，y轴使用科学计算法。  orientation：vertical竖直，horizontal水平
# 绘制柱状图，柱宽 0.3
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

# 在上面画的那个柱旁边的位置再画一个柱状图
new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, exponential_data, width = 0.3 ,color='red')

# 上述两个柱状图摞在一起
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, exponential_data, width = 0.3, bottom=linear_data, color='r')

# 绘制一个横向的柱状图
plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, exponential_data, height = 0.3, left=linear_data, color='r')


#---------------------------------------------------------   实际操作
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++ '  , 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]


# align设置plt.xticks()函数中的标签的位置；yerr让柱形图的顶端空出一部分
plt.bar(pos, popularity, align='center')

# 这里让所有的柱 颜色为 灰色，但是第一个强调为浅蓝色
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')


plt.xticks(pos, languages, alpha=0.8)
plt.ylabel('% Popularity', alpha=0.8)


# 设置x轴的各项名称，把pos对应的位置换为languages
plt.xticks(pos, languages) 
#设置y轴名称
plt.ylabel('% Popularity')

plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

#删除掉 图标上下左右的刻度线， 以及左侧的坐标值，保留x轴的 坐标值
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
# 删除掉图标的图标线。边框
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# 将y轴的数字直接在柱上面百分号形式体现出来 (标注位置的横向位置，标注位置的纵向位置，标注位置的y轴对应坐标，标注的位置（居中），
# 颜色，字体大小)
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)


plt.show()





# --------------------------------------------------- subplot

import matplotlib.pyplot as plt
import numpy as np

# 一个综合例子 创建一个2*2的图表阵，然后在第二行第二列画直线图,第一行第二列画一个柱状图
fig, ax = plt.subplots(2,2)
linear_data = np.array([1,2,3,4,5,6,7,8])
ax[1,1].plot(linear_data,'-')
ax[0,1].bar(linear_data,[1,2,3,4,5,6,7,8], color= 'b',alpha=0.25)
plt.show()



# 创造一个 1 行，两列的坐标图，第三位表示，现在对第一列编辑.
# 图表从左到右，从上到下进行编号
# 假设分了四块，但是想上半部分有两个图，但是下半部分合在一起一个图，则三个图的代号分别为
# (2,2,1), (2,2,2), (2,1,2) 相对于，对于下半部分，只是两行，一列的第二项
# plt.subplot(1,2,1)也可以写成plt.subplot(121)
plt.subplot(1, 2, 1)
linear_data = np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data, '-o')
exponential_data = linear_data**2 

# 现在对第二列编辑
plt.subplot(1, 2, 2)
plt.plot(exponential_data, '-o')

# 重新对第一列编辑
plt.subplot(1, 2, 1)
plt.plot(exponential_data, '-x')
ax1 = plt.subplot(1, 2, 1)

# 为了让几个图标的横纵坐标统一，sharey=ax1为让ax2的纵坐标ax1相同, sharex=ax1为让ax2的横坐标与ax1相同
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data, '-x')


# 创建一个3*3的，横纵坐标相同的坐标图阵，并在第五个图上画图
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
ax5.plot(linear_data, '-')
# 让上述得到的坐标图的横纵刻度可视化
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

# 创建两个图表共用一个图，共用一个x轴，两个y轴
ax2 = ax1.twinx()


# ------------------------------------------------------------histogram
# gridspec创建这样一个图表，左半部分和上部分分别表示x轴和y轴数据的变化情况，
# 中间的图标表示x与y的关系

import matplotlib.gridspec as gridspec

plt.figure()
# 创建一个3*3的 图表matrix， 并设置三个图表在其中的位置
gspec = gridspec.GridSpec(3, 3)
top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

# 设置x y的值并体现在图表中
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal')

# 清理数据，重新设置数据，并对数据进行归一化处理。 bins代表了，图中一共用几个长方形来显示数据
top_histogram.clear()
top_histogram.hist(X, bins=100, normed=True)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', normed=True)

# 将左，上两个图表的x轴与右下的图表在一边
side_histogram.invert_xaxis()

# 设置横纵坐标范围
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)

# 设置title  https://blog.csdn.net/helunqu2017/article/details/78659490
axs[n].set_title('n={}'.format(sample_size))


# ----------------------------------------------------------heatmaps

plt.figure()

# 创建一个heatmap
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
_ = plt.hist2d(X, Y, bins=25)

# 添加一个colorbar，来显示每种颜色代表什么
plt.colorbar()


# -----------------------------------------------------------BOX

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']

bplot = plt.boxplot(all_data, patch_artist=True, labels=labels)  # 设置箱型图可填充
plt.title('Rectangular box plot')

colors = ['pink', 'lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)  # 为不同的箱型图填充不同的颜色

plt.yaxis.grid(True)
plt.xlabel('Three separate samples')
plt.ylabel('Observed values')
plt.show()



# -----------------------------------------Seaborn 更高级的API来画图

import seaborn as sns
x = np.random.randn(100)
# 核密度估计(kernel density estimation)是在概率论中用来估计未知的密度函数，属于非参数检验方法之一。
# 通过核密度估计图可以比较直观的看出数据样本本身的分布特征。具体用法如下：
sns.kdeplot(x, cut=0, cumulative=True, shade=True, color='g', vertical=False, cbar = True)
# cut：参数表示绘制的时候，切除带宽往数轴极限数值的多少(默认为3)
# cumulative ：是否绘制累积分布
# shade：若为True，则在kde曲线下面的区域中进行阴影处理，color控制曲线及阴影的颜色
# vertical：表示以X轴进行绘制还是以Y轴进行绘制.若为False,则横轴为x轴
# cbar：参数若为True，则会添加一个颜色棒(颜色帮在二元kde图像中才有)


# displot()集合了matplotlib的hist()与核函数估计kdeplot的功能，
# 增加了rugplot分布观测条显示与利用scipy库fit拟合参数分布的新颖用途。
fig,axes=plt.subplots(1,3)   #创建于给1*3的图表阵列
sns.distplot(x,color="g", hist=True,kde=True, ax=axes[1] , bins=20,rug=True，fit=norm， norm_hist=True)
# color控制直方图的颜色
# hist，kde若为True，则在图中共同显示
# ax为这个displot作用与中间的图表
# bins为数据分成多少个小格
# fit为展示处一个黑线，这里是正态分布的曲线，从而和kde画出的曲线进行对比，看拟合程度
# rug：控制是否生成观测数值的小细条
# norm_hist：若为True, 则直方图高度显示密度而非计数(含有kde图像中默认为True)

sns.jointplot(x,y,alpha=0.4, kind='hex', space = 0)
# 将x与y两组数据结合，生成一个二元的密度图像，图像上方为x的分布密度函数的hist，图像下方为y的分布密度函数的hist
# kind可以为hex（生成的密度函数用小六边形表示），可以为kde（生成的二元密度函数类似于等高线，x与y的密度函数以kde的形式展现）
# space为单独的分布密度函数与二元密度函数的举例。