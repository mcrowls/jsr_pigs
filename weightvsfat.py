import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


file = pd.read_csv('Weight_Data.csv')

weight = np.array(file['Weight Out'])
fat = np.array(file['P2'])
plt.scatter(weight, fat, label='Data')
coeffs = stats.linregress(weight, fat)
x = np.linspace(np.min(weight), np.max(weight), 1000)
y = coeffs[1] + coeffs[0]*x
plt.plot(x, y, 'r-', label='Regression Line')
plt.xlabel('Weight(kg)')
plt.ylabel('Backfat(cm)')
plt.legend(loc='best')
plt.show()
print(coeffs[0])
print('slope = ', coeffs[0])
print('intercept = ', coeffs[1])
