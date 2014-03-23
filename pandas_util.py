from pandas import DataFrame
from json_util import load_json
import datetime as dt

# load_json_dataframe(path)
#   loads a Pandas DataFrame from a JSON file, indexed by the 'time' property

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def select_time(dict):
    return dict['time']

def load_json_dataframe(path):
    json_data = list(load_json(path))
    for d in json_data:
        d['time'] = dt.datetime.strptime(d['time'], DATE_FORMAT)

    return DataFrame(data=json_data, index=map(select_time, json_data))
