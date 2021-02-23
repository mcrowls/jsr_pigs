import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

generate_data = False
n_runs = 250 # Number of times to run the simulation
if generate_data:
    # Create lists to eventually add to a pandas dataframe
    run_num = []
    total_sold = []
    over = []
    opt = []
    p10 = []
    p20 = []
    p25 = []
    p30 = []
    p35 = []
    p45 = []
    p50 = []

    # run the simulation n_runs times
    for run in range(1,n_runs+1):
        run_num.append(run)

        # runs the simulation
        os.system('python Simulation.py')

        # reads the data produced in the simulation
        SoldPigsDF = pd.read_csv('SoldPigsDF.csv')
        SoldPigsDF["Price Per KG"] = (SoldPigsDF["earning"] / SoldPigsDF["weight"]).round()

        # Overweight Pigs
        pigs_over = SoldPigsDF.loc[SoldPigsDF['weight'] > 105]

        # Optimal Pigs - those which are sold for 150p/kg
        pigs_opt = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 150) & (SoldPigsDF['weight'] <= 105)]

        # Penalties, given by number at end
        pigs_10 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 140) & (SoldPigsDF['weight'] <= 105)]
        pigs_20 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 130) & (SoldPigsDF['weight'] <= 105)]
        pigs_25 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 125) & (SoldPigsDF['weight'] <= 105)]
        pigs_30 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 120) & (SoldPigsDF['weight'] <= 105)]
        pigs_35 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 115) & (SoldPigsDF['weight'] <= 105)]
        pigs_45 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 105) & (SoldPigsDF['weight'] <= 105)]
        pigs_50 = SoldPigsDF.loc[(SoldPigsDF['Price Per KG'] == 100) & (SoldPigsDF['weight'] <= 105)]

        # Add the numbers of pigs in each penalty group to the relevant lists
        total_sold.append(len(SoldPigsDF))
        over.append(len(pigs_over))
        opt.append(len(pigs_opt))
        p10.append(len(pigs_10))
        p20.append(len(pigs_20))
        p25.append(len(pigs_25))
        p30.append(len(pigs_30))
        p35.append(len(pigs_35))
        p45.append(len(pigs_45))
        p50.append(len(pigs_50))

    # Make a Pandas dataframe with the data, save to csv
    resultsDF = pd.DataFrame({'Run': run_num, 'Total Pigs Sold': total_sold, 'Overweight': over, 'No Penalty': opt, '-10p/kg': p10, '-20p/kg': p20, '-25p/kg': p25, '-30p/kg': p30, '-35p/kg': p35, '-45p/kg': p45, '-50p/kg': p50})
    resultsDF.to_csv("ResultsDF.csv")
else:
    resultsDF = pd.read_csv('ResultsDF.csv')

resultsDF['% optimal'] = 100*resultsDF["No Penalty"]/resultsDF["Total Pigs Sold"]

print(f"Averaged over {n_runs} runs of the simulation, {resultsDF['% optimal'].mean()}% of pigs are sold with no penalty.")