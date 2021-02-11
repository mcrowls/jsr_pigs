import pandas as pd
import matplotlib.pyplot as plt


# Function to find the total number born alive and the total number of births at each sow parity
# Takes:
#   LowerRange - The lower index for the dataset to start iterating through from
#   UpperRange - The higher index for the dataset to stop iterating through when it reaches it
#   df - The dataframe of Farrowing Data
#   MaxSP - The maximum sow parity in the dataframe
# Returns:
#   NumberBornAlive - A list of total number born alive for each sow parity where index corresponds to sow parity
#   SowParityCount - A list of the number of births at each sow parity where index corresponds to sow parity
def FarmBornAlive(LowerRange, UpperRange, df, MaxSP):
    NumbersBornAlive = [0] * (MaxSP + 1)
    SowParityCount = [0] * (MaxSP + 1)
    for i in range(LowerRange, UpperRange):
        NumbersBornAlive[df["Sow Parity"][i]] += df["Numbers Born Alive"][i]
        SowParityCount[df["Sow Parity"][i]] += 1
    return NumbersBornAlive, SowParityCount


# Function to find the average number born alive at each sow parity
# Takes:
#   MaxSP - The maximum sow parity in the dataframe
#   NumberBornAlive - A list of total number born alive for each sow parity where index corresponds to sow parity
#   SowParityCount - A list of the number of births at each sow parity where index corresponds to sow parity
# Returns:
#   AvgNumbersBornAlive - The average number born alive at each sow parity as a list where the index corresponds to
# the sow parity
def Average(MaxSP, NumberBornAlive, SowParityCount):
    AvgNumbersBornAlive = [0] * (MaxSP + 1)
    for i in range(0, MaxSP):
        if SowParityCount[i] != 0:
            AvgNumbersBornAlive[i] = NumberBornAlive[i] / SowParityCount[i]
    return AvgNumbersBornAlive


# Function to find the total number born alive and the total number of births at each sow parity across all farms
# Takes:
#   EBNumberBA - A list of total number born alive for each sow parity for farm EB where index corresponds to sow
# parity
#   EBSowPC - A list of the number of births at each sow parity for farm EB where index corresponds to sow parity
#   HWNumberBA - A list of total number born alive for each sow parity for farm HW where index corresponds to sow
# parity
#   HWSowPC - A list of the number of births at each sow parity for farm HW where index corresponds to sow parity
#   SBNumberBA - A list of total number born alive for each sow parity for farm SB where index corresponds to sow
# parity
#   SBSowPC - A list of the number of births at each sow parity for farm SB where index corresponds to sow parity
#   MaxSP - The maximum sow parity in the dataframe
def SumFarms(EBNumberBA, EBSowPC, HWNumbersBA, HWSowPC, SBNumbersBA, SBSowPC, MaxSP):
    AllFarmsNBA = [0] * (MaxSP + 1)
    AllFarmsSPC = [0] * (MaxSP + 1)
    for i in range(0, MaxSP):
        AllFarmsNBA[i] = EBNumberBA[i] + HWNumbersBA[i] + SBNumbersBA[i]
        AllFarmsSPC[i] = EBSowPC[i] + HWSowPC[i] + SBSowPC[i]
    return AllFarmsNBA, AllFarmsSPC


# Function to remove instances where there are no cases of birth of a pig at a certain sow parity
# Takes:
#   y - A list of the average number born alive where the index corresponds to sow parity
# Returns:
#   x - A list of sow parities without zero values for average number born alive
#   y - A list of average number born alive without zero values as corresponding sow parities with the same index in x
def RemoveZeros(y):
    x = list(range(0, len(y)))
    for i in range(0, y.count(0)):
        index = y.index(0)
        y.pop(index)
        x.pop(index)
    return x, y


