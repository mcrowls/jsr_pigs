import numpy as np
import Insemination

# File that updates all datasets for the passing of one day


# Function to update the back fat of a piglet in the piglet dataset
# Takes:
#   BF - The depth of back fat of the piglet
# Returns:
#   BF - The updated depth of back fat of the piglet
def UpdateBackFat(weight):
    BF = 1.0364296522510674 + weight*0.08841889413839167
    return BF


# Function to update the piglet dataset for a day passing
# Takes:
#   DS - The dataset of piglets
#   D - The day in the simulation
# Returns:
#   DS - The updated dataset of piglets
def DayUpdatePiglets(DS, D, growth_curve):
    for i in range(0, len(DS)):
        # Update weight using time (D) and growth rate for pig DS[i, 10]
        if growth_curve == 0:
            DS[i, 1] = Insemination.CalculateWeightLogistic(D, DS[i, 10])
        elif growth_curve == 1:
            DS[i, 1] = Insemination.CalculateWeightGompertz(D, DS[i, 10])
        elif growth_curve == 2:
            DS[i, 1] = Insemination.CalculateWeightLinear(D, DS[i, 10])
        # Update back fat using weight since backfat is assumed to be directly proportional to weight 
        DS[i, 2] = Insemination.CalculateBackFat(DS[i, 1])
        # Update age if alive and born
        if DS[i, 6] == 1 and DS[i, 5] <= D:
            DS[i, 9] += 1
    return DS
