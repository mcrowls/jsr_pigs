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


print(revenue_data)


data = revenue_data[3]
print(data)
selling_policy = data['[1, 257]']

revenue = data['rev']
sold = data['sold']
height = revenue/(sold*100)
bars = selling_policy.tolist()
print(bars)
y_pos = np.arange(len(bars))
plt.bar(y_pos, height)
plt.xticks(np.arange(len(bars)), (bars),fontsize=7, rotation=45)
plt.yticks(np.arange(0, max(height)+10,max(height)/6))
plt.xlabel('selling policies[days between selling, numbers sold at selling]')
plt.ylabel('nominal pig value')
plt.show()

plt.boxplot(height,showfliers=False)
plt.ylabel('revenue (hundereds of millions)')
plt.xticks([])
plt.show()
