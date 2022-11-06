"""
Happy World
===========

Every year since 2005, the World Happiness Report has analysed the results of the Gallup World Poll, 
which is carried out in 160 countries (covering 99% of the world’s population). 
The pollsters contact a random sample of people in each country and ask them over 
100 questions – about their income, their health and their family. These questions include the 
following question about happiness:::

All things considered, how satisfied are you with your life as a whole these days? Use a 0 to 10 scale, 
where 0 is dissatisfied and 10 is satisfied to give your answer.

People living in different countries give different answers. In the UK is 6.94, making the UK 17th in the world for happiness. 
The top ranked country – rather surprisingly given a national stereotype of people who are reserved and don’t express their 
feelings very much – is Finland, with a score of 7.82. In general, Scandinavian and Northern European countries are 
ranked highest. The USA is 16th (0.03 points ahead of the UK). China, with a score of 5.59 and at 72nd place, is 
roughly in the middle of the table of the countries surveyed. Other mid-ranked countries include Montenegro, Ecuador, 
Vietnam and Russia. Further down the table, we find many African – Uganda and Ethiopia placed 117th and 131st, 
respectively – and Middle Eastern countries – Iran is at 110 and Yemen at 132.  
The unhappiest country in the world in 2022 is Afghanistan, with an average happiness score of only 2.40.

The code below plots the average life expectancy of each of these countries against their happiness scores. 

"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Read in the data
happy = pd.read_csv("../data/HappinessData.csv",delimiter=';') 
happy.rename(columns = {'Social support':'SocialSupport'}, inplace = True) 
happy.rename(columns = {'Life Ladder': 'LifeLadder'}, inplace = True) 
happy.rename(columns = {'Perceptions of corruption':'Corruption'}, inplace = True) 
happy.rename(columns = {'Log GDP per capita': 'LogGDP'}, inplace = True) 
happy.rename(columns = {'Healthy life expectancy at birth': 'LifeExp'}, inplace = True) 
happy.rename(columns = {'Freedom to make life choices': 'Freedom'}, inplace = True) 

# Preview the first 5 lines of the loaded data for 2018
df=happy.loc[happy['Year'] == 2018]
df.head()
print(df.head())

##############################################################################
# Each circle in the plot is a country. 
# The x-axis shows the life expectancy in the country and 
# the y-axis shows the average ranking of life-satisfaction, 
# on the 0 to 10 scale. In general, the higher the life expectancy of a country, 
# the higher the happiness there. 


from pylab import rcParams
rcParams['figure.figsize'] = 6/2.54, 6/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)


fig,ax=plt.subplots(num=1)

ax.plot('LifeExp','LifeLadder', data=df, linestyle='none', markersize=2, marker='o', color=[0.85, 0.85, 0.85])
for country in ['United States','United Kingdom','Croatia','Benin','Finland','Yemen']:
    ci=np.where(df['Country name']==country)[0][0]
    ax.plot(  df.iloc[ci]['LifeExp'],df.iloc[ci]['LifeLadder'], linestyle='none', markersize=3, marker='o', color='black')
    if country=='United Kingdom':
        ax.text(  df.iloc[ci]['LifeExp']+0.5,df.iloc[ci]['LifeLadder'],  'UK')
    else:
        ax.text(  df.iloc[ci]['LifeExp']+0.5,df.iloc[ci]['LifeLadder']+0.08,  country)
       
ax.set_xticks(np.arange(30,90,step=5))
ax.set_yticks(np.arange(11,step=1))
ax.set_ylabel('Average Happiness (0-10)')
ax.set_xlabel('Life Expectancy at Birth')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(47,78)
ax.set_ylim(2.5,8.1) 
plt.show()

##############################################################################
# Each circle in the plot is a country. 
# The x-axis shows the life expectancy in the country and 
# the y-axis shows the average ranking of life-satisfaction, 
# on the 0 to 10 scale. In general, the higher the life expectancy of a country, 
# the higher the happiness there. 
