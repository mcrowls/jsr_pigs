import numpy as np
import pandas as pd

# File to update the sow and piglet dataset after an insemination event


# Function to take a random integer number from a normal distribution
# Takes:
#   Sigma - The mean of the normal distribution
#   Mu -  The standard deviation of the normal distribution
# Returns:
#   Value - The randomly chosen integer
def Int_Distribution(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    Value = int(round(Value))
    return Value


# Function to determine the weight of a new born piglet
# Takes:
#   Sigma - The mean of the normal distribution
#   Mu -  The standard deviation of the normal distribution
# Returns:
#   Value - The randomly chosen value
def CalculateWeight(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    return Value


# Function to determine the depth of back fat of a new born piglet
# Takes:
#   Sigma - The mean of the normal distribution
#   Mu -  The standard deviation of the normal distribution
# Returns:
#   Value - The randomly chosen value
def CalculateBackFat(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    return Value


# Function to determine the pregnancy period of a sow in days
# Takes:
#   Sigma - The mean of the normal distribution
#   Mu -  The standard deviation of the normal distribution
# Returns:
#   Value - The randomly chosen integer
def PregnancyPeriod(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    Value = int(round(Value))
    return Value


# Function to generate all the new data for each for each piglet a sow has birthed
# Takes:
#   D - The day the simulation is on
#   SN - The sow number of the sow birthing the piglet
#   SP - The sow parity of the sow birthing the piglet
#   F - The Farm the piglet is birthed onto
#   SP_Mean - The list of mean piglets born alive depending on sow parity
#   SP_SD - The list of standard deviations of piglets born alive depending on sow parity
#   WeightMean - The mean weight of piglets born alive
#   WeightSD - The standard deviation of weights of piglets born alive
#   BF_Mean - The mean depth of back far of piglets born alive
#   BF_SD - The standard deviation of depths of back far of piglets born alive
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   DF - The already existing dataset of piglets (If none a dummy is passed)
#   DF_Set - A True/False variable saying whether there is already a dataset of piglets
# Returns:
#   DS - The dataset of piglets
def GenPigletData(D, SN, SP, F, SP_Mean, SP_SD, WeightMean, WeightSD, BF_Mean, BF_SD, PregMean, PregSD, DF, DF_Set):
    # Calculate the number of piglets the sow has birthed
    BA = Int_Distribution(SP_Mean[SP], SP_SD[SP])
    # Initiate dataset
    DS = np.zeros((BA, 10))
    # Generate piglet number
    if not DF_Set:
        DS[:, 0] = np.linspace(1, BA, BA)
    else:
        DS[:, 0] = np.linspace(1 + len(DF), len(DF) + BA, BA)
    for i in range(0, BA):
        # Generate weight for each piglet
        DS[i, 1] = CalculateWeight(WeightMean, WeightSD)
        # Generate the back fat depth for each piglet
        DS[i, 2] = CalculateBackFat(BF_Mean, BF_SD)
        # Generate the pregnancy period for each piglet
        DS[i, 5] = PregnancyPeriod(PregMean, PregSD) + D
    # Assign farm
    DS[:, 3] = F
    # Assign day inseminated
    DS[:, 4] = D
    # Assign Alive = True
    DS[:, 6] = 1
    # Assign sow number
    DS[:, 7] = SN
    # Assign sow parity
    DS[:, 8] = SP
    # Assign initial age (0 as not born)
    DS[:, 9] = 0
    return DS


# Function to update sow and piglet dataset for all sows in the sow dataset
# Takes:
#   D - The day the simulation is on
#   SP_Mean - The list of mean piglets born alive depending on sow parity
#   SP_SD - The list of standard deviations of piglets born alive depending on sow parity
#   WeightMean - The mean weight of piglets born alive
#   WeightSD - The standard deviation of weights of piglets born alive
#   BF_Mean - The mean depth of back far of piglets born alive
#   BF_SD - The standard deviation of depths of back far of piglets born alive
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   SowDS - The sow dataset
#   SetDS - A True/False variable saying whether there is already a dataset of piglets
# Returns:
#   DS - The dataset of piglets
#   SetDS - A True/False variable saying whether there is already a dataset of piglets
def Insemination(D, SP_Mean, SP_SD, WeightMean, WeightSD, BF_Mean, BF_SD, PregMean, PregSD, SowDS, SetDS,
                 DS):
    # Iterates through sows adding more piglets to the piglet dataset by either creating a piglet dataset or
    # concatenating them to the end of the existing piglet dataset
    for i in range(0, len(SowDS)):
        if not SetDS:
            DS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), SP_Mean, SP_SD, WeightMean,
                               WeightSD, BF_Mean, BF_SD, PregMean, PregSD, DS, SetDS)
            SetDS = True
        else:
            TempDS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), SP_Mean, SP_SD, WeightMean,
                                   WeightSD, BF_Mean, BF_SD, PregMean, PregSD, DS, SetDS)
            DS = np.concatenate((DS, TempDS))
    return DS, SetDS
