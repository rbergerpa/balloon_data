import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe
import sys

gps_data = load_json_dataframe('c1_gps.txt')
logger_data = load_json_dataframe('c1_data.txt')

max_altitude_time = gps_data['hgt'].idxmax()

ascending_temp = logger_data.ix[logger_data.time <= max_altitude_time]['temp3']
descending_temp = logger_data.ix[logger_data.time >= max_altitude_time]['temp3']

height = []
for i in range(0, ascending_temp.size):
    height.append(gps_data['hgt'].asof(ascending_temp.index[i]))
plt.plot(height, ascending_temp)

height = []
for i in range(0, descending_temp.size):
    height.append(gps_data['hgt'].asof(descending_temp.index[i]))
plt.plot(height, descending_temp)


axes = plt.axes()
axes.set_ylabel("Temperature (Celcius)")
axes.set_xlabel("Altitude (feet)")

plt.show()
