import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd


def get_data_frame(path):
	data_frame = pd.read_csv(path)
	return data_frame
