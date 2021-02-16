"""
Plots reduction from max value for pig against fat depth for different pigs, shows previous selling data on top
"""
from matplotlib import pyplot as plt


def pig_value(pigBackFatPenalty, pigWeight):
    return (150+pigBackFatPenalty)*pigWeight


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

# now will plot pig actual values

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