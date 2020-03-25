import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import  MultipleLocator


# 1. 2005-2014年从多个气象站获取的数据中，找出，这十年来每一天所对应的十年每天最高气温和最低气温，并绘图
# 2. 找出2015年每天的最高气温和最低气温
# 3. 在 1 中得到的图中标出，2015年打破前十年最高温和最低温记录的日子和其对应温度


get_ipython().magic('matplotlib notebook')
df=pd.read_csv('data/C2A2_data/BinnedCsvs_d400/6bfe451be8ad7abced396241683a69ba88103e019d15e945a56d0d05.csv')
ab=df.copy()


# ------------------------------------------------------------2005-2014
# 先从表格中筛选出2014年以前的数据，并找出element列中，最高温和最低温所在的行
df=df.sort_values(by='Date')[df['Date']<='2014-12-31']
df_Tmax=df[df['Element']=='TMAX']
df_Tmin=df[df['Element']=='TMIN']

# 按照date分组，并对datavalue相应列 采取max 和 min函数，求出每天中的最高气温和最低气温
df_Tmax=df_Tmax.groupby('Date').agg({'Data_Value':max})
df_Tmin=df_Tmin.groupby('Date').agg({'Data_Value':min})
df_Tmax=df_Tmax.reset_index()
df_Tmin=df_Tmin.reset_index()



# 将Date列中的数据变成时间标准格式。 这里是 月份.日期
df_Tmin['Date']=pd.to_datetime(df_Tmin['Date'])
df_Tmax['Date']=pd.to_datetime(df_Tmax['Date'])
df_Tmin['Date']=df_Tmin['Date'].dt.strftime('%m.%d')
df_Tmax['Date']=df_Tmax['Date'].dt.strftime('%m.%d')


# 按照data重新整理数据
df_Tmin=df_Tmin.groupby('Date').agg({'Data_Value':min})
df_Tmax=df_Tmax.groupby('Date').agg({'Data_Value':max})
# 去除掉02.29， 避免闰年平年的区别
df_Tmin=df_Tmin.drop('02.29')
df_Tmax=df_Tmax.drop('02.29')
df_Tmin=df_Tmin.reset_index()
df_Tmax=df_Tmax.reset_index()




#----------------------------------------2015年数据整理方式同上
ab = ab.sort_values(by='Date')[ab['Date'].str.contains('2015')]
ab_Tmax=ab[ab['Element']=='TMAX']
ab_Tmin=ab[ab['Element']=='TMIN']

ab_Tmax=ab_Tmax.reset_index()
ab_Tmin=ab_Tmin.reset_index()

ab_Tmin['Date']=pd.to_datetime(ab_Tmin['Date'])
ab_Tmax['Date']=pd.to_datetime(ab_Tmax['Date'])
ab_Tmin['Date']=ab_Tmin['Date'].dt.strftime('%m.%d')
ab_Tmax['Date']=ab_Tmax['Date'].dt.strftime('%m.%d')

ab_Tmin=ab_Tmin.groupby('Date').agg({'Data_Value':min})
ab_Tmax=ab_Tmax.groupby('Date').agg({'Data_Value':max})
ab_Tmin=ab_Tmin.reset_index()
ab_Tmax=ab_Tmax.reset_index()

# -------------------------------------数据对比
# 合并表格后，对比出2015年打破纪录的日期
max_2015 = pd.merge (df_Tmax, ab_Tmax,how = 'inner',left_on='Date',right_on='Date')
max_2015 = max_2015[max_2015['Data_Value_x'] < max_2015['Data_Value_y']]
min_2015 = pd.merge(df_Tmin, ab_Tmin, how = 'inner',left_on='Date',right_on='Date')
min_2015 = min_2015[min_2015['Data_Value_x'] > min_2015['Data_Value_y']]



# --------------------------------------------------------------画图

date = df_Tmax['Date']
max_2015_list_y = max_2015['Data_Value_y']
min_2015_list_y = min_2015['Data_Value_y']

# 当横坐标为文本时，所采取的方法
pos = np.arange(len(df_Tmax['Date']))

# 为找出图像中打破记录的对应日期，采用如下方法
pos_max = []
for i in max_2015['Date']:
    for j in df_Tmax['Date']:
        if i == j:
            a = df_Tmax[df_Tmax['Date']==j].index.values[0] # 获取相应数值的index的 int形式数值
            pos_max.append(a)            
pos_min = []
for i in min_2015['Date']:
    for j in df_Tmin['Date']:
        if i == j:
            a = df_Tmin[df_Tmin['Date']==j].index.values[0]
            pos_min.append(a)


# 画图并标出打破纪录的点
plt.figure()
plt.plot(pos,df_Tmax['Data_Value'],'-',pos,df_Tmin['Data_Value'],'-')
plt.scatter(pos_max,max_2015_list_y,c='red')
plt.scatter(pos_min,min_2015_list_y,c='gray')

# 添加标注 
plt.legend(['High Temperature','Low Temerature','Break points in 2015(High)','Break points in 2015(Low)'])

# 按照一定间隔显示横坐标
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
DayOfMonth=[1,32,60,91,121,152,182,213,244,274,305,335]
plt.xticks(DayOfMonth,month,alpha=0.8)

# 画出十年间最高温和最低温之间的阴影
plt.gca().fill_between(range(len(pos)), 
                       df_Tmax['Data_Value'], df_Tmin['Data_Value'],
                       facecolor='green', 
                       alpha=0.25)
# 添加标题
plt.title('Low and High temperature between 2005-2014\n With break points in 2015    Boston,MA')


# 将纵坐标改为摄氏度的形式
pos,labels=plt.yticks()
newpos=[]
newpos2=[]
for i in pos:
    newpos.append(str(int(i/10))+u'\N{DEGREE SIGN}'+'C')
    newpos2.append(str(int(i/10*1.8+32))+u'\N{DEGREE SIGN}'+'F')

plt.yticks(pos,newpos)


# 保留横纵坐标，删除刻度线
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')