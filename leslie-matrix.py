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
Fecundity rate per age          chance of parent of piglet giving birth per age  <--- not sure if we can do this or not
Survival rate per age           number of litter weaning per age

'''

import csv
import pandas as pd
import numpy as np
from scipy.linalg import leslie
from born_alive import get_dates

# import simple farrowing data

pigs_df = pd.read_csv("farrowing_data_simple.csv")

with open('unique_sow_id_list.csv', newline='') as f:
    reader = csv.reader(f)
    unique_sow = list(reader)

# unique_sow = pd.read_csv("unique_sow_id_list.csv")


# print(pigs_df[pigs_df["Sow"] == 'KPOF0034'])

'''
CALCULATE FECUNDITRY (here Weaning) RATE
1. Find all infants of all sows and note farrowing date, weaning date
2. Find difference between farrowing date (date of birth) and weaning date (date the pig moved on from mother to solid 
foods)
3. Calculate age of each piglet
4. Count number of piglets at each age (accurate to each day). This is our 
'''
print(unique_sow)
for sow in unique_sow[1:]:
    print(sow)
    sow_info = pigs_df[pigs_df["Sow"] == str(sow)]
    print(sow_info)
    # numberInFarrow = len(pigs_df[pigs_df["Sow"] == sow])
#same_infants = pigs_df["Sow"]
#print(same_infants)

# calculate death rate




# for 27-05-2020
