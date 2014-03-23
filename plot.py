import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe
import sys

# Convert a series indexed by time to a series indexed by altitude, 
#     by combining the given series with the altitude vs time from gps_data
def by_altitude(series):
    df = DataFrame({'Value': series, 'Altitude': gps_data.hgt.reindex(series.index, method='ffill')})
    return df.set_index('Altitude')['Value'].sort_index()


gps_data = load_json_dataframe('c1_gps.txt')
logger_data = load_json_dataframe('c1_data.txt')

# Use the GPS data to determine the time of maximum altitude
max_altitude_time = gps_data['hgt'].idxmax()

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
    p = DataFrame({'Ascending': by_altitude(ascending), 'Descending': by_altitude(descending)}).plot()
    p.set_ylabel(y_label)
    p.set_xlabel("Altitude")

# show both plots
plt.show()
