import scipy.optimize as opt
import numpy as np

def cos_x(x, a, b, d):
    return a*np.cos((b*x))+d

def find_growth_rates(cos_x):
    days_since_year = [1, 22, 35, 56, 63, 70, 105, 119, 147, 161, 175, 189]
    growth_rates = [0.0520, 0.0506, 0.0376, 0.0296, 0.0363, 0.0301, 0.0250, 0.0258, 0.0221, 0.0215, 0.0195, 0.0202]
    for j in range(1, 4):
        for i in range(np.size(days_since_year)):
            days_since_year.append(days_since_year[i]- j*365)
            growth_rates.append(growth_rates[i])

    amplitude = (np.max(growth_rates)-np.min(growth_rates))/2
    initials = [amplitude, 2*np.pi/365, 2*amplitude]
    curve_fit = opt.curve_fit(cos_x, days_since_year, growth_rates, p0=initials)
    xs = np.linspace(np.min(days_since_year), np.max(days_since_year), 10000)
    ys = cos_x(xs, curve_fit[0][0], curve_fit[0][1], curve_fit[0][2])
    a,b,d = curve_fit[0][0], curve_fit[0][1], curve_fit[0][2]
    return a,b,d
