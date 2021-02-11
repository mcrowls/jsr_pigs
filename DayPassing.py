import numpy as np


def UpdateWeights(Weight):
    Weight = Weight * 1.1
    return Weight


def UpdateBackFat(BF):
    BF = BF * 1.1
    return BF


def DayUpdatePiglets(DS, D):
    for i in range(0, len(DS)):
        DS[i, 1] = UpdateWeights(DS[i, 1])
        DS[i, 2] = UpdateBackFat(DS[i, 2])
        if DS[i, 6] == 1 and DS[i, 5] <= D:
            DS[i, 9] += 1
    return DS


'''
Piglets = np.random.randint(100, size=(10, 10))

Day = 1

DayUpdatePiglets(Piglets, Day)
'''
