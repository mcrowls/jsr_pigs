# This file is for variables to do with how the simulation will run

# Length of time for the simulation runs for in days
SimRunTime = 200

# How often there is an insemination event
InseminationFrequency = 1

# How often to sell pigs, and how many to sell - format: [days after birth, number to sell]. list of dates and sales
# from pigs weaned on certain day. Final sell date of 500 days beyond birth with 0 sold to avoid indexing errors
elevethMarchWeaning = [[157, 60], [167, 210], [170, 209], [173, 210], [180, 105], [181, 360], [184, 190], [187, 574], [500, 0]]
firstJanWeaning = [[155, 47], [164, 64], [170, 180], [174, 220], [178, 220], [180, 220], [183, 221], [184, 509], [500, 0]]
SellingPolicy = firstJanWeaning

# How many days from start of simulation until selling begins
DaysUntilBeginSelling = 150