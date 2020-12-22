import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

# This shows absolutely fuck all lol
plt.scatter(numbers_born_alive, numbers_weaned)
plt.xlabel('numbers born alive')
plt.ylabel('numbers weaned')
plt.show()
