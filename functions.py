import pandas as pd
import numpy as np
import scipy.stats as sc


'''The code below basically just gets all of the columns in the excel in a workable format. I have edited the excel file
so that all of the entries in which we don't know the farrowing or weaning date yet are no longer in the data set so
this way we can analyse previous data ONLY.'''


'''This function 'getdates()' gets the dates in a form that we can do things with them. So '01-Jan-20 will change to an
 array in the form [1, 1, 20]'''



# How many pigs are in each farm
def get_farm_numbers(data):
    farms = []
    for j in range(np.shape(data)[0]):
        farms.append(data.iloc[j]['Farm'])
    farm_numbers = []
    farm = []
    for i in range(np.size(farms)):
        if i != np.size(farms) - 1 and farms[i+1] == farms[i]:
            farm.append(farms[i])
        elif i == np.size(farms):
            farm.append(farms[i])
        else:
            farm_numbers.append(np.size(farm)+1)
            farm = []
    return farm_numbers



# Probably won't need this function but it just creates 3 separate lists from the initial farms
def separate_farms(data, farm_numbers):
    separated_farms = []
    farm = []
    for i in range(farm_numbers[0]):
        farm.append(data.iloc[i])
    separated_farms.append(farm)
    farm = []
    for i in range(farm_numbers[0]+1, farm_numbers[0] + farm_numbers[1]):
        farm.append(data.iloc[i])
    separated_farms.append(farm)
    farm = []
    for i in range(farm_numbers[0] + farm_numbers[1] + 1, int(np.sum(farm_numbers))):
        farm.append(data.iloc[i])
    separated_farms.append(farm)
    return separated_farms


def get_dates(dates):
    # this array allows us to make put a number to the date ('01-Jan-20' : Jan ---> 1 because it is the index+1 of 'Jan'
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    numbered_dates = []
    for date in dates:
        # Getting the weird entries out the way where the date = 0 or whatever
        if str(date) != 'nan':
            date = str(date)
            date_array = []
            # gets '01-Jan-20' to ['01', 'Jan', '20']
            split_date = date.split('-')
            # We want everything in integer form
            day = int(split_date[0])
            date_array.append(day)
            for i in range(np.size(months)):
                if str(months[i]) == split_date[1]:
                    month = i + 1
                    date_array.append(month)
            year = int(split_date[2])
            date_array.append(year)
            numbered_dates.append(date_array)
    return numbered_dates


'''From an array of the date, this function 'calc_days()' can work out how many days AD this is so we can subtract the days from
eachother to work out how many days it took to wean etc. Bit of a roundabout way but it works...'''

# Used to calculate the days since jesus christ popped it
def calc_days(date_array):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    days += date_array[2]*365
    month = date_array[1]
    month_days = 0
    for j in range(month - 1):
        month_days += days_in_months[j]
    days += month_days
    days += date_array[0]
    return days


def remove_zeros(alive, array):
    data_no = 0
    while data_no < np.size(alive):
        if alive[data_no] == 0:
            alive.remove(alive[data_no])
            array.remove(array[data_no])
        else:
            data_no += 1
    return alive, array


#Silly function
def make_array(data):
    array = []
    for data_no in range(np.size(data)):
        array.append(data[data_no])
    return array


def get_selling_dates(dates):
    # this array allows us to make put a number to the date ('01/Jan/20' : Jan ---> 1 because it is the index+1 of 'Jan'
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    numbered_dates = []
    for date in dates:
        # Getting the weird entries out the way where the date = 0 or whatever
        if str(date) != 'nan':
            date = str(date)
            date_array = []
            # gets '01-Jan-20' to ['01', 'Jan', '20']
            split_date = date.split('/')
            # We want everything in integer form
            day = int(split_date[0])
            date_array.append(day)
            for i in range(np.size(months)):
                if str(months[i]) == split_date[1]:
                    month = i + 1
                    date_array.append(month)
            year = int(split_date[2])
            date_array.append(year)
            numbered_dates.append(date_array)
    return numbered_dates


# Can vary the growth rate but the shift and the max weight are fixed.
def gombertz(x, growth_rate):
    y = 135 * np.exp(-30 * np.exp(-growth_rate * x)) # x in any of these equations will be the time 't'
    return y

# Same as gombertz in terms of initial parameters but this model is actually a better fit for the data
def logistic(x, growth_rate):
    y = 135 / (1 + 30 * np.exp(-growth_rate * x))
    return y

# Calculating the mean square error 
def mean_squared_error_gombertz(x, y, growth_rate):
    error = 0
    for i in range(np.size(x)):
        error += (gombertz(x[i], growth_rate) - y[i])**2
    return error


def mean_squared_error_logistic(x, y, growth_rate):
    error = 0
    for i in range(np.size(x)):
        error += (logistic(x[i], growth_rate) - y[i])**2
    return error

#Picks the growth rate with the lowest error. X and Y in this case will be dates and weights
def minimise_error_gombertz(x, y, growth_rate_array):
    lowest_error = np.inf
    best_growth_rate = 0
    for growth_rate in growth_rate_array:
        mse = mean_squared_error_gombertz(x, y, growth_rate)
        if mse < lowest_error:
            lowest_error = mse
            best_growth_rate = growth_rate
    return lowest_error, best_growth_rate

# does the same thing
def minimise_error_logistic(x, y, growth_rate_array):
    lowest_error = np.inf
    best_growth_rate = 0
    for growth_rate in growth_rate_array:
        mse = mean_squared_error_logistic(x, y, growth_rate)
        if mse < lowest_error:
            lowest_error = mse
            best_growth_rate = growth_rate
    return lowest_error, best_growth_rate

