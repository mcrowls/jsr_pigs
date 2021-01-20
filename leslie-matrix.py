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

# data used taken from excel manually,
# assessing jan_1st farrowing data only
with open('data\jan_1_sale_death_dates.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    death_rate = [row for row in reader]
    #print(death_rate)

with open('data\jan_1_sale_birth_date.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    birth_rate = [row for row in reader]
    #print(birth_rate)
'''
CALCULATE FECUNDITRY RATE for WEANING ON 1st JAN
Calculates the probability of 
'''

# make list of total number of days from first birth to last death
base = datetime.date(2019, 12, 2)
days_in_model = [base + datetime.timedelta(days=x) for x in range(189)]
#print(days_in_model)

# covert dates to datetime values
for row in birth_rate[1:]:
    row[0] = datetime.datetime.strptime(row[0], "%d/%m/%Y").date()

for row in death_rate[1:]:
    row[0] = datetime.datetime.strptime(row[0], "%d/%m/%Y").date()

# make dictionary of births per day
fecunditry_dict = dict()
for date in days_in_model:
    fecunditry_dict[str(date)] = 0

#make fecunditry dictionary - for each date we have  (the number that were born)/(the total population)
for row1 in days_in_model:
    for row2 in birth_rate[1:]:
        if row1 == row2[0]:
            fecunditry_dict[str(row1)] += int(row2[1])


#Experimentingggg===================
# take ones born on first day, gives fecunditry rate for these pigs born on this day
for row1 in days_in_model[1:]:
    fecunditry_dict[str(row1)] = 0

#give 100% chance to birth on day 1
day_1 = '2019-12-02'
fecunditry_dict[day_1] = 1
# print(fecunditry_dict)

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
# print(total_deaths)

# create survival rate
for key in survival_dict:
    if key in deaths_per_day_dict:
        survival_probability = int(deaths_per_day_dict[key]) / total_deaths
        # print(survival_probability)
        survival_dict[key] = survival_probability

# print(survival_dict)
# print(fecunditry_dict)

survival_list = list(survival_dict.values())
fecunditry_list = list(fecunditry_dict.values())

# print(survival_list)
# print(fecunditry_list)

# make diagonal matrix with survival rate as diagonal
leslie_matrix = np.eye(len(survival_list))
diagonal = np.diag_indices_from(leslie_matrix)
leslie_matrix[diagonal] = survival_list

# make first row fecunditry rate
np.concatenate(([fecunditry_list, leslie_matrix]))
print(leslie_matrix)
print(len(leslie_matrix[:,0]))