# Reads data from csv into pandas and selects useful columns: Farm, Sow Parity, Numbers Born Alive
Data = pd.read_csv("Farrowing Data.csv")
Data = Data[["Farm", "Sow Parity", "Numbers Born Alive"]].copy()
Data = Data.dropna()

# Uncomment to set option to print the full pandas dataframe
'''
 with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(Data)
'''

# Finds the Max Sow Parity in the Dataset
MaxSowParity = max(Data["Sow Parity"])

# Runs function to find:
# The total number of pigs born from each sow parity returned as a list where the index corresponds to the sow parity
# The total number of times a sow of a each sow parity gave birth returned as a list where the index corresponds to
# the sow parity
EBNumbersBornAlive, EBSowParityCount = FarmBornAlive(0, 1736, Data, MaxSowParity)
HWNumbersBornAlive, HWSowParityCount = FarmBornAlive(2526, 6729, Data, MaxSowParity)
SBNumbersBornAlive, SBSowParityCount = FarmBornAlive(9139, 10490, Data, MaxSowParity)

# Uncomment to print the lists returned for each farm
'''
print(EBNumbersBornAlive)
print(EBSowParityCount, '\n')
print(HWNumbersBornAlive)
print(HWSowParityCount, '\n')
print(SBNumbersBornAlive)
print(SBSowParityCount, '\n')
'''

# Runs function to return the average number of pigs born from one sow of each sow parity as a list where the index
# corresponds to the sow parity
EBAvgNumbersBornAlive = Average(MaxSowParity, EBNumbersBornAlive, EBSowParityCount)
HWAvgNumbersBornAlive = Average(MaxSowParity, HWNumbersBornAlive, HWSowParityCount)
SBAvgNumbersBornAlive = Average(MaxSowParity, SBNumbersBornAlive, SBSowParityCount)

# Uncomment to print the lists returned for each farm
'''
print(EBAvgNumbersBornAlive, '\n')
print(HWAvgNumbersBornAlive, '\n')
print(SBAvgNumbersBornAlive, '\n')
'''

# Runs function to find:
# the total number of pigs born alive across all farms as a list where the index corresponds to the sow parity.
# The total number of times a sow of a each sow parity gave birth across all farms returned as a list where the index
# corresponds to the sow parity
AllNumbersBornAlive, AllSowParityCount = SumFarms(EBNumbersBornAlive, EBSowParityCount, HWNumbersBornAlive,
                                                  HWSowParityCount, SBNumbersBornAlive, SBSowParityCount, MaxSowParity)

# Uncomment to print the lists returned
'''
print(AllNumbersBornAlive)
print(AllSowParityCount, '\n')
'''

# Runs a function to find the avergae number of pigs born alive at each sow parity as a list where the index
# corresponds to the sow parity
AllAvgNumberBornAlive = Average(MaxSowParity, AllNumbersBornAlive, AllSowParityCount)

# Uncomment to print the lists returned
'''
print(AllAvgNumberBornAlive, '\n')
'''

# Runs a function to remove instances where there are no cases of birth of a pig at a certain sow parity returned as
# a list of average number of pigs born alive and corresponding sow parities
x1, y1 = RemoveZeros(AllAvgNumberBornAlive)
x2, y2 = RemoveZeros(EBAvgNumbersBornAlive)
x3, y3 = RemoveZeros(HWAvgNumbersBornAlive)
x4, y4 = RemoveZeros(SBAvgNumbersBornAlive)

# Plots a graph of of average number of piglets born alive against sow parity for all farms
plt.figure(1)
plt.rc('axes', labelsize=12)
plt.plot(x1, y1, 'rx', x1, y1, 'r')
plt.ylabel('Number born alive')
plt.xlabel('Sow parity')
plt.xlim(0, MaxSowParity + 1)
plt.ylim(10, 18)
plt.title('Line graph to show how sow parity affects the live litter size')

# Plots a graph of of average number of piglets born alive against sow parity for all farms and for the 3 individual
# farms
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
