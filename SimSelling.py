# returns the value made on each pig as a dataframe, plus the total profit.
def return_pig_value(day, df_as_numpy, numSold):
    import pandas as pd

    # set up pandas dataframe for sold/slaughtered pigs:
    source_df = pd.DataFrame(
        {'pigID': df_as_numpy[:, 0], 'weight': df_as_numpy[:, 1], 'backFat': df_as_numpy[:, 2], 'farm': df_as_numpy[:, 3],
         'dayInseminated': df_as_numpy[:, 4], 'birthingDate': df_as_numpy[:, 5], 'aliveBoolean': df_as_numpy[:, 6],
         'sowNumber': df_as_numpy[:, 7], 'sowParity': df_as_numpy[:, 8], 'initialAge': df_as_numpy[:, 9],
         'growth_constant': df_as_numpy[:, 10], 'earning': df_as_numpy[:, 11]})

    # back fat penalty within each pig weight range (above 105 not necessary, no fat depth penalties - returns constant)
    underFiftyKGPenalty = [-25, -25, -25, -35, -45, -50]
    fiftyToSixtyFiveKGPenalty = [-10, -10, -10, -20, -30, -35]
    sixtyFiveToHundredFiveKGPenalty = [0, 0, 0, -10, -20, -25]
    backFatPenalties = [underFiftyKGPenalty, fiftyToSixtyFiveKGPenalty, sixtyFiveToHundredFiveKGPenalty]
    weight_brackets = [[0, 50], [50, 65], [65, 105]]

    """take heaviest pigs exclusively to sell. For pigs being sold (heaviest alive pigs in source_df) we find the minimum
    weight, to allow us to set alive = 0 all pigs being killed iteration. Allows nparray to store all pigs ever
    (instead of just alive ones)"""
    # pigs being sold are set to df (in pd.DataFrame form). Find min weight from batch being killed
    source_df = source_df.sort_values(by=['weight'], ascending=False)
    df = source_df[source_df["aliveBoolean"] == 1]
    df = df.iloc[0:numSold]
    min_weight_sold = df["weight"].min()

    # set killed activeBoolean = 0 and re-sort by ID so looping updates are done to the correct pigs in the np.array
    source_df.loc[(source_df["aliveBoolean"] == 1) & (source_df["weight"] >= min_weight_sold), "aliveBoolean"] = 0
    source_df = source_df.sort_values(by=['pigID'], ascending=False)
    df_as_numpy = source_df.to_numpy()

    print("\nPoint of sale info:")
    print("length of source_df: {}".format(len(source_df)))
    print("Number of dead pigs in source_df/PigletDF: {}".format(len(source_df[source_df["aliveBoolean"] == 0])))
    print("length of df_as_numpy: {}".format(len(df_as_numpy)))
    print("length of df: {}".format(len(df)))
    print("minimum weight of pigs killed: {}".format(min_weight_sold))

    # convert to deadweights (and save live weight as well)
    df["liveWeight"] = df["weight"]
    df["weight"] = df["weight"] * 0.754

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
    df["deathDate"] = day

    return df_as_numpy, df, earnings
