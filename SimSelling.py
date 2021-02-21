# optimal conditions. A little changeable, to account for lots of pigs being near this weight at the same time, we'll
# take a little less than the ideal weight of 105kgs
sellable_weight = 95
sellable_backfat = 10

# from numpy import genfromtxt
# Piglet = genfromtxt('PigletDF.csv', delimiter=',')
# columnLabels = ['pigID', 'weight', 'backFat', 'farm', 'dayInseminated', 'birthingDate',
#                                              'aliveBooelan', 'sowNumber', 'sowParity', 'initialAge']
# PigletDF = pd.DataFrame({'pigID':Piglet[:, 0],'weight':Piglet[:, 1], 'backFat':Piglet[:, 2],'farm':Piglet[:, 3],
#                          'dayInseminated':Piglet[:, 4], 'birthingDate':Piglet[:, 5], 'aliveBooelan':Piglet[:, 6],
#                          'sowNumber':Piglet[:, 7], 'sowParity':Piglet[:, 8],'initialAge':Piglet[:, 9]})

# returns the value made on each pig as a dataframe, plus the total profit.
def return_pig_value(day, df_as_numpy, numSold):
    import pandas as pd
    import numpy as np
    # convert numpy array to pandas dataframe:
    columnLabels = ['pigID', 'weight', 'backFat', 'farm', 'dayInseminated', 'birthingDate',
                    'aliveBooelan', 'sowNumber', 'sowParity', 'initialAge', 'growth_constant', 'earning']
    source_df = pd.DataFrame(
        {'pigID': df_as_numpy[:, 0], 'weight': df_as_numpy[:, 1], 'backFat': df_as_numpy[:, 2], 'farm': df_as_numpy[:, 3],
         'dayInseminated': df_as_numpy[:, 4], 'birthingDate': df_as_numpy[:, 5], 'aliveBooelan': df_as_numpy[:, 6],
         'sowNumber': df_as_numpy[:, 7], 'sowParity': df_as_numpy[:, 8], 'initialAge': df_as_numpy[:, 9],
         'growth_constant': df_as_numpy[:, 10], 'earning': df_as_numpy[:, 11]})

    # back fat penalty within each pig weight range (above 105 not necessary, no fat depth penalties - returns constant
    underFiftyKGPenalty = [-25, -25, -25, -35, -45, -50]
    fiftyToSixtyFiveKGPenalty = [-10, -10, -10, -20, -30, -35]
    sixtyFiveToHundredFiveKGPenalty = [0, 0, 0, -10, -20, -25]
    backFatPenalties = [underFiftyKGPenalty, fiftyToSixtyFiveKGPenalty, sixtyFiveToHundredFiveKGPenalty]
    weight_brackets = [[0, 50], [50, 65], [65, 105]]

    # take heaviest pigs exclusively to sell
    # pigs being sold are set to df (in pd.DataFrame form). All not being sold are set to df_as_numpy, (in numpy array)
    source_df = source_df.sort_values(by=['weight'], ascending=False)
    print("length of source_df: {}".format(len(source_df)))
    df = source_df.iloc[0:numSold]
    df_as_numpy = source_df.iloc[numSold:]
    df_as_numpy = df_as_numpy.to_numpy()

    print("length of df: {}".format(len(df)))
    print("length of df_as_numpy: {}".format(len(df_as_numpy)))

    # all cases for weights beneath 105kgs
    for i in range(0, len(weight_brackets)):
        # print("bracket: {} & {}".format(weight_brackets[i][0], weight_brackets[i][1]))
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] < 10), "earning"] = (150+backFatPenalties[0][0])*df["weight"]
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] > 10) & (df["backFat"] <= 12), "earning"] = (150 + backFatPenalties[i][1])*df["weight"]
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] > 12) & (df["backFat"] <= 14), "earning"] = (150 + backFatPenalties[i][1])*df["weight"]
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] > 14) & (df["backFat"] <= 16), "earning"] = (150 + backFatPenalties[i][1])*df["weight"]
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] > 16) & (df["backFat"] <= 18), "earning"] = (150 + backFatPenalties[i][1])*df["weight"]
        df.loc[(df["weight"] > weight_brackets[i][0]) & (df["weight"] <= weight_brackets[i][1]) & (df["backFat"] > 18), "earning"] = (150 + backFatPenalties[i][1])*df["weight"]

    # all cases for weight above 105kgs
    df.loc[(df["weight"] > 105), "earning"] = 11000

    # calculate max profit
    earnings = sum(df["earning"])

    return df_as_numpy, df, earnings


# set frequency of sales (every 7 days, 2000 pigs  or  every 14 days 5000 pigs)

# calculate profit across each farms sales and loss (on pigs left to grow out of optimal range or too early before
# optimal range). Choose policies on judgement if you cannot formulate it as a optimisation problem
