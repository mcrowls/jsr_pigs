# optimal conditions. A little changeable, to account for lots of pigs being near this weight at the same time, we'll
# take a little less than the ideal weight of 105kgs
sellable_weight = 95
sellable_backfat = 10

import pandas as pd
PigletDF = pd.read_csv("PigletDF.csv")

print(PigletDF)

# check how many pigs in population are sellable
sellable_pig_count = PigletDF[(PigletDF["Weight"] >= sellable_weight) & (PigletDF["BackFat"] >= sellable_backfat)]

print(sellable_pig_count)


# set frequency of sales (every 7 days, 2000 pigs  or  every 14 days 5000 pigs)

# calculate profit across each farms sales and loss (on pigs left to grow out of optimal range or too early before
# optimal range). Choose policies on judgement if you cannot formulate it as a optimisation problem
