def answer_one():
    
    import pandas as pd
    import numpy as np
    import re


    # Energy 

    x = pd.read_excel('Energy Indicators.xls', skiprows=17, skipfooter=38) 
    # 删除前17行，后38行的没用数据    
    energy = x.copy().drop(x.columns[[0,1]], axis=1) 
    # 删除前两列
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # 直接对剩下的四列进行命名
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy = energy.replace('...',np.NaN)

    country = []
    for i in list(energy['Country']):
        i = re.sub('\d+', '', i)
        # 删除所有的数字
        i = re.sub('\(.*\)', '', i)
        # 删除所有括号里面的内容
        i = i.rstrip()
        # 删除字符串右面的空格，lstrip是删除左面，strip是删除两边
        country.append(i)
    energy['Country'] = country
    # 这种方法可以直接用一整个list对一列进行赋值
    
    energy = energy.replace(to_replace=['...', 'Republic of Korea', 'United States of America',
                                         'United Kingdom of Great Britain and Northern Ireland',
                                         'China, Hong Kong Special Administrative Region'],
                              value=[np.NaN, 'South Korea', 'United States', 'United Kingdom', 'Hong Kong'])
    # 当需要替换很多个目标时，可以用这个方法

        
    # GDP 
    y = pd.read_csv('world_bank.csv', skiprows=3, header = 1)
    # 跳过前三行， 并设置第一行为列的名字
    gdp = y.copy()
    gdp.rename(columns={'Country Name':'Country'}, inplace= True)
    

    gdp=gdp.replace(to_replace=['Korea, Rep.', 'Iran, Islamic Rep.', 'Hong Kong SAR, China']
                       ,value=['South Korea', 'Iran','Hong Kong'])

   
    
    
    # Sci
    z = pd.read_excel('scimagojr-3.xlsx')
    sci = z.copy()



    
    # Zusammen
    w1 = pd.merge(sci,energy,on='Country',how = 'outer')
    w2 = pd.merge(w1 , gdp, on='Country', how = 'outer')
    columns = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', 
               '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

    w2.index = w2['Country']
    w2 = w2[columns]
    # 可以直接获取想要的列
    
    w2.sort_values(by='Rank', inplace = True)
    
    w2 = w2.iloc[0:15]
    columns = ['Rank','Documents','Citable documents','Citations','Self-citations','H index']

    w2[columns] =w2[columns].astype(int)
    w2['Energy Supply'] = w2['Energy Supply'].astype(float)
    w2['Energy Supply per Capita'] = w2['Energy Supply per Capita'].astype(float)
    # 将DataFrame中的数据类型强制转换成想要的数据类型


    
    
    
    #  求最大值以及global的用法

    global census_df                     # 这个地方为了能内部直接调用外部的变量，需要用global
    df7 = census_df.copy()               # 为了防止函数对源文件做出改变，需要用copy函数
    info_list = []
    maxnum = 0
    
    CTYNAME_LIST = df7['CTYNAME'].unique()
    df7 = df7.set_index('CTYNAME')
    for i in CTYNAME_LIST:
        dic = {'name' : i,
              '2010' : df7.loc[i, 'POPESTIMATE2010'],
              '2011' : df7.loc[i, 'POPESTIMATE2011'],
              '2012' : df7.loc[i, 'POPESTIMATE2012'],
              '2013' : df7.loc[i, 'POPESTIMATE2013'],
              '2014' : df7.loc[i, 'POPESTIMATE2014'],
              '2015' : df7.loc[i, 'POPESTIMATE2015']}
        a = dic['2010']       # abcdef这个地方输出的type是 numpy.int64，不能做成list，然后用list的max*函数
                              # 不止如此，求最大值最小值平局值等等，都要用向量的方法
        b = dic['2011']
        c = dic['2012']
        d = dic['2013']
        e = dic['2014']
        f = dic['2015']
        
        numlist = np.array([a,b,c,d,e,f])  # 应该把abcdef做成一个新的数组。然后用向量的最大值函数
        maxnum = numlist.max()
        minnum = numlist.min()
        change = maxnum - minnum
        
        dic['change'] = change
        info_list.append(dic)
    for ii in range(0,len(info_list)):
        if info_list[ii]['change'] > maxnum:
            maxnum = info_list[ii]['change']
            name = info_list[ii]['name']
        else: maxnum = maxnum 


    return w2




