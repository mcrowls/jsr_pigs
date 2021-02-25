import numpy as np
import math

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


# Now two functions separate for gompertz and logistic. Make sure that this
# corresponds to the right mean and variance when you implement
def CalculateWeightLogistic(t, growth_rate):
    y = 240 / (1 + 30 * np.exp(-growth_rate * t))
    return y


def CalculateWeightGompertz(t, growth_rate):
    y = 240 * np.exp(-30*np.exp(-growth_rate*t))
    return y


def CalculateWeightLinear(t, growth_rate):
    y = (growth_rate * t) + 7
    return y


# Function to determine the growth rate of a new born piglet based on a certain mean and variance
# Takes:
# Returns:
#   GrowthRate - The growth rate of the pig
def GenerateGrowthRate(mean_and_variance):
    GrowthRate = np.random.normal(mean_and_variance[0], math.sqrt(mean_and_variance[1]), 1)
    return GrowthRate


# Function to determine the depth of back fat of a new born piglet
# Takes:
#   Weight - The current weight of the pig
# Returns:
#   fat - The updated depth of fat
def CalculateBackFat(weight):
    fat = 1.0364296522510674 + weight*0.08841889413839167
    return fat


# Function to calculate the number of piglets born from a Sow
# Takes:
#   SP - The sow parity of the Sow giving birth
# Returns:
#   Value - The number of piglets born alive
def BornAlive(SP):
    mean = (9.89634522e-03 * (SP ** 3)) - (2.80572294e-01 * (SP ** 2)) + (1.75100075e+00 * SP) + 1.30828185e+01
    SD = 3.6799672876782386
    Value = np.random.normal(mean, SD)
    Value = int(round(Value))
    return Value


# Mean and variance, mean takes position 0 and variance takes 1 in these arrays
growth_rate_logistic_model_1 = [0.018460179351268462, 9.078204438994627e-08]
growth_rate_logistic_model_2 = [0.02387738773877388, 2.910790462317891e-06]
growth_rate_gompertz_model_1 = [0.0209020902090209, 1.1335600340045393e-07]
growth_rate_gompertz_model_2 = [0.026602660266026604, 3.3640061009134556e-06]
growth_rate_linear_model = [0.060555555555, 0.04534777]


# Function to generate all the new data for each for each piglet a sow has birthed
# Takes:
#   D - The day the simulation is on
#   SN - The sow number of the sow birthing the piglet
#   SP - The sow parity of the sow birthing the piglet
#   F - The Farm the piglet is birthed onto
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   DF - The already existing dataset of piglets (If none a dummy is passed)
#   DF_Set - A True/False variable saying whether there is already a dataset of piglets
# Returns:
#   DS - The dataset of piglets
def GenPigletData(D, SN, SP, F, PregMean, PregSD, DF, DF_Set, growth_curve, mean_and_var):
    # Calculate the number of piglets the sow has birthed
    BA = BornAlive(SP)
    # Initiate dataset
    DS = np.zeros((BA, 12))
    # Generate piglet number
    if not DF_Set:
        DS[:, 0] = np.linspace(1, BA, BA)
    else:
        DS[:, 0] = np.linspace(1 + len(DF), len(DF) + BA, BA)
    for i in range(0, BA):
        # Generate the growth rate for each piglet
        DS[i, 10] = GenerateGrowthRate(mean_and_var)
        # Generate weight for each piglet
        DS[i, 1] = growth_curve(D, DS[i, 10])
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
    # Assign earning value
    DS[:, 11] = None
    return DS


# Function to update sow and piglet dataset for all sows in the sow dataset
# Takes:
#   D - The day the simulation is on
#   PregMean - The mean length of pregnancy for sows
#   PregSD - The standard deviation of pregnancy periods
#   SowDS - The sow dataset
#   SetDS - A True/False variable saying whether there is already a dataset of piglets
#   DS - The dataset of piglets
# Returns:
#   DS - The dataset of piglets
#   SetDS - A True/False variable saying whether there is already a dataset of piglets

'''For this new function, you must specify which model you want to use
(CalculateWeightLogisitic()/CalculateWeightGompertz()) and you must also specify
the mean and variance array from one of the 4 above. This way, we can see how this
varies with data generated from both the datasets'''


def Insemination(D, PregMean, PregSD, SowDS, SetDS, DS, model, mean_and_var):
    # Iterates through sows adding more piglets to the piglet dataset by either creating a piglet dataset or
    # concatenating them to the end of the existing piglet dataset
    for i in range(0, len(SowDS)):
        if not SetDS:
            DS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), PregMean,
                               PregSD, DS, SetDS, model, mean_and_var)
            SetDS = True
        else:
            TempDS = GenPigletData(D, int(SowDS[i, 0]), int(SowDS[i, 1]), int(SowDS[i, 2]), PregMean,
                                   PregSD, DS, SetDS, model, mean_and_var)
            DS = np.concatenate((DS, TempDS))
    return DS, SetDS
