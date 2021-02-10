from functions import *
import matplotlib.pyplot as plt
import numpy as np
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


growth_rates = np.linspace(0, 1, 10000)
# The days vary between 0 and 320 depending on the time of year.
mean_days_to_mid = sum(days_from_birth_to_mid)/len(days_from_birth_to_mid)
x1 = np.linspace(0, mean_days_to_mid, 10000)
x2 = np.linspace(mean_days_to_mid,350, 10000)

shift = 30
lowest_error_gombertz1, growth_rate_gombertz1 = minimise_error_gombertz(days_from_birth_to_wean, weaning_weights, growth_rates,shift)
lowest_error_logistic1, growth_rate_logistic1 = minimise_error_logistic(days_from_birth_to_wean, weaning_weights, growth_rates,shift)
lowest_error_gombertz2, growth_rate_gombertz2 = minimise_error_gombertz(days_from_birth_to_mid, ave_weight, growth_rates,shift)
lowest_error_logistic2, growth_rate_logistic2 = minimise_error_logistic(days_from_birth_to_mid, ave_weight, growth_rates,shift)
lowest_error_gombertz3, growth_rate_gombertz3 = minimise_error_gombertz(days_from_birth_to_death, weight_out, growth_rates,shift)
lowest_error_logistic3, growth_rate_logistic3 = minimise_error_logistic(days_from_birth_to_death, weight_out, growth_rates,shift)

# need to weight the 3 different predictions accordingly based on accuracy of data
lowest_error_gombertz = (lowest_error_gombertz1 + lowest_error_gombertz2)/2
lowest_error_logistic = (lowest_error_logistic1 + lowest_error_logistic2)/2
growth_rate_gombertz = (growth_rate_gombertz1 + growth_rate_gombertz2)/2
growth_rate_logistic = (growth_rate_logistic1 + growth_rate_logistic2)/2
print(lowest_error_gombertz1,lowest_error_gombertz2,lowest_error_gombertz3)
y_gombertz = gombertz(x1, growth_rate_gombertz,shift) # 30 corresponds to the first shift (days since weaning)
y_logistic = logistic(x1, growth_rate_logistic,shift)

mean_ave_weight = sum(ave_weight)/len(ave_weight)

shift = mean_ave_weight
y_gombertz1 = gombertz(x2, growth_rate_gombertz3 ,shift)
y_logistic1 = logistic(x2, growth_rate_logistic3 ,shift)


plt.scatter(days_from_birth_to_wean, weaning_weights, label='weaning')
plt.scatter(days_from_birth_to_mid, ave_weight, label='mid weights')
plt.scatter(days_from_birth_to_death, weight_out, label='selling')
plt.plot(x1, y_gombertz, label='gombertz model. Growth rate = '+str(growth_rate_gombertz)[0:6],color='blue')
plt.plot(x1, y_logistic, label='logistic model. Growth rate = '+str(growth_rate_logistic)[0:6],color="orange")
plt.plot(x2, y_gombertz1,color='blue')
plt.plot(x2, y_logistic1,color='orange')
#plt.plot(x2, y_gombertz1, label='gombertz model. Growth rate = '+str(growth_rate_gombertz)[0:6],color='blue')
#plt.plot(x2, y_logistic1, label='logistic model. Growth rate = '+str(growth_rate_logistic)[0:6],color='orange')

plt.xlabel('days since birth')
plt.ylabel('weight (kg)')
plt.legend(loc='best')
plt.show()
