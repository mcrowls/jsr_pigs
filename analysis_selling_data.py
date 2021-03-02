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


for data in revenue_data:
    selling_policy = data['[1, 257]']
    revenue = data['0']
    height = revenue
    bars = selling_policy.tolist()
    print(bars)
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(np.arange(len(bars)), (bars),fontsize=8, rotation='vertical')
    plt.yticks(np.arange(0, max(height)+1000,max(height)/6))
    plt.xlabel('selling policies')
    plt.ylabel('revenue')
    plt.show()
