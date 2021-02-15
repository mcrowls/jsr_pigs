from functions import *
import math
import scipy.optimize as opt


def cos_x(x, a, b, d):
    return a*np.cos((b*x))+d


def coeffs_growth_rate():
    days_since_year = [1, 22, 35, 56, 63, 70, 105, 119, 147, 161, 175, 189]
    growth_rates = [0.0520, 0.0506, 0.0376, 0.0296, 0.0363, 0.0301, 0.0250, 0.0258, 0.0221, 0.0215, 0.0195, 0.0202]
    for j in range(1, 3):
        for i in range(np.size(days_since_year)):
            days_since_year.append(days_since_year[i]- j*365)
            growth_rates.append(growth_rates[i])
    amplitude = (np.max(growth_rates)-np.min(growth_rates))/2
    initials = [2*amplitude, math.pi/365, 2*amplitude]
    curve_fit = opt.curve_fit(cos_x, days_since_year, growth_rates, p0=initials)
    return curve_fit[0]


weight_data = pd.read_csv('Weight_Data.csv')
selling_dates = get_selling_dates(weight_data['Date'])

days_in_building = weight_data['Days in']
days_after_weaning = weight_data['Days Post Wean']

reference_days = calc_days([1, 1, 2020])
days_array = []
for date in selling_dates:
    days = calc_days(date)
    days_since_ref = days - reference_days
    days_array.append(days_since_ref)
