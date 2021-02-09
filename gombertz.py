from functions import *
import matplotlib.pyplot as plt
import numpy as np


weaning_csv = pd.read_csv('C:/Users/charl/GitHub/jsr_pigs/Weaning/08-July-Weaning.csv')
weight_csv = pd.read_csv('C:/Users/charl/GitHub/jsr_pigs/Weights/08-July-Weights.csv')

birth_dates = weaning_csv['Date Served']
weaning_dates = weaning_csv['Weaning Date']
date_farrowed = [27, 1, 2020]
weaning_date_days = calc_days(date_farrowed)

pig_weights = weight_csv['Average Weight']
selling_dates = get_selling_dates(weight_csv['Date Sold'])
weaning_to_selling = []

# This for loop gets the days between weaning and selling
for i in range(np.shape(selling_dates)[0]):
    days = calc_days(selling_dates[i])
    num_days = days - weaning_date_days
    weaning_to_selling.append(num_days)


print(shift_from_weaning_weight(10))

growth_rates = np.linspace(0, 1, 10000)
# The days vary between 0 and 320 depending on the time of year.
x = np.linspace(0, 320, 10000)
lowest_error_gombertz, growth_rate_gombertz = minimise_error_gombertz(weaning_to_selling, pig_weights, growth_rates)
lowest_error_logistic, growth_rate_logistic = minimise_error_logistic(weaning_to_selling, pig_weights, growth_rates)
print(lowest_error_gombertz)
print(lowest_error_logistic)
y_gombertz = gombertz(x, growth_rate_gombertz)
y_logistic = logistic(x, growth_rate_logistic)
plt.scatter(30, 10, label='weaning')
plt.scatter(weaning_to_selling, pig_weights, label='selling')
plt.plot(x, y_gombertz, label='gombertz model. Growth rate = '+str(growth_rate_gombertz)[0:6])
plt.plot(x, y_logistic, label='logistic model. Growth rate = '+str(growth_rate_logistic)[0:6])
plt.xlabel('days since birth')
plt.ylabel('weight (kg)')
plt.legend(loc='best')
plt.show()


# export weights and days
output = np.array((x, y_gombertz, y_logistic))
print(output)
np.savetxt("gombertz_growth_data.csv", output, delimiter=",")