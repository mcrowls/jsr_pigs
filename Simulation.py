import GenerateSowParityDataset
import Insemination
import DayPassing
import InitVar
import DepVar
import SimVar
from SimSelling import return_pig_value
import numpy as np
import pandas as pd


# Initiate Variables
Day = 1
InitiatedPigletDataset = False
totalEarnings = 0
PigletDF = np.array([0])
SoldPigsDF = pd.DataFrame(columns=['pigID', 'weight', 'backFat', 'farm', 'dayInseminated', 'birthingDate',
                    'aliveBooelan', 'sowNumber', 'sowParity', 'initialAge', 'growth_constant', 'earning'])


# Generate sow dataset
SowDF = GenerateSowParityDataset.GenerateSowParityDataSet(InitVar.GenerateSP_EB, InitVar.GenerateSP_HW,
                                                          InitVar.GenerateSP_SB)

# Runs for length of the simulation
while Day <= SimVar.SimRunTime:
    # Updates piglet dataset from the second day onwards
    if InitiatedPigletDataset:
        PigletDF = DayPassing.DayUpdatePiglets(PigletDF, Day)
    # Performs an insemination event every certain amount of days
    if Day % SimVar.InseminationFrequency == 1:
        PigletDF, InitiatedPigletDataset = Insemination.Insemination(Day, DepVar.SowParityMean, DepVar.SowParitySD,
                                                                     DepVar.PregPeriodMean, DepVar.PregPeriodSD,
                                                                     SowDF, InitiatedPigletDataset, PigletDF)
    # removes pigs from PigletDF, slaughtering and selling them. Adds slaughter data to SoldPigsDF (pd.DataFrame form)
    if (Day % SimVar.SellingPolicy[0] == 1) and Day >= SimVar.DaysUntilBeginSelling:
        PigletDF, PigletPandasDF, new_earnings = return_pig_value(Day, PigletDF, SimVar.SellingPolicy[1])
        totalEarnings =+ new_earnings
        SoldPigsDF = pd.concat([SoldPigsDF, PigletPandasDF])
    Day += 1

# # extract piglet data for testing and building selling/slaughter policy program
SoldPigsDF.to_csv("SoldPigsDF.csv")
print("Total earnings: {}".format(totalEarnings))