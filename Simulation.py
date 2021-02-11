import GenerateSowParityDataset
import Insemination
import DayPassing
import InitVar
import DepVar
import SimVar
import numpy as np


Day = 1
InitiatedPigletDataset = False
PigletDF = np.array([0])


SowDF = GenerateSowParityDataset.GenerateSowParityDataSet(InitVar.GenerateSP_EB, InitVar.GenerateSP_HW,
                                                          InitVar.GenerateSP_SB)

while Day <= SimVar.SimRunTime:
    if InitiatedPigletDataset:
        PigletDF = DayPassing.DayUpdatePiglets(PigletDF, Day)
    if Day % SimVar.InseminationFrequency == 1:
        PigletDF, InitiatedPigletDataset = Insemination.Insemination(Day, DepVar.SowParityMean, DepVar.SowParitySD,
                                                                     DepVar.WeightBA_Mean, DepVar.WeightBA_SD,
                                                                     DepVar.BackFatBA_Mean, DepVar.BackFatBA_SD,
                                                                     DepVar.PregPeriodMean, DepVar.PregPeriodSD,
                                                                     SowDF, InitiatedPigletDataset, PigletDF)
    Day += 1

