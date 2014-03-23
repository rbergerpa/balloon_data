import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from json_util import load_json
import datetime as dt
import sys

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

field = sys.argv[1]

def select_time(dict):
    return dict['time']

def load_data(path):
    json_data = list(load_json(path))
    for d in json_data:
        d['time'] = dt.datetime.strptime(d['time'], DATE_FORMAT)

    return DataFrame(data=json_data, index=map(select_time, json_data))

gps_data = load_data('c1_gps.txt')
logger_data = load_data('c1_data.txt')

max_altitude_time = gps_data['hgt'].idxmax()

try:
    ascending = logger_data.ix[logger_data.time <= max_altitude_time][field]
    descending = logger_data.ix[logger_data.time >= max_altitude_time][field]
except:
    ascending = gps_data.ix[gps_data.time <= max_altitude_time][field]
    descending = gps_data.ix[gps_data.time >= max_altitude_time][field]

data = DataFrame({'Ascending': ascending, 'Descending': descending})

p = data.plot()

if len(sys.argv) == 3:
    y_label = sys.argv[2]
else:
    y_label = sys.argv[1]

p.set_ylabel(y_label)
p.set_xlabel("Time")

plt.show()
