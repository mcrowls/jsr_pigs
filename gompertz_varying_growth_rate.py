from functions import *
from growth_rate_functions import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import random


weight_csv = pd.read_csv('Weight_Data.csv')

dates = weight_csv['Date']
days_post = weight_csv['Days Post Wean']
days_in = weight_csv['Days in']
number_of_pigs = weight_csv['Number pigs']
ave_weight = weight_csv['Average Weight']
ave_P2 = weight_csv['P2']
weight_out = weight_csv['Weight Out']
weaning_weight_ND = np.random.normal(7,1, 1000)


days_from_birth_to_wean = []
days_from_birth_to_mid = []
weaning_weights = []
days_from_birth_to_death = []
for i in range(np.shape(days_post)[0]):
    days_from_birth_to_wean.append(30)
    # change so picks form a normal distribution  of weaning weights
    weaning_weights.append(random.choice(weaning_weight_ND))
    days_from_birth_to_mid.append(days_post[i] + 30) # days taken to wean
    days_from_birth_to_death.append(days_from_birth_to_mid[i] + days_in[i])

weights = weaning_weights + ave_weight + weight_out
# The days vary between 0 and 320 depending on the time of year.
mean_days_to_mid = sum(days_from_birth_to_mid)/len(days_from_birth_to_mid)
xs = np.linspace(0,350, 10000)

# T is different for every pig and is simply the date since they were born
# find birth date, find death date then find date inbetween and use as growth rate
# for lot of pigs [0]
death_date = get_individual_date(dates[5])
T = days_since_jan_01(death_date,days_from_birth_to_death[5])

death_date = get_individual_date(dates[4])
T = days_since_jan_01(death_date,days_from_birth_to_death[4])

growth_rates = np.linspace(0, 1, 10000)
# returns the parameters for function of birth rates
#a,b,d = find_growth_rates(cos_x)

def y_linear(days,growth_rate):
    return growth_rate*(days-30) + 7

def CalculateWeightLogistic(t, growth_rate):
    y = 240 / (1 + 30 * np.exp(-growth_rate * t))
    return y


def CalculateWeightGompertz(t, growth_rate):
    y = 240 * np.exp(-30*np.exp(-growth_rate*t))
    return y

growth_rate = 0.725555
ms =[]
for i in range(len(days_from_birth_to_death)):
    ms.append((weight_out[i]-weaning_weights[i])/days_from_birth_to_death[i])


print(np.std(ms))

y_lin = y_linear(xs,growth_rate)
growth_rate_log = 0.018460179351268462
growth_rate_gom = 0.0209020902090209

y_log = CalculateWeightLogistic(xs,growth_rate_log)
y_gom = CalculateWeightGompertz(xs, growth_rate_gom)

plt.scatter(days_from_birth_to_wean, weaning_weights, label='weaning')
plt.scatter(days_from_birth_to_mid, ave_weight, label='mid weights')
plt.scatter(days_from_birth_to_death, weight_out, label='selling')
plt.plot(xs, y_lin, label='linear model',color="orange")
plt.plot(xs, y_log, label='logistic model',color="blue")
plt.plot(xs, y_gom, label='gompertz model',color="red")


plt.xlabel('days since birth')
plt.ylabel('weight (kg)')
plt.legend(loc='best')
plt.show()
