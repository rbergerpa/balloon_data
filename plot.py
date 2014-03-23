import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe
import sys

field = sys.argv[1]

gps_data = load_json_dataframe('c1_gps.txt')
logger_data = load_json_dataframe('c1_data.txt')

max_altitude_time = gps_data['hgt'].idxmax()

# Set ascendeing and descending each to a Series of the specified field vs. time
try:
    ascending = logger_data.ix[logger_data.time <= max_altitude_time, field]
    descending = logger_data.ix[logger_data.time >= max_altitude_time, field]
except:
    ascending = gps_data.ix[gps_data.time <= max_altitude_time , field]
    descending = gps_data.ix[gps_data.time >= max_altitude_time, field]

# Plot the ascending and descending series in different colors
p = DataFrame({'Ascending': ascending, 'Descending': descending}).plot()

if len(sys.argv) == 3:
    y_label = sys.argv[2]
else:
    y_label = sys.argv[1]

p.set_ylabel(y_label)
p.set_xlabel("Time")

plt.show()
