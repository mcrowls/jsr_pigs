from functions import *
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats

growth_rates_yeno_da = []
avg_days = []

datey_bois = ['01-Jan', '04-March', '05-Feb', '08-July', '10-June', '11-March', '15-April', '22-Jan', '24-June', '26-Feb', '27-May', '29-April']
for date in datey_bois:
    weaning_csv = pd.read_csv('weaning/'+str(date)+'-Weaning.csv')
    weight_csv = pd.read_csv('Weights/'+str(date)+'-Weights.csv')

    birth_dates = weaning_csv['Date Served']
    weaning_dates = weaning_csv['Weaning Date']
    weaning_date_days = calc_days(get_dates(weaning_dates)[0])

    pig_weights = weight_csv['Average Weight']
    selling_dates = get_selling_dates(weight_csv['Date Sold'])
    weaning_to_selling = []

    # This for loop gets the days between weaning and selling
    for i in range(np.shape(selling_dates)[0]):
        days = calc_days(selling_dates[i])
        num_days = days - weaning_date_days
        weaning_to_selling.append(num_days)

    avg_days.append(np.mean(weaning_to_selling))
    #print(shift_from_weaning_weight(10))

    growth_rates = np.linspace(0, 1, 10000)
    # The days vary between 0 and 320 depending on the time of year.
    x = np.linspace(0, 320, 10000)
    lowest_error_logistic, growth_rate_logistic = minimise_error_logistic(weaning_to_selling, pig_weights, growth_rates, 30)
    growth_rates_yeno_da.append(growth_rate_logistic)
    y_logistic = logistic(x, growth_rate_logistic, 30)
    '''
    plt.scatter(30, 10, label='weaning')
    plt.scatter(weaning_to_selling, pig_weights, label='selling')
    plt.plot(x, y_logistic, label='logistic model. Growth rate = '+str(growth_rate_logistic)[0:6])
    plt.xlabel('days since birth')
    plt.ylabel('weight (kg)')
    plt.legend(loc='best')
    '''
mean = np.mean(growth_rates_yeno_da)
var = np.var(growth_rates_yeno_da)
sigma = math.sqrt(var)
x = np.linspace(mean - 4*sigma, mean + 4*sigma, 1000)
y = stats.norm.pdf(x, mean, sigma)
print(y)
mean_xs = [mean, mean]
mean_ys = [0, np.max(y)]
plt.plot(x, y, label='Normal Distribution')
plt.plot(mean_xs, mean_ys, label='Mean')
plt.legend(loc='best')
#plt.scatter(all_days, all_weights)
# plt.plot(x, y)
'''
plt.ylim(0, 240)
plt.legend(loc='best')
plt.xlabel('Days of growth')
plt.ylabel('Weight(kg)')
'''
plt.ylim(0, 250)
plt.xlabel('growth rate (a.u)')
plt.ylabel('frequency')
plt.show()
