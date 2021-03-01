import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
from datetime import date
import pandas as pd
import random
import ast


revenue_data = pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/SoldPigsInfofor70SellingPoliciesusingLogistic1GrowthModel/totalEarningsDataLogistic_1.csv')
log = pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/logistic1.csv')

print(log)

selling_policys = log['pol']
print(selling_policys)
revenue = log['rev']
print(revenue)
'''
revenue = revenue_data.iloc[2][2:]
print(revenue)
pigs_sold = revenue_data.iloc[3][2:]

num_days_between_selling = []
num_pigs_at_selling = []
selling_policy = []
for x in selling_policys[2:]:
    xnew = ast.literal_eval(x)
    num_days_between_selling.append(xnew[0])
    num_pigs_at_selling.append(xnew[1])
    selling_policy.append(xnew)
'''

'''

plt.plot(num_days_between_selling, revenue, label='days between')
plt.plot(num_pigs_at_selling, revenue, label='pigs at selling')
plt.xlabel('days between selling/num pigs at selling')
plt.ylabel('revenue')
plt.legend(loc='best')
plt.show()

#plt.scatter(days_from_birth_to_mid, ave_weight, label='mid weights')
#plt.scatter(days_from_birth_to_death, weight_out, label='selling')
#plt.plot(xs, y_lin, label='logistic model',color="orange")

#Axes3D.scatter(xs=num_days_between_selling, ys=num_pigs_at_selling, zs=revenue

'''
height = revenue
bars = selling_policys
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
#plt.xticks(np.arange(bars), ('G1', 'G2', 'G3', 'G4', 'G5'))
#plt.yticks(np.arange(0, 81, 10))
plt.xlabel('selling policies', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')
plt.ylabel('revenue')
plt.show()
'''
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = selling_policys[2:]
students = revenue
ax.bar(langs,students)
plt.xlabel('selling policy')
plt.ylabel('revenue')
plt.legend(loc='best')
ax.set_xticklabels(langs)
ax.set_yticks([0,10000,20000,30000,40000])
plt.show()



Axes3D.plot_wireframe(num_days_between_selling,num_pigs_at_selling, revenue, rstride=10, cstride=10)
plt.xlabel('days between selling')
plt.ylabel('revenue')
plt.legend(loc='best')
plt.show()
revenue = revenue.tolist()

dict = {'days':num_days_between_selling, 'num pigs':num_pigs_at_selling, 'rev':revenue}
df = pd.DataFrame(dict)
print(df)

flights = df
flights = flights.pivot("days", "num pigs", "revenue")
ax = sns.heatmap(flights)

'''
