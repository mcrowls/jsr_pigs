from functions import *
from growth_model_with_varying_rates import *
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import scipy.stats as stats


weight_csv = pd.read_csv('Weight_Data.csv')
grouped_dates = group_dates_together(weight_csv)


growth_rate_array = []
time_since_start_of_year = []

for month in grouped_dates:
    dates = []
    days_post = []
    days_in = []
    number_of_pigs = []
    ave_weight = []
    ave_P2 = []
    weight_out = []
    for i in range(np.shape(month)[0]):
        dates.append(get_individual_date(month[i]['Date']))
        days_post.append(month[i]['Days Post Wean'])
        days_in.append(month[i]['Days in'])
        number_of_pigs.append(month[i]['Number pigs'])
        ave_weight.append(month[i]['Average Weight'])
        ave_P2.append(month[i]['P2'])
        weight_out.append(month[i]['Weight Out'])
    days = []
    weights = []
    days_from_birth_to_wean = []
    days_from_birth_to_mid = []
    weaning_weights = []
    days_from_birth_to_death = []
    for i in range(np.size(days_post)):
        days_from_birth_to_wean.append(30)
        days.append(days_from_birth_to_wean[i])
        weights.append(7)
        # change so picks form a normal distribution  of weaning weights
        days_from_birth_to_mid.append(days_post[i] + 30) # days taken to wean
        days.append(days_from_birth_to_mid[i])
        weights.append(ave_weight[i])
        days_from_birth_to_death.append(days_from_birth_to_mid[i] + days_in[i])
        days.append(days_from_birth_to_death[i])
        weights.append(weight_out[i])
    reference_days = calc_days([1, 1, 2020])
    days_array = []
    tot = []
    for date in dates:
        days_since_start_of_year = 30*date[1] + date[0] - days_from_birth_to_death[i] + days_from_birth_to_mid
        tot.append(days_since_start_of_year)
    ave = np.mean(tot)
    time_since_start_of_year.append(ave)


    growth_rates = np.linspace(0, 1, 10000)
    shift = 30
    xs = []
    ys = []
    for i in range(np.shape(month)[0]):
        xs.extend((30, days_from_birth_to_mid[i], days_from_birth_to_death[i]))
        ys.extend((7, ave_weight[i], weight_out[i]))
    rmse, growth_rate = minimise_error_gombertz(xs, ys, growth_rates, shift)
    growth_rate_array.append(growth_rate)
    x_plot = np.linspace(0, 350, 1000)
    y_plot = gombertz(x_plot, growth_rate, shift)
    #markers, caps, bars = plt.errorbar(x_plot, y_plot, xerr=None, yerr=rmse, ecolor=None)
    #plt.scatter(days, weights, label='gr = '+str(growth_rate)[0:6])
    #plt.plot(x_plot, y_plot)

    #[bar.set_alpha(0.02) for bar in bars]
    #[cap.set_alpha(0.02) for cap in caps]


mean = np.mean(growth_rate_array)
var = np.var(growth_rate_array)
print(mean)
print(var)
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
plt.ylim(0, 1500)
plt.xlabel('growth rate (a.u)')
plt.ylabel('frequency')
plt.show()
