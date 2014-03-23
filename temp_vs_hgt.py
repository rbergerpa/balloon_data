import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe
import sys

gps_data = load_json_dataframe('c1_gps.txt')
logger_data = load_json_dataframe('c1_data.txt')

temp = logger_data['temp3']

height = []
for i in range(0, temp.size):
    height.append(gps_data['hgt'].asof(temp.index[i]))

plt.plot(height, temp)

axes = plt.axes()
axes.set_ylabel("Temperature (Celcius)")
axes.set_xlabel("Altitude (feet)")

plt.show()
