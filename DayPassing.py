import numpy as np

# File that updates all datasets for the passing of one day


# Function to update the weight of a piglet in the piglet dataset
# Takes:
#   Weight - The weight of the piglet
# Returns:
#   Weight - The updated weight of the piglet
def UpdateWeights(Weight):
    Weight = Weight + 5/6
    return Weight


# Function to update the back fat of a piglet in the piglet dataset
# Takes:
#   BF - The depth of back fat of the piglet
# Returns:
#   BF - The updated depth of back fat of the piglet
def UpdateBackFat(BF):
    BF = BF * 1.1
    return BF


# Function to update the piglet dataset for a day passing
# Takes:
#   DS - The dataset of piglets
#   D - The day in the simulation
# Returns:
#   DS - The updated dataset of piglets
def DayUpdatePiglets(DS, D):
    for i in range(0, len(DS)):
        # Update weight
        DS[i, 1] = UpdateWeights(DS[i, 1])
        # Update back fat
        DS[i, 2] = UpdateBackFat(DS[i, 2])
        # Update age if alive and born
        if DS[i, 6] == 1 and DS[i, 5] <= D:
            DS[i, 9] += 1
    return DS
