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

try:
    logger_data[field].plot()
except:
    gps_data[field].plot()

plt.show()

