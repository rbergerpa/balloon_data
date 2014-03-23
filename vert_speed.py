import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe, by_altitude
from datetime import timedelta
import sys

gps_data = load_json_dataframe('c1_gps.txt')

hgt = gps_data['hgt']
# Delete the samples when the balloon was on the ground
hgt = hgt[4:hgt.size-15]

max_altitude_time = hgt.idxmax()
max_altitude = hgt.max()

# delta is the height difference between samples shifted by 2 minutes
delta = hgt.shift(-1, 'min') - hgt.shift(1, 'min')

miles = delta / 5280.0
mph = miles * 30  # delta shift is 30 periods per hour

offset = timedelta(minutes = 1)
ascending = mph.ix[mph.index < max_altitude_time - offset]
descending = mph.ix[mph.index > max_altitude_time- offset]

# Plot vertical speed vs time
p = DataFrame({'Ascending': ascending, 'Descending': descending}).plot()
p.set_ylabel("Vertical Speed (MPH)")
p.set_xlabel("Time")
plt.show()

# Plot descent speed vs altitude
b = by_altitude(descending, gps_data)
b = b.ix[b.index < max_altitude - 1000] # Time window causes artifacs at the altitude peak
p = b.plot()
p.set_ylabel("Descent Speed (MPH)")
p.set_xlabel("Altitude")
plt.show()
