import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from json_util import load_json
import datetime as dt
import sys

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def select_time(dict):
    return dict['time']

def load_data(path):
    json_data = list(load_json(path))
    for d in json_data:
        d['time'] = dt.datetime.strptime(d['time'], DATE_FORMAT)

    return DataFrame(data=json_data, index=map(select_time, json_data))


gps_data = load_data('c1_gps.txt')

hgt = gps_data['hgt']
# Delete the samples when the balloon was on the ground
hgt = hgt[6:hgt.size-15]

# delta is the height difference between samples shifted by 2 minutes
delta = hgt.shift(-1, 'min') - hgt.shift(1, 'min')

miles = delta / 5280.0

mph = miles * 30  # delta shift is 30 periods per hour

# resample height to the time indices of mph
height = []
for i in range(0, mph.size):
    height.append(hgt.asof(mph.index[i]))

plt.plot(height, mph)

axes = plt.axes()
axes.set_ylabel("Vertical Speed (MPH)")
axes.set_xlabel("Altitude (feet)")

plt.show()
