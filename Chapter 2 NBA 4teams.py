import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

df = pd.read_excel('Heat.xls')

Heat = df[df['Team'] =='Miami Heat'].sort_values(by='Season', ascending=False).reset_index()
Buck = df[df['Team'] == 'Milwaukee Bucks'].sort_values(by='Season', ascending =False).reset_index()
Lackers = df[df['Team'] == 'Los Angeles Lakers'].sort_values(by='Season', ascending=False).reset_index()
Rockets = df[df['Team'] == 'Houston Rockets'].sort_values(by='Season',ascending=False).reset_index()

Heat_max = Heat.sort_values(by='WIN RATE', ascending = False).reset_index()
Heat_max_Season = Heat_max.iloc[0]['Season']
Heat_max_Winrate = Heat_max.iloc[0]['WIN RATE']

Buck_max = Buck.sort_values(by='WIN RATE', ascending = False).reset_index()
Buck_max_Season = Buck_max.iloc[0]['Season']
Buck_max_Winrate = Buck_max.iloc[0]['WIN RATE']

Lackers_max = Lackers.sort_values(by='WIN RATE', ascending = False).reset_index()
Lackers_max_Season = Lackers_max.iloc[0]['Season']
Lackers_max_Winrate = Lackers_max.iloc[0]['WIN RATE']

Rockets_max = Rockets.sort_values(by='WIN RATE', ascending = False).reset_index()
Rockets_max_Season = Rockets_max.iloc[0]['Season']
Rockets_max_Winrate = Rockets_max.iloc[0]['WIN RATE']

plt.figure()


Win = df[df['Finals Result'] == 'LEAGUE CHAMPION']
Win_index = []
for i in Win.index:
    if i <= len(Heat):
        Win_index.append(i)
    if (i > len (Heat)) & (i <=2*len(Heat)):
        i = i-len(Heat)
        Win_index.append(i)
    if (i > 2*len(Heat)) & (i <= 3*len(Heat)):
        i = i-2*len(Heat)
        Win_index.append(i)


x_axis = range(len (Heat['Season']))

 
plt.plot(x_axis,Heat['WIN RATE'],'-',alpha=0.8)
plt.plot(x_axis,Buck['WIN RATE'],'-',alpha=0.8)
plt.plot(x_axis,Lackers['WIN RATE'],'-',alpha=0.8)
plt.plot(x_axis,Rockets['WIN RATE'],'-',alpha=0.8)

plt.plot( Win_index,Win['WIN RATE'], 'om' )

win_total = pd.DataFrame()
Win = Win.reset_index()
win_total['id'] = Win_index
win_total['Team'] = Win['Team']
win_total['WIN RATE'] = Win['WIN RATE']
win_total['Season']  = Win ['Season']
for i in range(len(win_total)):
    plt.text(win_total.iloc[i]['id'], win_total.iloc[i]['WIN RATE'], win_total.iloc[i]['Team']+'\n'+win_total.iloc[i]['Season'], size = 8 )


plt.legend(['Miami Heat','Milwaukee Buck','Los Angeles Lackers','Houston Rockets','League Champion'],loc=2)
x_index = [0,7,15,23,31]
x_new = ['2019-20', '2012-13', '2004-05', '1996-97', '1988-89']
plt.xticks(x_index, x_new)
plt.grid(axis='y',linestyle='-.',alpha = 0.4)

plt.title('Win Rate of 4 NBA teams from Season 1989-90 to 2019-2020')
plt.xlabel('Season')
plt.ylabel('Win Rate')

plt.show()
