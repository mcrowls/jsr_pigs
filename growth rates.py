import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np


def inverse_x(x, a, b):
    return (a*np.log(x))+b


days_since_year = [1, 22, 35, 56, 63, 70, 105, 119, 147, 161, 175, 189]
growth_rates = [0.0520, 0.0506, 0.0376, 0.0296, 0.0363, 0.0301, 0.0250, 0.0258, 0.0221, 0.0215, 0.0195, 0.0202]


curve_fit = opt.curve_fit(inverse_x, days_since_year, growth_rates)
print(curve_fit)
xs = np.linspace(1, 200, 10000)
ys = inverse_x(xs, curve_fit[0][0], curve_fit[0][1])
plt.plot(xs, ys)
plt.scatter(days_since_year, growth_rates)
plt.xlabel('Days since the start of the year when weaning begins')
plt.ylabel('Growth Rate for this group of pigs (a.u)')
plt.show()

