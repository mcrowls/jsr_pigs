'''
Exploring leslie matrix application to our data. model's discrete-time, age-structured population growth

Explanation:
2 key factors on population - birth and death rate. Fecundity rate (number of babies per year). Works on comparing
this fecundity rate with the survival rate. Leslie matrix only models female pigs. Leslie matrix;

[   F_1,    F_2,    F_3,    F_4, ...    ]
[   S_1,    0,      0,      0,   ...    ]
[   0,      S_2,    0,      0,   ...    ]
[   0,      0,      S_3,    0,   ...    ]
[   .                       ...         ]
[   .                            ...    ]

With initial population vector (N_1 = number of 1 yr old females)

[   N_1 ]
[   N_2 ]
[   N_3 ]
[   .   ]
[   .   ]
[   .   ]

run the matrix day by day so fecundity rate is the number of piglets born per day. Equivalent terms:

Leslie matrix input:            JSR applicable data:
Fecundity rate per age          first entry will be date of weaning, all others 0
Survival rate per age           1 for all entry bar dates that align with "date sold" in relevant slaughter data

'''

import csv
import datetime
import pandas as pd
import numpy as np
from scipy.linalg import leslie
from born_alive import get_dates
from matplotlib import pyplot as plt

# data used taken from excel manually,
# assessing jan_1st farrowing data only
with open('data\jan_1_sale_death_dates.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    death_rate = [row for row in reader]

with open('data\jan_1_sale_birth_date.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    birth_rate = [row for row in reader]

'''
CALCULATE fecundity RATE for WEANING ON 1st JAN
'''

# make list of total number of days from first birth to last death
base = datetime.date(2019, 12, 2)
days_in_model = [base + datetime.timedelta(days=x) for x in range(189)]

# covert dates to datetime values
for row in birth_rate[1:]:
    row[0] = datetime.datetime.strptime(row[0], "%d/%m/%Y").date()

for row in death_rate[1:]:
    row[0] = datetime.datetime.strptime(row[0], "%d/%m/%Y").date()

# make dictionary of births per day
birth_dict = dict()
for date in days_in_model:
    birth_dict[str(date)] = 0

# make fecundity dictionary - for each date we have (the number that were born)/(the total population)
for row1 in days_in_model:
    for row2 in birth_rate[1:]:
        if row1 == row2[0]:
            birth_dict[str(row1)] += int(row2[1])


# Experimentingggg===================
# take ones born on first day, gives fecundity rate for these pigs born on this day
fecundity_dict = dict(birth_dict)
for row1 in days_in_model[1:]:
    fecundity_dict[str(row1)] = 0

# give 100% chance to birth on day 1
day_1 = '2019-12-02'
fecundity_dict[day_1] = 1
# print(fecundity_dict)

# make survival rate out of probability of death per date for all pigs weaned on 1st jan / total deaths for all pigs
# weaned on 1st jan

# make dict of deaths per day
survival_dict = dict()
for date in days_in_model:
    survival_dict[str(date)] = 1

# make dict of days animals are slaughtered
deaths_per_day_dict = dict()
for day_of_death in death_rate[1:]:
    deaths_per_day_dict[str(day_of_death[0])] = int(day_of_death[1])

total_deaths = sum(deaths_per_day_dict.values())

# create survival rate
for key in survival_dict:
    if key in deaths_per_day_dict:
        survival_probability = int(deaths_per_day_dict[key]) / total_deaths
        # print(survival_probability)
        survival_dict[key] = survival_probability

survival_list = list(survival_dict.values())
survival_list.pop(0)
fecundity_list = list(fecundity_dict.values())

#print(survival_list)
#print(fecundity_list)

leslie_matrix = leslie(fecundity_list, survival_list)
#print(leslie_matrix)

'''
Create P0 - our starting population. Index 0 is all the newborns on that day but has to be = 0; otherwise new babies 
equat to that value would be born each day. Index 1 and so forth is the number that age as time goes on.
As the final birth from the subset of piglets weaned on the 1st jan happened on '2019-12-08', this will be the day
before day 1, to allow day 0 with 0 births
'''

P0 = [0, 72, 161, 193, 464, 421, 398, 69] + [0] * (len(fecundity_list) - 8)


'''
create results array, where each row is a different day in the model. As time goes on, the pigs move down the vector,
corresponding to them getting older. Finally they reach survival rate areas != 0 and reduce in numbers.
'''
results = np.array(([P0]))

P_old = P0

for i in range(200):
    P_new = np.dot(leslie_matrix, P_old)
    results = np.append(results, [P_new], axis=0)

    P_old = P_new

'''
currently displaying total population over time. But we can track age groups separately, for all ages that weaned
on the 1st Jan. Could include more weaning times nearby this figure to get a more accurate prediction of expected
death time

to add date labels (unreadable right now) use

plt.plot(list(fecundity_dict.keys()), total_pop[0:189])

'''
total_pop = []
for row in results:
    total_pop.append(sum(row))

plt.plot(total_pop[0:189])
plt.title('population of pigs that weaned 1st January')
plt.ylabel('total population')
plt.xlabel('days from 2019-12-09')
plt.show()