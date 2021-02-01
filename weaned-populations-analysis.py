'''
Assess each population of pigs (split based on weaning date) and plot all population numbers on the same graph
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from dataReader import farrow_and_weaning_data_reader, death_weights_data_reader

print(death_weights_data_reader())