from pandas import DataFrame
from json_util import load_json
import datetime as dt

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def select_time(dict):
    return dict['time']

#  load a Pandas DataFrame from a JSON file, indexed by the 'time' property
def load_json_dataframe(path):
    json_data = list(load_json(path))
    for d in json_data:
        d['time'] = dt.datetime.strptime(d['time'], DATE_FORMAT)

    return DataFrame(data=json_data, index=map(select_time, json_data))

# Convert a series indexed by time to a series indexed by altitude, 
#     by combining the given series with the altitude vs time from gps_data
def by_altitude(series, gps_data):
    df = DataFrame({'Value': series, 'Altitude': gps_data.hgt.reindex(series.index, method='ffill')})
    return df.set_index('Altitude')['Value'].sort_index()
