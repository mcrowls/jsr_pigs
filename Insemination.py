import numpy as np

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
#   t - Time in days
#   growth_rate - the growth rate of the piglet
# Returns:
#   y - the updated weight of the pig
def CalculateWeight(t, growth_rate):
    y = 240 / (1 + 30 * np.exp(-growth_rate * t))
    return y


# Function to determine the growth rate of a new born piglet
# Takes:
# Returns:
#   GrowthRate - The growth rate of the pig
def GenerateGrowthRate():
    mean = 0.018460179351268462
    var = 9.078204438994627e-08
    GrowthRate = np.random.normal(mean, var, 1)
    return GrowthRate


# Function to determine the depth of back fat of a new born piglet
# Takes:
#   Weight - The current weight of the pig
# Returns:
#   fat - The updated depth of fat
def CalculateBackFat(weight):
    fat = 1.0364296522510674 + weight*0.08841889413839167
    return fat


# Function to generate all the new data for each for each piglet a sow has birthed
# Takes:
#   D - The day the simulation is on
#   SN - The sow number of the sow birthing the piglet
#   SP - The sow parity of the sow birthing the piglet
#   F - The Farm the piglet is birthed onto
#   SP_Mean - The list of mean piglets born alive depending on sow parity
#   SP_SD - The list of standard deviations of piglets born alive depending on sow parity
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   DF - The already existing dataset of piglets (If none a dummy is passed)
#   DF_Set - A True/False variable saying whether there is already a dataset of piglets
# Returns:
#   DS - The dataset of piglets
def GenPigletData(D, SN, SP, F, SP_Mean, SP_SD, PregMean, PregSD, DF, DF_Set):
    # Calculate the number of piglets the sow has birthed
    BA = Int_Distribution(SP_Mean[SP], SP_SD[SP])
    # Initiate dataset
    DS = np.zeros((BA, 11))
    # Generate piglet number
    if not DF_Set:
        DS[:, 0] = np.linspace(1, BA, BA)
    else:
        DS[:, 0] = np.linspace(1 + len(DF), len(DF) + BA, BA)
    for i in range(0, BA):
        # Generate the growth rate for each piglet
        DS[i, 10] = GenerateGrowthRate()
        # Generate weight for each piglet
        DS[i, 1] = CalculateWeight(D, DS[i, 10])
        # Generate the back fat depth for each piglet
        DS[i, 2] = CalculateBackFat(DS[i, 1])
    # Assign farm
    DS[:, 3] = F
    # Assign day inseminated
    DS[:, 4] = D
    # Generate the birthing date for the set of piglets
    DS[:, 5] = Int_Distribution(PregMean, PregSD) + D
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
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   SowDS - The sow dataset
#   SetDS - A True/False variable saying whether there is already a dataset of piglets
# Returns:
#   DS - The dataset of piglets
#   SetDS - A True/False variable saying whether there is already a dataset of piglets
def Insemination(D, SP_Mean, SP_SD, PregMean, PregSD, SowDS, SetDS,
                 DS):
    # Iterates through sows adding more piglets to the piglet dataset by either creating a piglet dataset or
    # concatenating them to the end of the existing piglet dataset
    for i in range(0, len(SowDS)):
        if not SetDS:
            DS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), SP_Mean, SP_SD, PregMean,
                               PregSD, DS, SetDS)
            SetDS = True
        else:
            TempDS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), SP_Mean, SP_SD, PregMean,
                                   PregSD, DS, SetDS)
            DS = np.concatenate((DS, TempDS))
    return DS, SetDS
