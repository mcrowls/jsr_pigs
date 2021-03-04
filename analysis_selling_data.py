import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
from datetime import date
import pandas as pd
import random
import ast

rev_datas = []

revenue_data = [pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/TotalEarningsData/formatted/Gompertz1Earnings.csv'),pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/TotalEarningsData/formatted/Gompertz2Earnings.csv')
,pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/TotalEarningsData/formatted/LinearEarnings.csv'),pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/TotalEarningsData/formatted/Logistic1Earnings.csv')
,pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/TotalEarningsData/formatted/Logistic2Earnings.csv')]

titles = ['Gompertz model dataset 1','Gompertz model dataset 2','linear model', 'logistic model dataset 1', 'logistic model dataset 2']
markers = ['o','o','s','x','x']


i = 0
for data in revenue_data:
    data = data[:-35]
    selling_policy = data['[1, 257]']

    revenue = data['rev']
    sold = data['sold']
    height = revenue/(sold*100)
    bars = selling_policy.tolist()
    y_pos = np.arange(len(bars))
    #plt.bar(y_pos, height)
    #plt.plot(y_pos,height,label=titles[i],marker=markers[i])
    plt.plot(y_pos,height,label=titles[i],marker=markers[i])
    i+=1

ic = 0
for item in bars:
    if (ic+1)%2 == 0:
        bars[ic] = ''

    ic+=1
print(bars)


plt.xticks(np.arange(len(bars)), (bars),rotation=45)
plt.yticks(np.arange(0, int(max(height)+50),int(max(height))/10))
plt.xlabel('selling policies[days between selling, numbers sold at selling]')
plt.ylabel('Average price of pig (Sterling, £)', fontsize=12)
plt.legend(loc='best')
plt.ylim(90,160)
plt.show()


'''
    plt.boxplot(height,showfliers=False)
    plt.ylabel('revenue (hundereds of millions)')
    plt.xticks([])
    plt.show()
'''
