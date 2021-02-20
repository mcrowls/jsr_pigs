import pandas as pd

farrowing_data = pd.read_csv('Farrowing Data Simple.csv')

# convert dates to timestamps
farrowing_data['Date Served'] = pd.to_datetime(farrowing_data['Date Served'])
farrowing_data['Date Farrowed'] = pd.to_datetime(farrowing_data['Date Farrowed'])

# calculate gestation length in days
farrowing_data['Gestation Length'] = farrowing_data['Date Farrowed'] - farrowing_data['Date Served']

# calculate mean gestation length in days
mean_gestation_length = farrowing_data['Gestation Length'].mean()
mean_gestation_length = mean_gestation_length.total_seconds()/(24*60**2)

# calculate standard deviation of gestation length in days
sd_gestation_length = farrowing_data['Gestation Length'].std()
sd_gestation_length = sd_gestation_length.total_seconds()/(24*60**2)

print(f"mean = {mean_gestation_length}")
print(f"sd   = {sd_gestation_length}")
