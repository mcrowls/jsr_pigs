import numpy as np

# File to initiate the sow dataset


# Function to initiate the sow dataset
# Takes:
#   GenSP_EB - The list of numbers of each sow at each sow parity from InitVar for farm EB
#   GenSP_HW - The list of numbers of each sow at each sow parity from InitVar for farm HW
#   GenSP_SB - The list of numbers of each sow at each sow parity from InitVar for farm SB
# Returns:
#   SP - The dataset of sows
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
