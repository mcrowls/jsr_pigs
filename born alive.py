import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc


'''The code below basically just gets all of the columns in the excel in a workable format. I have edited the excel file
so that all of the entries in which we don't know the farrowing or weaning date yet are no longer in the data set so
this way we can analyse previous data ONLY.'''


'''This function 'getdates()' gets the dates in a form that we can do things with them. So '01-Jan-20 will change to an
 array in the form [1, 1, 20]'''


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


def make_array(data):
    array = []
    for data_no in range(np.size(data)):
        array.append(data[data_no])
    return array


# Use your file location for this. Keep it in pandas aswell rather than csv its so much easier to work with.
pigs_csv = pd.read_csv('C:/Users/crowl/PycharmProjects/Pigs/Farrowing Data Simple.csv')
# indexing using the column title to access the different columns respectively
sow = pigs_csv['Sow']
date_served = pigs_csv['Date Served']
date_farrowed = pigs_csv['Date Farrowed']
numbers_born_alive = pigs_csv['Numbers Born Alive']
date_weaned = pigs_csv['Weaning Date']
numbers_weaned = pigs_csv['Numbers Weaned']
sow_parity = pigs_csv['Sow Parity']
farm = pigs_csv['Farm']

# getting the dates in array format. See functions above
serving_dates = get_dates(date_served)
farrowing_dates = get_dates(date_farrowed)
weaning_dates = get_dates(date_weaned)

# initialising the arrays to add the values from the below 'for' loop
farrowing_days_array = []
weaning_days_array = []
for i in range(np.shape(farrowing_dates)[0]):
    # See function above
    serving_days = calc_days(serving_dates[i])
    farrowing_days = calc_days(farrowing_dates[i])
    weaning_days = calc_days(weaning_dates[i])
    days_1 = farrowing_days - serving_days
    days_2 = weaning_days - farrowing_days
    farrowing_days_array.append(days_1)
    weaning_days_array.append(days_2)

numbers_born_alive_array = make_array(numbers_born_alive)
numbers_born_alive_array, farrowing_days_array = remove_zeros(numbers_born_alive_array, farrowing_days_array)

avg_numbers_born_alive = np.mean(numbers_born_alive_array)
sd_numbers_born_alive = np.std(numbers_born_alive_array)

scaling_factor = 3.5
x = np.linspace(np.min(numbers_born_alive_array), np.max(numbers_born_alive_array), 10000)
y = sc.norm.pdf(x, avg_numbers_born_alive, sd_numbers_born_alive) * np.size(numbers_born_alive_array) * scaling_factor
plt.plot(x, y, color='coral', label='normal distribution')
plt.hist(numbers_born_alive_array, label='histogram')
plt.xlabel('number born alive')
plt.ylabel('frequency per ' + str(np.size(numbers_born_alive_array)))
plt.legend(loc='best')
plt.show()
