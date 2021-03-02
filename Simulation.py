import GenerateSowParityDataset
import Insemination
import DayPassing
import InitVar
import DepVar
import SimVar
from SimSelling import return_pig_value
import numpy as np
import pandas as pd

# set up growth rate model and mean/var
model = Insemination.CalculateWeightLogistic
meanVar = Insemination.growth_rate_logistic_model_1
totalEarningsList = []
SoldPigsList = []
overweightPigsList = []
sellingPoliciesList = []
growthCurveList = []


# for i in range(0, len(SimVar.sellingPoliciesLong)):


# Initiate Variables
Day = 1
BeginSellingDate = SimVar.listOfBeginSellingDates[2]
InitiatedPigletDataset = False
totalEarnings = 0
PigletDF = np.array([0])
SoldPigsDF = pd.DataFrame(columns=['pigID', 'weight', 'backFat', 'farm', 'dayInseminated', 'birthingDate',
                                   'aliveBooelan', 'sowNumber', 'sowParity', 'initialAge', 'growth_constant',
                                   'earning'])

# Generate sow dataset
SowDF = GenerateSowParityDataset.GenerateSowParityDataSet(InitVar.GenerateSP_EB, InitVar.GenerateSP_HW,
                                                          InitVar.GenerateSP_SB)

# Runs for length of the simulation
while Day <= SimVar.SimRunTime:
    # print("Day: {}".format(Day))
    # Updates piglet dataset from the second day onwards
    if InitiatedPigletDataset:
        PigletDF = DayPassing.DayUpdatePiglets(PigletDF, Day, model)
    # Performs an insemination event every certain amount of days for each farm
    if Day % SimVar.InseminationFrequencyEB == 1:
        PigletDF, InitiatedPigletDataset = Insemination.Insemination(Day, DepVar.PregPeriodMean, DepVar.PregPeriodSD,
                                                                     SowDF[np.where(SowDF[:, 3] == 1)],
                                                                     InitiatedPigletDataset, PigletDF, model, meanVar)
        # print("Insemination at Eastburn, new pig population total: {}".format(len(PigletDF)))
    if (Day + 1) % SimVar.InseminationFrequencyHW == 1: # Day+1 as pigs are never inseminated on the same week
        PigletDF, InitiatedPigletDataset = Insemination.Insemination(Day, DepVar.PregPeriodMean, DepVar.PregPeriodSD,
                                                                     SowDF[np.where(SowDF[:, 3] == 2)],
                                                                     InitiatedPigletDataset, PigletDF, model, meanVar)
        # print("Insemination at Haywold, new pig population total: {}".format(len(PigletDF)))
    if (Day + 2) % SimVar.InseminationFrequencySB == 1: # Day+2 as pigs are never inseminated on the same week
        PigletDF, InitiatedPigletDataset = Insemination.Insemination(Day, DepVar.PregPeriodMean, DepVar.PregPeriodSD,
                                                                     SowDF[np.where(SowDF[:, 3] == 3)],
                                                                     InitiatedPigletDataset, PigletDF, model, meanVar)
        # print("Insemination at Southburn, new pig population total: {}".format(len(PigletDF)))

    # Adds slaughter data to SoldPigsDF (pd.DataFrame form) if the day is a day to sell in the selling policy
    if (Day % SimVar.bestSellingPolicy[0] == 1) and Day >= BeginSellingDate:
        PigletDF, PigletPandasDF, new_earnings = return_pig_value(Day, PigletDF, SimVar.bestSellingPolicy[1])
        totalEarnings += new_earnings
        SoldPigsDF = pd.concat([SoldPigsDF, PigletPandasDF])
    Day += 1

# extract piglet and slaughter data
SoldPigsDF.to_csv("SoldPigsDF_best_logistic_policy_" + str(SimVar.bestSellingPolicy) + ".csv")
print("Total earnings: {}".format([str(SimVar.bestSellingPolicy), totalEarnings]))
totalEarningsList.append(totalEarnings)
SoldPigsList.append(len(SoldPigsDF))
sellingPoliciesList.append(str(SimVar.bestSellingPolicy))
growthCurveList.append(str(model))
overweightPigsList.append(len(SoldPigsDF[SoldPigsDF["earning"] == 11000]))


print("totalEarningsList: {}".format(totalEarningsList))
print("SoldPigsList: {}".format(SoldPigsList))
print("sellingPoliciesList: {}".format(sellingPoliciesList))
print("growthCurveList: {}".format(growthCurveList))
print("overweightPigsList: {}".format(overweightPigsList))
export_df = pd.DataFrame([sellingPoliciesList, growthCurveList, totalEarningsList, SoldPigsList, overweightPigsList])
export_df.to_csv("totalEarningsDataBestLogistic.csv")
