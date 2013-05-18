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
logger_data = load_data('c1_data.txt')

temp = logger_data['temp3']

height = []
for i in range(0, temp.size):
    height.append(gps_data['hgt'].asof(temp.index[i]))

plt.plot(height, temp)

axes = plt.axes()
axes.set_ylabel("Temperature (Celcius)")
axes.set_xlabel("Altitude (feet)")

plt.show()
