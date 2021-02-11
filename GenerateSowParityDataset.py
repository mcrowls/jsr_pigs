import numpy as np


def GenerateSowParityDataSet(GenSP_EB, GenSP_HW, GenSP_SB):
    # Find the number of Sows in each farm and total across all farms
    TotalSowsEB = sum(GenSP_EB)
    TotalSowsHW = sum(GenSP_HW)
    TotalSowsSB = sum(GenSP_SB)
    TotalSows = TotalSowsEB + TotalSowsHW + TotalSowsSB

    # Initiate dataset
    SP = np.zeros((TotalSows, 4))

    # Add Sow number in column 0
    SP[:, 0] = np.linspace(1, TotalSows, TotalSows)

    # Add Sow Parity in column 1
    Index = 0
    for i in range(0, len(GenSP_EB)):
        SP[Index: Index + GenSP_EB[i], 1] = i
        Index += GenSP_EB[i]
    for j in range(0, len(GenSP_HW)):
        SP[Index: Index + GenSP_HW[j], 1] = j
        Index += GenSP_HW[j]
    for k in range(0, len(GenSP_SB)):
        SP[Index: Index + GenSP_SB[k], 1] = k
        Index += GenSP_SB[k]

    # Add farm ID: EB=1 HW=2 SB=3 in column 2
    SP[0:TotalSowsEB, 2] = 1
    SP[TotalSowsEB:TotalSowsEB + TotalSowsHW, 2] = 2
    SP[TotalSowsEB + TotalSowsHW:TotalSowsEB + TotalSowsHW + TotalSowsSB, 2] = 3

    # Add Alive column: Alive/True=1 Dead/False=0 in column 3
    SP[:, 3] = 1

    return SP


'''
# Input number of Sows of parity corresponding to index for each farm
GenerateSP_EB = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
GenerateSP_HW = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
GenerateSP_SB = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3)

SP = GenerateSowParityDataSet(GenerateSP_EB, GenerateSP_HW, GenerateSP_SB)
print(SP)
'''