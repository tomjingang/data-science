import pandas as pd 
import re
# ------------------------------------------------------------------------------------------- 创建 和 基本查询

# 通常情况下，要对列操作，在各种函数里添加 axis=1 理论上都ok
# 在函数中添加inplace=True 意味着直接对Dataframe内部值进行操作，改变了原始数据

animals = ['tiger', 'Bear', 'Moose']
numbers = [1, 2, 3]

pd.Series(numbers)

pd.Series(animals)            # 出来的有两列 第一列是index，从0开始，第二列是animals中的数据

data = {'Zhoumanhong':'25.10.1996', 
'Tanglichen':'25.12.1996'}

pd.Series(data)               # 出来的有两列，第一列是key，第二列是values

s = pd.Series(['Zhoumanhong', 'Tanglichen'], index=['25.10.1996', '25.12.1996'])

s.iloc[1]     # 输出Tanglichen 
print (s.iloc[1])
print(s.loc['25.10.1996'])  #输出Zhoumanhong loc中的参数是index

%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label]= value+2

%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
s+=2    # 这种方法的时间会大大缩小


%%timeit -n 100
summary = 0
for item in s:
    summary+=item

%%timeit -n 100
summary = np.sum(s)  #这种方法 向量的方法，会大大缩短时间



# ------------------------------------------------------------------------------------------- DataFrame的基本操作
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
# 在这里 index是行，name cost 等是列, columns 可以给每一列命名


df.head()  # 默认读取前五条
df.loc['Store 1', 'Cost']   # 获取Store 1的所有cost 
df.loc[0]['Cost']           # 获取第一行中Cost的值

# .loc中的两个参数分别为，列和行所以如果想选择全部列，和行中的某几列:
df.loc[:,['Cost']]
df['Cost']

# 如果想把列作为索引:
df.T



copy_df = df.copy()
del copy_df['Name']  # 直接在表格上删除这一列，所以通常要copy一下

df.drop([0,1]) # 删除前两行
df.drop(df.columns[行名])# 删除具体行   
df.drop([列名], axis = 1) # 删除列，一定要加 axis为1
# 删除一列，或一行。注意，del直接生效，会直接修改表格内容。所以建议copy

df['Location'] = None
# 新添加一列Location,所有值为None
df.loc['Store 3'] = None 
# 新添加一行



import numpy as np
import pandas as pd
df=pd.DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['one','two','three','four']) 
# 生成一个4*4的从0-15 的矩阵，列是abcd， 行是onetwothreefour




# ------------------------------------------------------------------------------------------- DataFrame的 index 和 Loading

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
# 设置这个文件中的第一列为index， 并跳过第一行
df.columns   
# 获取这个Dataframe的所有行名
df.index
# 获取这个Dataframe的所有index



df.rename(index={1 : 'A', 2: 'B'}, columns = {'abc':'bcd'}, inplace = True)
# 把index中1改为A，2改为B。行中abc改为bcd。 inplace=True 意味着改直接作用与原文件。
# 如果不想直接更改源文件，则删掉inplace = True






# ------------------------------------------------------------------------------ Dataframe的数据查询，  Boolean再DataFrame中的使用
only_gold = df.where(df['Gold'] > 0)
only_gold.head() 
# 找到df中gold数量大于0的国家并将他们按照原数据结构展示出来，其他的没有金牌的国家这一行全部用NaN 表示
only_gold['gold'].count() 
# 输出onlygold中还剩下的 有gold的国家数量
only_gold = only_gold.dropna()
# 去除onlygold中数值为NaN的行。通过这一步和上两部就能得到 df中所有获得金牌数不是0的国家


df[df['Gold']>0]
df[(df['Gold'] >0) | (df['Gold .1'] > 0)]   
# 找出gold数不是0  or gold.1不是0 的国家。 '和'是 &  >, <, ==




# -------------------------------------------------------------------------------------------DataFrame中对Index进行操作
df['country'] = df.index
df = df.set_index('Gold')
# 讲Gold设置为新的index
df = df.reset_index()
# 彻底重置index

df['SUMLEV'].unique()
# 找出SUMLEV中的所有出现的值 

df = df.set_index(['STNAME', 'CTYNAME'])
# 双重索引，创建两个索引值，前者为第一个，后者为第二个
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]
# 比较两行，分别为同一Michigan下的两个城市



