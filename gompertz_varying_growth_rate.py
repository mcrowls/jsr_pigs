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
<<<<<<< HEAD
death_date = get_individual_date(dates[5])
T = days_since_jan_01(death_date,days_from_birth_to_death[5])

=======
death_date = get_individual_date(dates[4])
T = days_since_jan_01(death_date,days_from_birth_to_death[4])
>>>>>>> fb60dc9b3c6c4b41aa3148093bc06a4d23fdf534

growth_rates = np.linspace(0, 1, 10000)
# returns the parameters for function of birth rates
#a,b,d = find_growth_rates(cos_x)

xi = np.linspace(0,1000, 10000)
print(growth_rate(xi,0,a,b,d))
max_growth_rate = max(growth_rate(xi,0,a,b,d))
min_growth_rate = min(growth_rate(xi,0,a,b,d))

# shift is days taken to wean
shift = 30
x = 0
<<<<<<< HEAD
y_logistic = logistic(xs,growth_rate(x,T,a,b,d),shift)
y_logistic_max = logistic(xs,max_growth_rate,shift)
y_logistic_min = logistic(xs,min_growth_rate,shift)
=======
best_growth_rate = minimise_error_logistic(xs, weights, growth_rates, shift)
y_logistic = logistic(xs, best_growth_rate, shift)
>>>>>>> fb60dc9b3c6c4b41aa3148093bc06a4d23fdf534

plt.scatter(days_from_birth_to_wean, weaning_weights, label='weaning')
plt.scatter(days_from_birth_to_mid, ave_weight, label='mid weights')
plt.scatter(days_from_birth_to_death, weight_out, label='selling')
plt.plot(xs, y_logistic, label='logistic model',color="orange")
plt.plot(xs, y_logistic_max, label='logistic model max growth rate',color="blue")
plt.plot(xs, y_logistic_min, label='logistic model min growth rate',color="red")

plt.xlabel('days since birth')
plt.ylabel('weight (kg)')
plt.title('Varying growth rate')
plt.legend(loc='best')
plt.show()