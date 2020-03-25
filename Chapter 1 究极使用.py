import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end 
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    import re
    town = pd.read_csv('university_towns.txt', sep="\n", header = None).copy()
    town.columns = ['Name of the Town']
    name = []
    state = []
    region = []
    state_region = []
    
    for i in town['Name of the Town']:  
        
        # 将town中的state和region的名字分开装在两个list中
        # 同时删除掉每个名字后面[]和其中的内容，删除 数字，删除两边的空格
        if '[ed' in i:
            i = re.sub('\\[.*?\\]', '',i)
            i = re.sub('\s+$','',i)
            i = i.strip()
            
            state.append(i)
        else:
            i = re.sub('\\[.*?\\]', '',i)
            i = i.strip()
            i = re.sub('\s+$','',i)
            region.append(i)
        name.append(i)

    # 将名字以（ 为分隔符，分成三部分，取前一部分为最终想要得到的名字部分
    for i in range(0,len(state)-1):
        for j in range(0,len(name)-1):
            if state[i] == name[j]:
                statename = state[i]
                a = 1
                while (name[j+a] != statename) & (name[j+a] != state[i+1]):
                    head, sep, tail = name[j+a].partition(' (')
                    
                    

                   
                    dic = {'State' : statename,
                          'RegionName' : head}
                    a += 1
                    
                    state_region.append(dic)
    last = re.sub('\(.*?\)','',name[len(name)-1]).strip()

    dic = {'State' : state[len(state)-1],
          'RegionName' : last }
    state_region.append(dic)
               
        
    df = pd.DataFrame(state_region)
    df = df[['State', 'RegionName']]

    # 最终该函数返回一个 有着 不含中括号 小括号以及数字的，纯粹的 美国城市和其对应州的名字的dataframe


    return df


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''


    gdp = pd.read_excel('gdplev.xls',header = 219,names = ['Time', 'GDP','GDP C','none']).copy()

    # recession开始的意思是，连续 两个 季度的GDP下降
    for i in range(0,len(gdp)-2):
        if (gdp.iloc[i+1]['GDP C'] < gdp.iloc[i]['GDP C']) & (gdp.iloc[i+2]['GDP C'] < gdp.iloc[i+1]['GDP C']) :
            a = gdp.iloc[i+1]['Time']
            break
        
    
    return  a

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    start = get_recession_start()
    gdp = pd.read_excel('gdplev.xls',header = 219, names = ['Time', 'GDP','GDP C','none'])
    end = []

    # recession结束的意思是， 连续两个季度的GDP上升
    for i in range(0,len(gdp)-2):
        if (gdp.iloc[i+1]['GDP C'] < gdp.iloc[i]['GDP C']) & (gdp.iloc[i+2]['GDP C'] < gdp.iloc[i+1]['GDP C']) :
            a = gdp.iloc[i]['Time']
            for j in range (i, len(gdp)-2):
                if (gdp.iloc[j+1]['GDP C'] > gdp.iloc[j]['GDP C']) & (gdp.iloc[j+2]['GDP C'] > gdp.iloc[j+1]['GDP C']) :
                    b = gdp.iloc[j+2]['Time']
                    break

       
    return b

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    gdp = pd.read_excel('gdplev.xls',header = 219, names = ['Time', 'GDP','GDP C','none'])

    # 下面这个循环的目的与上两个函数相同，不过输出的值略有不同，只是我懒得搞返回值了
    for i in range(0,len(gdp)-2):
        if (gdp.iloc[i+1]['GDP C'] < gdp.iloc[i]['GDP C']) & (gdp.iloc[i+2]['GDP C'] < gdp.iloc[i+1]['GDP C']) :
            a = gdp.iloc[i]['Time']
            start_po = i
            for j in range (i, len(gdp)-2):
                if (gdp.iloc[j+1]['GDP C'] > gdp.iloc[j]['GDP C']) & (gdp.iloc[j+2]['GDP C'] > gdp.iloc[j+1]['GDP C']) :
                    b = gdp.iloc[j+2]['Time']
                    end_po = j+2
                    break

    # bottom 的意思是，在一个recession中GDP最小的值
    gdplist = gdp[['Time','GDP C']][start_po-1 : end_po+1]
    gdplist = gdplist.set_index('Time')
    gdplist.sort_values(by = 'GDP C', inplace=True)#.index#['Time'][0]
    mingdp = gdplist.index[0]
