import GenerateSowParityDataset
import Insemination
import DayPassing
import InitVar
import DepVar
import SimVar
import numpy as np


# Initiate Variables
Day = 1
InitiatedPigletDataset = False
PigletDF = np.array([0])


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
    Day += 1

# extract piglet data for testing and building selling/slaughter policy program
# print(type(PigletDF))
# np.savetxt("PigletDF.csv", PigletDF, delimiter=",")

