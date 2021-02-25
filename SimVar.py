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

# Different growth rates for each model
growth_rate_logistic_model_1 = [0.018460179351268462, 9.078204438994627e-08]
growth_rate_logistic_model_2 = [0.02387738773877388, 2.910790462317891e-06]
growth_rate_gompertz_model_1 = [0.0209020902090209, 1.1335600340045393e-07]
growth_rate_gompertz_model_2 = [0.026602660266026604, 3.3640061009134556e-06]
growth_rate_linear_model = [0.060555555555, 0.04534777]

# Choose model:
# 0 - Logistic
# 1 - Gompertz
# 2 - Linear
Model = 0
