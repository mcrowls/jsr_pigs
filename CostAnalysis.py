"""
Plots reduction from max value for pig against fat depth for different pigs, shows previous selling data on top
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns; sns.set_theme()


def pig_value(pigBackFatPenalty, pigWeight):
    return (150+pigBackFatPenalty)*pigWeight

# import real data to plot also
reader = np.loadtxt(open("weight_data.csv", "rb"), delimiter=",", skiprows=1)
real_average_weights = reader[:, -3]
real_average_weights = [i*0.754 for i in real_average_weights]
real_p2_backfat_depth = reader[:, -1]

# import BestSimulationLogistic1 weights to plot as well
reader2 = pd.read_csv("SoldPigsDF_best_logistic_policy_[65, 16714].csv", delimiter=",")
sim_average_weights = reader2["weight"]
sim_average_weights = [i*0.754 for i in sim_average_weights]
sim_p2_backfat_depth = reader2["backFat"]
print("sim_average_weights: {}".format(len(sim_average_weights)))
print("sim_p2_backfat_depth: {}".format(sim_p2_backfat_depth))

for i in range(0, len(sim_p2_backfat_depth)):
    if sim_p2_backfat_depth[i] < 10:
        sim_p2_backfat_depth[i] = 0
    elif 10 <= sim_p2_backfat_depth[i] < 12:
        sim_p2_backfat_depth[i] = 1
    elif 12 <= sim_p2_backfat_depth[i] < 14:
        sim_p2_backfat_depth[i] = 2
    elif 14 <= sim_p2_backfat_depth[i] < 16:
        sim_p2_backfat_depth[i] = 3
    elif 16 <= sim_p2_backfat_depth[i]:
        sim_p2_backfat_depth[i] = 4

for i in range(0, len(real_p2_backfat_depth)):
    if real_p2_backfat_depth[i] < 10:
        real_p2_backfat_depth[i] = 0
    elif 10 <= real_p2_backfat_depth[i] < 12:
        real_p2_backfat_depth[i] = 1
    elif 12 <= real_p2_backfat_depth[i] < 14:
        real_p2_backfat_depth[i] = 2
    elif 14 <= real_p2_backfat_depth[i] < 16:
        real_p2_backfat_depth[i] = 3
    elif 16 <= real_p2_backfat_depth[i]:
        real_p2_backfat_depth[i] = 4

fatDepths = ["<10", "10-12", "13-14", "15-16", "17-18", ">19"]

underFiftyKGs = [-25, -25, -25, -35, -45, -50]
fiftyToSixtyFiveKGs = [-10, -10, -10, -20, -30, -35]
sixtyFiveToHundredFiveKGs = [0, 0, 0, -10, -20, -25]
aboveHundredFiveKGs = [0, 0, 0, 0, 0, 0]
plots = [underFiftyKGs, fiftyToSixtyFiveKGs, sixtyFiveToHundredFiveKGs, aboveHundredFiveKGs]
legendLabels = ["Under 50KGs", "50-65KGs", "65-105KGs", "Above 105KGs"]

fig, ax = plt.subplots()
ax.plot(fatDepths, plots[0])
ax.plot(fatDepths, plots[1])
ax.plot(fatDepths, plots[2])
ax.plot(fatDepths, plots[3])
ax.legend(legendLabels)

ax.set(xlabel='fat depth (mm)', ylabel='penalty',
       title='Penalty against fat depth')
ax.grid()

plt.show()

# now will plot the pig backfat depth against the pig weight

idealWeights = [50, 65, 105]
middleWeights = [45, 57.5, 85, 115] # takes mid values or +-10 if an edge case
costs = [None] * 4

# reassign the arrays to the value of the pig
count = 0
for weight in plots:
    if weight[5] == 0:
        for i in range(0, len(weight)):
            weight[i] = 110     # fixed evaulation for pigs over 105kgs
    else:
        for i in range(0, len(weight)):
            weight[i] = pig_value(weight[i], idealWeights[count])/100
    count += 1
print(plots)

fig, ax = plt.subplots()
ax.plot(fatDepths, plots[0])
ax.fill_between(fatDepths, plots[0])
ax.plot(fatDepths, plots[1])
ax.fill_between(fatDepths, plots[0], plots[1])
ax.plot(fatDepths, plots[2])
ax.fill_between(fatDepths, plots[1], plots[2])
ax.plot(fatDepths, plots[3])
ax.legend(legendLabels)

ax.set(xlabel='fat depth (mm)', ylabel='Price for pig (based on current rates)',
       title='Value of pig against fat depth penalty\n'
             'at ideal weight value is max (top) of each region')
ax.grid()

plt.show()

# now we'll plot a heatmap of pig weight against fat depth
underFiftyKGs = [-25, -25, -25, -35, -45, -50]
fiftyToSixtyFiveKGs = [-10, -10, -10, -20, -30, -35]
sixtyFiveToHundredFiveKGs = [0, 0, 0, -10, -20, -25]
aboveHundredFiveKGs = [0, 0, 0, 0, 0, 0]

allWeights = range(0, 140)
allValues = np.ndarray(shape=[140, 6])

for i in range(0, len(allWeights)):
    if 50 > allWeights[i]:
        for j in range(0, len(underFiftyKGs)):
            allValues[i][j] = pig_value(underFiftyKGs[j], allWeights[i])
    elif 65 > allWeights[i] >= 50:
        for j in range(0, len(fiftyToSixtyFiveKGs)):
            allValues[i][j] = pig_value(fiftyToSixtyFiveKGs[j], allWeights[i])
    elif 105 > allWeights[i] >= 65:
        for j in range(0, len(sixtyFiveToHundredFiveKGs)):
            allValues[i][j] = pig_value(sixtyFiveToHundredFiveKGs[j], allWeights[i])
            print(allValues[i][j])
    elif allWeights[i] >= 105:
        for j in range(0, len(sixtyFiveToHundredFiveKGs)):
            allValues[i][j] = 11000

print(allValues)
print(allValues.shape)

fig, ax = plt.subplots()
ax.imshow(allValues, cmap='hot', interpolation='nearest', aspect='auto')
# ax = sns.heatmap(allValues, xticklabels=6, yticklabels=False)
ax.set(xlabel='Fat depth (mm)', ylabel='Weight of the pig (kg)', title='back fat depth against weight\n'
                                                                    'values on grid are values for pig')
ax.scatter(real_p2_backfat_depth, real_average_weights)
ax.scatter(sim_p2_backfat_depth, sim_average_weights)
ax.legend(["Real sold weights"])

plt.show()