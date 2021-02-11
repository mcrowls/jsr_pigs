import pandas as pd
import matplotlib.pyplot as plt


def FarmBornAlive(LowerRange, UpperRange, df, MaxSP):
    NumbersBornAlive = [0] * (MaxSP + 1)
    SowParityCount = [0] * (MaxSP + 1)
    for i in range(LowerRange, UpperRange):
        NumbersBornAlive[df["Sow Parity"][i]] += df["Numbers Born Alive"][i]
        SowParityCount[df["Sow Parity"][i]] += 1
    return NumbersBornAlive, SowParityCount


def Average(MaxSP, NumberBornAlive, SowParityCount):
    AvgNumbersBornAlive = [0] * (MaxSP + 1)
    for i in range(0, MaxSP):
        if SowParityCount[i] != 0:
            AvgNumbersBornAlive[i] = NumberBornAlive[i] / SowParityCount[i]
    return AvgNumbersBornAlive


def SumFarms(EBNumberBA, EBSowPC, HWNumbersBA, HWSowPC, SBNumbersBA, SBSowPC, MaxSP):
    AllFarmsNBA = [0] * (MaxSP + 1)
    AllFarmsSPC = [0] * (MaxSP + 1)
    for i in range(0, MaxSP):
        AllFarmsNBA[i] = EBNumberBA[i] + HWNumbersBA[i] + SBNumbersBA[i]
        AllFarmsSPC[i] = EBSowPC[i] + HWSowPC[i] + SBSowPC[i]
    return AllFarmsNBA, AllFarmsSPC


def RemoveZeros(y):
    x = list(range(0, len(y)))
    for i in range(0, y.count(0)):
        index = y.index(0)
        y.pop(index)
        x.pop(index)
    return x, y


Data = pd.read_csv("Farrowing Data.csv")
Data = Data[["Farm", "Sow Parity", "Numbers Born Alive"]].copy()
Data = Data.dropna()
'''
 with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(Data)
'''
MaxSowParity = max(Data["Sow Parity"])

EBNumbersBornAlive, EBSowParityCount = FarmBornAlive(0, 1736, Data, MaxSowParity)
HWNumbersBornAlive, HWSowParityCount = FarmBornAlive(2526, 6729, Data, MaxSowParity)
SBNumbersBornAlive, SBSowParityCount = FarmBornAlive(9139, 10490, Data, MaxSowParity)
'''
print(EBNumbersBornAlive)
print(EBSowParityCount, '\n')
print(HWNumbersBornAlive)
print(HWSowParityCount, '\n')
print(SBNumbersBornAlive)
print(SBSowParityCount, '\n')
'''
EBAvgNumbersBornAlive = Average(MaxSowParity, EBNumbersBornAlive, EBSowParityCount)
HWAvgNumbersBornAlive = Average(MaxSowParity, HWNumbersBornAlive, HWSowParityCount)
SBAvgNumbersBornAlive = Average(MaxSowParity, SBNumbersBornAlive, SBSowParityCount)
'''
print(EBAvgNumbersBornAlive, '\n')
print(HWAvgNumbersBornAlive, '\n')
print(SBAvgNumbersBornAlive, '\n')
'''
AllNumbersBornAlive, AllSowParityCount = SumFarms(EBNumbersBornAlive, EBSowParityCount, HWNumbersBornAlive,
                                                  HWSowParityCount, SBNumbersBornAlive, SBSowParityCount, MaxSowParity)
'''
print(AllNumbersBornAlive)
print(AllSowParityCount, '\n')
'''
AllAvgNumberBornAlive = Average(MaxSowParity, AllNumbersBornAlive, AllSowParityCount)
'''
print(AllAvgNumberBornAlive, '\n')
'''
x1, y1 = RemoveZeros(AllAvgNumberBornAlive)
x2, y2 = RemoveZeros(EBAvgNumbersBornAlive)
x3, y3 = RemoveZeros(HWAvgNumbersBornAlive)
x4, y4 = RemoveZeros(SBAvgNumbersBornAlive)

plt.figure(1)
plt.rc('axes', labelsize=12)
plt.plot(x1, y1, 'rx', x1, y1, 'r')
plt.ylabel('Number born alive')
plt.xlabel('Sow parity')
plt.xlim(0, MaxSowParity + 1)
plt.ylim(10, 18)
plt.title('Line graph to show how sow parity affects the live litter size')

plt.figure(2)
plt.plot(x2, y2, 'bx')
plt.plot(x2, y2, 'b', label='EB farm')
plt.plot(x3, y3, 'gx')
plt.plot(x3, y3, 'g', label='HW farm')
plt.plot(x4, y4, 'mx')
plt.plot(x4, y4, 'm', label='SB farm')
plt.ylabel('Number born alive')
plt.xlabel('Sow parity')
plt.xlim(0, MaxSowParity + 1)
plt.ylim(10, 18)
plt.legend()
plt.title('Line graph to show how sow parity affects the live \n litter size across various farms')

plt.show()
