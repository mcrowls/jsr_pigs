# This file is for variables to do with how the simulation will run

# How many days from start of simulation until selling begins
"""Grant states:

An animal served today (25/2/2021) would typically give birth (20/6/2021) so a gestation of 115 days.

Those animals would be weaned after ~30 days
They’d be in the nursery accommodation for ~40 days
The fastest growers would come out of the finishing accommodation approximately 80 days later (150 days old)
The slowest growers would come out of the finishing accommodation approximately 110 days later (180 days old).

So your 160-190 sounds about right to me.

Add on the gestation and I’d expect animals served today to be selling the resultant progeny between 17th November
 and 17th December."""
# value's taken from the inverse function of the growth rate are listed below. They're not perfect, but match our models
# well and lie close or inside to the range given by Grant above
gompertz1 = 128
gompertz2 = 178
logistic1 = 108
logistic2 = 142
listOfBeginSellingDates = [gompertz1, gompertz2, logistic1, logistic2]
NormalDaysUntilBeginSelling = 175

"""
The selling window for each selling policy will be 10 weeks. This will give both Haywood's 2 week BMS (Batch Management
Production) and Southburn and Eastburn's 5 week BMS an equal amount of time to birth even pigs no matter when the pig
births are (relative to the first pig insemination date). Scaled up to a year this will take 360 weeks of selling (so
36 repeats of the sale pattern).
"""
# Length of time for the simulation runs for in days
SimRunTime = gompertz1 + 70 # DaysUntilBeginSelling + 360 -----535

# How often there is an insemination event (2 weeks and 5 weeks)
InseminationFrequencyEB = 35
InseminationFrequencyHW = 14
InseminationFrequencySB = 35

# How often to sell pigs, and how many to sell - format: [days between selling, number to sell]
"""
With 10 weeks to play with we can try lots of different arrangements for fixed selling strategies. As 2000 pigs are inseminated each 
"""
SellingPolicies = [14, 3600], [7, 1800], [10, 2570], [35, 9000]

# find selling policies that will sell 18k pigs in 10 weeks
import numpy as np
import math

m = 18000/70
x = np.linspace(1, 70, 70)

y = m*x
for i in range(0, len(y)):
    y[i] = math.floor(y[i])

sellingPoliciesLong = [[int(i), int(j)] for i, j in zip(x, y)]
