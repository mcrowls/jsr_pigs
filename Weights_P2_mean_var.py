import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

def nd_maker():
    weight_csv = pd.read_csv('/Users/jakebeard/Documents/GitHub/jsr_pigs/Weight_Data.csv')

    dates = weight_csv['Date']
    number_of_pigs = weight_csv['Number pigs']
    total_weight = weight_csv['Total weight']
    ave_weight = weight_csv['Average Weight']
    ave_P2 = weight_csv['P2']
    weight_out = weight_csv['Weight Out']



    total_weight_all = 0
    total_weight_out = 0
    total_p2 = 0
    i_count = 0
    for i in range(np.shape(total_weight)[0]):
        total_weight_all += total_weight[i]/number_of_pigs[i]
        total_weight_out += weight_out[i]*number_of_pigs[i]
        total_p2 += ave_P2[i]*number_of_pigs[i]
        i_count += 1

    mean_weight = total_weight_all/i_count
    mean_weight_out = total_weight_out/sum(number_of_pigs)

    mean_p2 = total_p2/sum(number_of_pigs)
    # finds the standard deviation of pigs weights and P2
    i_count = 0
    for i in range(np.shape(total_weight)[0]):
        ave_weight_i = total_weight[i]/number_of_pigs[i]

        sum_weight_out_sd = (weight_out[i]-mean_weight_out)**2
        sum_weight_sd = (ave_weight_i-mean_weight)**2
        sum_sd_P2 = (ave_P2[i]-mean_p2)**2


        i_count += 1

    var_weight = sum_weight_sd/i_count
    var_weight_out = sum_weight_out_sd/i_count
    var_p2= sum_sd_P2/i_count


    # creates two random normal distributions that can be used in models
    weight_ND = np.random.normal(mean_weight,var_weight, 1000)
    weight_out_ND = np.random.normal(mean_weight_out,var_weight_out, 1000)
    print(mean_weight_out, var_weight_out)
    P2_ND = np.random.normal(mean_p2,var_p2, 1000)

    # plots the normal distributions

    x = np.linspace(mean_weight - 3*np.sqrt(var_weight),mean_weight + 3*np.sqrt(var_weight), 100)
    plt.plot(x, stats.norm.pdf(x, mean_weight, np.sqrt(var_weight)))
    plt.xlabel('weight of pigs')
    plt.ylabel('weight (kg)')
    plt.legend(loc='best')

    x = np.linspace(mean_weight_out - 3*np.sqrt(var_weight_out),mean_weight_out + 3*np.sqrt(var_weight_out), 100)
    plt.plot(x, stats.norm.pdf(x, mean_weight_out, np.sqrt(var_weight_out)))

    x = np.linspace(mean_p2 - 3*np.sqrt(var_p2),mean_p2 + 3*np.sqrt(var_p2), 100)
    plt.plot(x, stats.norm.pdf(x, mean_p2, np.sqrt(var_p2)))







nd_maker()




#useless piece of code
import statistics as st

def mean_and_var(data):
    mu = st.mean(data)
    var = st.variance(data)
    return mu, var

ave_weight_all = 0
for i in range(np.shape(ave_weight)[0]):
    ave_weight_all += ave_weight[i]*number_of_pigs[i]
total_num_pigs = sum(number_of_pigs)
mean_ave_weight = ave_weight_all/total_num_pigs



total_weight_mean, total_weight_var = mean_and_var(total_weight)
ave_weight_mean, ave_weight_var = mean_and_var(total_weight)

P2_mean, P2_var = mean_and_var(ave_P2)
