import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe, by_altitude
import sys

gps_data = load_json_dataframe('c1_gps.txt')
logger_data = load_json_dataframe('c1_data.txt')


max_altitude_time = gps_data['hgt'].idxmax()
max_altitude = gps_data['hgt'].max()
print "Max altitude", max_altitude, " at ", max_altitude_time

field = sys.argv[1]

# Set ascendeing and descending each to a Series of the specified field vs. time
try:
    ascending = logger_data.ix[logger_data.time <= max_altitude_time, field]
    descending = logger_data.ix[logger_data.time >= max_altitude_time, field]
except:
    ascending = gps_data.ix[gps_data.time <= max_altitude_time , field]
    descending = gps_data.ix[gps_data.time >= max_altitude_time, field]

y_label = sys.argv[len(sys.argv)-1]

# Plot specified field vs time
p = DataFrame({'Ascending': ascending, 'Descending': descending}).plot()
p.set_ylabel(y_label)
p.set_xlabel("Time")

# Plot specified field vs altitude
if field != 'hgt':
    p = DataFrame({'Ascending': by_altitude(ascending, gps_data), 'Descending': by_altitude(descending, gps_data)}).plot()
    p.set_ylabel(y_label)
    p.set_xlabel("Altitude")

# show both plots
plt.show()