#     name = gdp[gdp['GDP C']==mingdp]


    return mingdp

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    # 因为原始csv中，GDP不是以季度展示，而是以月份展示，所以要将月份按照每三个月份一个季度分开
    # 然后分完季度之后，对每个季度中的三个月份求平均值
    ilist =[]
    q1 = ['-01','-02','-03']
    q2 = ['-04','-05','-06']
    q3 = ['-07','-08','-09']
    q4 = ['-10','-11','-12']
    qqq1=[]
    price = pd.read_csv('City_Zhvi_AllHomes.csv').copy()
    a = list(range(3,51))
    price.drop(price.columns[a],axis =1 , inplace=True)
    price.drop(price.columns[0],axis =1 , inplace=True)
    for i in range(2000,2016):
        i1 = str(i) + 'q' +'1'
        i2 = str(i) + 'q' +'2'
        i3 = str(i) + 'q' +'3'
        i4 = str(i) + 'q' +'4'

        q11 = str(i) + q1[0]
        q12 = str(i) + q1[1]
        q13 = str(i) + q1[2]

        price[i1] = (price[q11] +price[q12] +price[q13])/3
        
        q21 = str(i) + q2[0]
        q22 = str(i) + q2[1]
        q23 = str(i) + q2[2]

        price[i2] = (price[q21] +price[q22] +price[q23])/3
        
        q31 = str(i) + q3[0]
        q32 = str(i) + q3[1]
        q33 = str(i) + q3[2]

        price[i3] = (price[q31] +price[q32] +price[q33])/3
        
        q41 = str(i) + q4[0]
        q42 = str(i) + q4[1]
        q43 = str(i) + q4[2]

        price[i4] = (price[q41] +price[q42] +price[q43])/3

    
    # 2016年在csv中只有8个月，所以单独拿出来处理
    price['2016q1'] = (price['2016-01'] + price['2016-02'] + price['2016-03'])/3
    price['2016q2'] = (price['2016-04'] + price['2016-05'] + price['2016-06'])/3
    price['2016q3'] = (price['2016-07'] + price['2016-08'])/2



    
    price.drop(price.columns[2:202], axis=1, inplace=True)
    price = price.set_index(['State', 'RegionName'])

    # 将CSV中的一些名字缩写改成全称
    price.rename(index = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}, inplace=True)

        
#     for i in price[2:]:
        
#     price.set_index([''])
    
    return price

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    # 这个函数的目的是对比，大学城中的住房价格和非大学城中的住房价格，在recession这个过程中，相对来说哪个更低

    from scipy import stats

    # 从上述几个函数中获取返回值
    house_price = convert_housing_data_to_quarters()
    df = get_list_of_university_towns()
    start = get_recession_start()
    end = get_recession_end()
    low = get_recession_bottom()
    
    df = df.set_index(['State','RegionName'])
    prices_begin = house_price[start]
    prices_end = house_price[end]

    
    
    ratio = prices_begin/prices_end


    # 因为df就是所有大学城的名字，所以可以直接通过df的index来获取， ration中的所有大学城的ratio  
    uni_price_ratio = ratio.loc[df.index].dropna()


    # 通过差集，直接获得非大学城的城市的名字
    not_uni = list(set(house_price.index) - set(df.index))
    not_uni_price_ratio = ratio.loc[not_uni].dropna()
    

    # null hypothesis
    sta, pvalue =stats.ttest_ind(uni_price_ratio, not_uni_price_ratio)


    # 设定的pvalue的 threshold的值为0.01，即百分之一
    if pvalue<0.01:
        different = True
    
    if sta > 0 :
        better = "non-university town"
    if sta < 0 :
        better = "university town"
    
    return different, pvalue, better


run_ttest()
