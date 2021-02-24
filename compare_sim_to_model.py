import numpy as np
import pandas as pd

df = pd.read_csv('SoldPigsDF.csv')
df.drop(df.loc[df['dayInseminated']>31].index)