# -------------------------------------------------------------------------------------------DataFrame 进行排序
DataFrame.sort_values(by=?, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
# axis这个参数的默认值为0，匹配的是index，跨行进行排序，当axis=1时，匹配的是columns，跨列进行排序
# by这个参数要求传入一个字符或者是一个字符列表，用来指定按照axis的中的哪个元素来进行排序
# ascending这个参数的默认值是True，按照升序排序，当传入False时，按照降序进行排列
# 最后一个参数na_position是针对DataFrame中的空缺值的，默认值是last表示将空缺值放在排序的最后，也可以传入first放在最前
# inplace默认为False,如果该值为False，那么原来的pd顺序没变，只是返回的是排序的。如果是True，则原来的pd顺序发生变化。

df = df.sort_index()
# 对index进行排序 


import pandas as pd 
df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])


adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
# 对某一列的某一行进行赋值，同时对为赋值的行自动复制None


ab = pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
      left_index=False, right_index=False, sort=True,
      suffixes=('_x', '_y'), copy=True, indicator=False)
#1.on=None 用于显示指定列名（键名），如果该列在两个对象上的列名不同，则可以通过 left_on=None, 
#  right_on=None 来分别指定（这里可以用一个列表，来进行多重索引，就是两个都需要一样才认为是相同的）。
#  或者想直接使用行索引作为连接键的话，就将 left_index=False, right_index=False 设为 True。
#2. how='inner' 参数指的是当左右两个对象中存在不重合的键时，取结果的方式：inner 代表交集；outer 代表并集；left 和 right 分别为取一边
#   （这里的取一边，是两个集合进行集合运算之后的取一边，这时，每个表格的列已经得到了扩充）。
#3. suffixes=('_x','_y') 指的是当左右对象中存在除连接键外的同名列时，结果集中的区分方式，可以各加一个小尾巴。
#4. 对于多对多连接，结果采用的是行的笛卡尔积。

DataFrame.apply(func, axis=0, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds)
# func : function作用于每一列或行。
# axis : {0 或 ‘index’, 1 或 ‘columns’}, 默认 0.函数所应用的轴:0 或 ‘index’: 对每一列应用函数。 1 或 ‘columns’: 对每一行应用函数。
# args : tuple 除了array/series外，还要传递给func的位置参数。
# **kwds 要作为关键字参数传递给func的关键字参数。

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))
# group输出的就是对应的STNAME， frame就是对应的每一行的对应列的statename。
# groupby里面也可以多个参数，完整的： groupby(['',''], axis = 0). axis默认为0，也可以通过设置axis来再其他任何轴上进行分组（最后展现的分组依据在不同的轴)

df.groupby('STNAME').agg({'avg': np.average})
functions = ['size', 'sum', 'mean', 'std']
result = Top15['population'].groupby(Top15.index).agg(functions)
# 通过这个方法，可以直接将表格进行分组，然后对对应列采取相应的函数。
# 两种在agg中写函数的方法

df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}
# level 0 的意思是： 如果存在多重索引，按照第零层索引进行分组，也就是最外面的索引

import pandas as pd
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
# 将Grades的底层类型改为categories， 并按照升序排序，这样，就可以对Grades进行bool操作。比如
# Grades>C 得到的结果就是，C之前都是True， 之后都是False。

df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10,labels=['Larbe','Middle','Small'])
# 对美国2010的各个州的人口求平均值
# 并按照10为间隔，对列表按照后面的label进行分级 

df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
# index设置为YEAR，行的title设置为每种Make， KW为对应的每一个数据的内容，对数据进行平均值和求最小值。
# margins为True， 表示输出行的总和，若为false， 则不输出。


##------------------------------------------------- time
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')  # 求两个日期的时间差
## 这个日期是2016年6月3号，注意

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')  # 月份 M 年份 Y

ta3.index = pd.to_datetime(ta3.index) # 将ta3中不符合pd中日期的格式的index全部改成符合格式的形式

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df.asfreq('W', method = 'ffill')
# 从2016.01.10开始，取接下来的九个日期：没两周取一次，每次取当周的周日
# 将取样频率改为每一周一取

df.index.weekday_name
# 看df的index是星期几

df.diff()
# 看df每个日期之间差几天

df.resample('M').mean()
# 求每个月的平均值

df['2017']  df['2017-10'] df['2017-10-10':]
# 分别为找出2017年的数据，2017年十月份的数据， 从2017年十月十号开始的数据



df = df.transpose()
# 将df 整个表格转置
df.describe()
# 对df的每一行进行操作，得出 count个数， mean std min 0.25 0.50 0.75 max这几个数据

index=pd.date_range('1/1/2017', periods=365)
#  快速生成日期


