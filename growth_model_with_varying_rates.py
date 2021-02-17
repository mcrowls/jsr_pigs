from functions import *
from growth_rate_functions import *
import math
import scipy.optimize as opt



def cos_x(x, a, b, d):
    return a*np.cos((b*x))+d


def coeffs_growth_rate(days_since_year, growth_rates):
    amplitude = (np.max(growth_rates)-np.min(growth_rates))/2
    initials = [2*amplitude, 2*math.pi/365, 2*amplitude]
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
