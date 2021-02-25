# This file is for variables to do with how the simulation will run

"""
The selling window for each selling policy will be 10 weeks. This will give both Haywood's 2 week BMS (Batch Management
Production) and Southburn and Eastburn's 5 week BMS an equal amount of time to birth even pigs no matter when the pig
births are (relative to the first pig insemination date)
"""
# Length of time for the simulation runs for in days
SimRunTime = 245

# How often there is an insemination event (2 weeks and 5 weeks)
InseminationFrequencyEB = 35
InseminationFrequencyHW = 14
InseminationFrequencySB = 35

# How often to sell pigs, and how many to sell - format: [days between selling, number to sell]
"""
With 10 weeks to play with we can try lots of different arrangements for fixed selling strategies. As 2000 pigs are inseminated each 
"""
SellingPolicies = [[14, 3600], [7, 1800], [10, 2570], [35, 9000]]

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
# value will be est to 175 days therefore
DaysUntilBeginSelling = 175
