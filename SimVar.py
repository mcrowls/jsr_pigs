# This file is for variables to do with how the simulation will run

# Length of time for the simulation runs for in days
SimRunTime = 200

# How often there is an insemination event
InseminationFrequency = 1

# How often to sell pigs, and how many to sell - format: [days between selling, number to sell]. list of dates and sales
# from pigs weaned on the 11th of march:
SellingPolicy = [[157, 60], [167, 210], [170, 209], [173, 210], [180, 105], [181, 360], [184, 190], [187, 574], [500, 0]]

# How many days from start of simulation until selling begins
DaysUntilBeginSelling = 150