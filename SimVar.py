import DepVar
# This file is for variables to do with how the simulation will run

# Length of time for the simulation runs for in days
SimRunTime = 208

# How often there is an insemination event
InseminationFrequencyEB = 35
InseminationFrequencyHW = 14
InseminationFrequencySB = 35

# How often to sell pigs, and how many to sell - format: [days between selling, number to sell]
SellingPolicy = [14, 2000]

# How many days from start of simulation until selling begins
DaysUntilBeginSelling = 180

# Choose model:
# 0 - Logistic
# 1 - Gompertz
# 2 - Linear
Model = 0

# Choose growth rate:
# growth_rate_logistic_model_1
# growth_rate_logistic_model_2
# growth_rate_gompertz_model_1
# growth_rate_gompertz_model_2
# growth_rate_linear_model
GrowthRate = DepVar.growth_rate_logistic_model_2
