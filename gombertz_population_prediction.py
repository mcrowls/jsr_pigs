import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import *

'''
Plots the population change against time for 1st Jan weaning. Can be scaled up for all weaning populations
'''


def calc_sale_dates_df(df):
    condition = df["number born/slaughtered"] > 0
    birth_dates = df.loc[condition]
    numerical_dates = df.loc[condition, "numerical date"]
    days_growing = inverse_gombertz(7, 135, 0.0195)

    pred_numerical_dates = numerical_dates + days_growing
    pred_pop_change = -birth_dates["number born/slaughtered"]

    death_dates = pd.concat([pred_pop_change, pred_numerical_dates], axis=1)

    print(birth_dates)
    print(death_dates)
    df2 = pd.concat([birth_dates, death_dates])
    df2["number born/slaughtered"] = np.cumsum(df2["number born/slaughtered"])

    return df2


# turns 01/01/2020 into [01, 01, 2020]
def format_date(date_array):
    counter = 0
    for date in date_array:
        date_list = str(date).split('/')
        for i in [0,1,2]:
            date_list[i] = int(date_list[i])
        date_array[counter] = date_list
        counter += 1
    return date_array


real_pop_change_df = pd.read_csv('C:/Users/charl/GitHub/jsr_pigs/population-data/Weaned1janPopChange.csv')

real_pop_change = np.cumsum(real_pop_change_df["number born/slaughtered"])
real_pop_change_dates = format_date(real_pop_change_df["farrow/sale date"])

# print(real_pop_change)
# print(real_pop_change_dates)

real_numerical_dates = []
for date in real_pop_change_dates:
    real_numerical_dates.append(calc_days(date))
real_pop_change_df["numerical date"] = real_numerical_dates

pred_pop_change_df = calc_sale_dates_df(real_pop_change_df)

plt.plot(real_numerical_dates, real_pop_change)
plt.plot(pred_pop_change_df["numerical date"], pred_pop_change_df["number born/slaughtered"])
plt.xlabel('Days since 2nd Dec first birth')
plt.ylabel('Number of pigs in population')
plt.show()