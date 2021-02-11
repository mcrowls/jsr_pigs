import numpy as np
import pandas as pd


def Int_Distribution(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    Value = int(round(Value))
    return Value


def CalculateWeight(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    return Value


def CalculateBackFat(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    return Value


def PregnancyPeriod(Sigma, Mu):
    Value = np.random.normal(Sigma, Mu)
    Value = int(round(Value))
    return Value


def GenPigletData(D, SN, SP, F, SP_Mean, SP_SD, WeightMean, WeightSD, BF_Mean, BF_SD, PregMean, PregSD, DF, DF_Set):
    BA = Int_Distribution(SP_Mean[SP], SP_SD[SP])
    DS = np.zeros((BA, 10))
    if not DF_Set:
        DS[:, 0] = np.linspace(1, BA, BA)
    else:
        DS[:, 0] = np.linspace(1 + len(DF), len(DF) + BA, BA)
    for i in range(0, BA):
        DS[i, 1] = CalculateWeight(WeightMean, WeightSD)
        DS[i, 2] = CalculateBackFat(BF_Mean, BF_SD)
        DS[i, 5] = PregnancyPeriod(PregMean, PregSD) + D
    DS[:, 3] = F
    DS[:, 4] = D
    DS[:, 6] = 1
    DS[:, 7] = SN
    DS[:, 8] = SP
    DS[:, 9] = 0
    return DS


def Insemination(D, SP_Mean, SP_SD, WeightMean, WeightSD, BF_Mean, BF_SD, PregMean, PregSD, SowDS, SetDS,
                 DS):
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


'''
pd.set_option("display.max_rows", None, "display.max_columns", None)

SowDataset = np.zeros((10, 1))

FakeInitialSet = np.zeros((1, 1))

SetDataSet = False

Day = 1

SowNumber = 1
SowParity = 4
Farm = 1
Alive = 1
TotalPiglets = 23

SowParityMean = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
SowParitySD = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

WeightBA_Mean = 10
WeightBA_SD = 1

BackFatBA_Mean = 2
BackFatBA_SD = 0.2

PregnancyPeriodMean = 80
PregnancyPeriodSD = 5

ds, SetDataSet = Insemination(Day, SowNumber, SowParity, Farm, SowParityMean, SowParitySD, WeightBA_Mean, WeightBA_SD,
                              BackFatBA_Mean, BackFatBA_SD, PregnancyPeriodMean, PregnancyPeriodSD, SowDataset,
                              SetDataSet, FakeInitialSet)

df = pd.DataFrame(ds, columns=['Piglet Number', 'Weight', 'Back Fat', 'Farm', 'Day Inseminated', 'Day Born', 'Alive',
                               'Sow Number', 'Mother Sow Parity', 'Age'])

print(df)
'''
