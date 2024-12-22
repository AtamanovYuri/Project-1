import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def show_data(day, date):
    NationStates = np.load("States.npy")
    NationStates = NationStates.astype(str)
    NationStates = np.char.replace(NationStates, '_', ' ')
    data = np.load("data.npy")
    data = data.astype(int)
    Freedom_data = [0]*len(data)
    Tolerance_data = [0]*len(data)
    Size_data = [0]*len(data)
    Economic_data_left = [0]*len(data)
    Economic_data_right = [0]*len(data)

 
    for i in range(0, len(data)):
        Size_data[i] = data[i][0]*(1 - day/data[i][1])/10
        Freedom_data[i] = int((data[i][2]-50) + (data[i][3]-50))/2
        Tolerance_data[i] = int((data[i][4]-50) + (data[i][5]/2-50))/2
        if Freedom_data[i] > 50:
            Freedom_data[i] = 50
        if Tolerance_data[i] > 50:
            Tolerance_data[i] = 50
        if data[i][6] > 50:
            if data[i][6] > 100:
                Economic_data_left[i] = 0
                Economic_data_right[i] = 1
            else:
                Economic_data_left[i] = 0
                Economic_data_right[i] = data[i][6]/100
        if data[i][6] < 50:
            if data[i][6] < 0:
                Economic_data_left[i] = 1
                Economic_data_right[i] = 0
            else:
                Economic_data_left[i] = data[i][6]/100
                Economic_data_right[i] = 0
 
 
 
    plt.figure(figsize = (7, 7))
    plt.title(date)
    plt.xlabel('Less Freedom                                                         More Freedom')
    plt.ylabel('Less Tolerance                                                                More Tolerance', rotation=90)
    plt.xlim(-55, 55)
    plt.ylim(-55, 55)
    for i in range(0, len(data)):
        if Freedom_data[i] != 1898:
            plt.scatter(Freedom_data[i], Tolerance_data[i], Size_data[i], (Economic_data_left[i], 0, Economic_data_right[i], Economic_data_left[i]+Economic_data_right[i]))
        else:
            continue
    for i in range(0, len(data)):
        if Freedom_data[i] != 1898:
            plt.annotate(NationStates[i], (Freedom_data[i], Tolerance_data[i]), horizontalalignment='center', fontsize = 6)
        else:
            continue
    plt.savefig("figure"+str(day)+".png")
    # plt.show()
