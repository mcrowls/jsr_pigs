import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SoldPigsDF = pd.read_csv('SoldPigsDF.csv')
SoldPigsDF["Price Per KG"] = (SoldPigsDF["earning"]/SoldPigsDF["weight"]).round()

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

# Print the numbers and percentages of pigs in each penalty group
print(f"Total number of pigs = {len(SoldPigsDF)}")

print("Number of pigs sold...")
print(f"    overweight (£110 fixed) = {len(pigs_over)}")
print(f"    optimal (no penalty)    = {len(pigs_opt)}")
print(f"    -10p/kg penalty         = {len(pigs_10)}")
print(f"    -20p/kg penalty         = {len(pigs_20)}")
print(f"    -25p/kg penalty         = {len(pigs_25)}")
print(f"    -30p/kg penalty         = {len(pigs_30)}")
print(f"    -35p/kg penalty         = {len(pigs_35)}")
print(f"    -45p/kg penalty         = {len(pigs_45)}")
print(f"    -50p/kg penalty         = {len(pigs_50)}")

print("Percentage of pigs sold...")
print(f"    overweight (£110 fixed) = {100*len(pigs_over)/len(SoldPigsDF)}%")
print(f"    optimal (no penalty)    = {100*len(pigs_opt)/len(SoldPigsDF)}%")
print(f"    -10p/kg penalty         = {100*len(pigs_10)/len(SoldPigsDF)}%")
print(f"    -20p/kg penalty         = {100*len(pigs_20)/len(SoldPigsDF)}%")
print(f"    -25p/kg penalty         = {100*len(pigs_25)/len(SoldPigsDF)}%")
print(f"    -30p/kg penalty         = {100*len(pigs_30)/len(SoldPigsDF)}%")
print(f"    -35p/kg penalty         = {100*len(pigs_35)/len(SoldPigsDF)}%")
print(f"    -45p/kg penalty         = {100*len(pigs_45)/len(SoldPigsDF)}%")
print(f"    -50p/kg penalty         = {100*len(pigs_50)/len(SoldPigsDF)}%")