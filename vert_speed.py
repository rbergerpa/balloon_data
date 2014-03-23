import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from pandas_util import load_json_dataframe
import sys

gps_data = load_json_dataframe('c1_gps.txt')

hgt = gps_data['hgt']
# Delete the samples when the balloon was on the ground
hgt = hgt[4:hgt.size-15]

# delta is the height difference between samples shifted by 2 minutes
delta = hgt.shift(-1, 'min') - hgt.shift(1, 'min')

miles = delta / 5280.0

mph = miles * 30  # delta shift is 30 periods per hour

p = mph.plot()
p.set_ylabel("Vertical Speed (MPH)")
p.set_xlabel("Time")

plt.show()
