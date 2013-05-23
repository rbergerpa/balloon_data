import matplotlib.pyplot as plt
from json_util import load_json
import lat_lon
import datetime as dt

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def load_data(path):
    """load the data into a list of dicts
    """
    json_data = list(load_json(path))
    for d in json_data:
        d['time'] = dt.datetime.strptime(d['time'], DATE_FORMAT)

    return json_data


gps_data = load_data('c1_gps.txt')

# Calculate speed using raw GPS lat/lon data
data_speed = []
data_timestamp = []
data_altitude = []
for i in range(len(gps_data)-1):
    time1 = gps_data[i]['time']
    lat1 = gps_data[i]['lat']
    lon1 = gps_data[i]['lon']
    altitude1 = gps_data[i]['hgt']

    time2 = gps_data[i+1]['time']
    lat2 = gps_data[i+1]['lat']
    lon2 = gps_data[i+1]['lon']
    altitude2 = gps_data[i+1]['hgt']

    # perform calculations
    time_difference = time2 - time1
    time = time1 + (time_difference)/2
    altitude = altitude1 + (altitude2 - altitude1)/2
    distance = lat_lon.distance(lat1, lon1, lat2, lon2)  # in miles
    speed = (distance * 60 * 60)/(time_difference.seconds)  # miles per hour

    # push the calculated data points into lists
    data_speed.append(speed)
    data_timestamp.append(time)
    data_altitude.append(altitude)

# split the lists at the max altitude
max_altitude = max(data_altitude)
max_altitude_index = data_altitude.index(max_altitude)

data_speed_ascending = data_speed[:max_altitude_index]
data_timestamp_ascending = data_timestamp[:max_altitude_index]
data_altitude_ascending = data_altitude[:max_altitude_index]

data_speed_descending = data_speed[max_altitude_index:]
data_timestamp_descending = data_timestamp[max_altitude_index:]
data_altitude_descending = data_altitude[max_altitude_index:]


# plot speed over time
plt.figure(1)
plt.plot(data_timestamp_ascending, data_speed_ascending, label="Ascending")
plt.plot(data_timestamp_descending, data_speed_descending, label="Descending")
plt.legend()
plt.title("Speed vs. Time")
axes = plt.axes()
axes.set_ylabel("Speed (MPH)")
axes.set_xlabel("Time")

# plot speed across altitude, split the series at the highest point
plt.figure(2)
plt.plot(data_altitude_ascending, data_speed_ascending, label="Ascending")
plt.plot(data_altitude_descending, data_speed_descending, label="Descending")
plt.legend()
plt.title("Speed vs. Altitude")
axes = plt.axes()
axes.set_ylabel("Speed (Miles per hour)")
axes.set_xlabel("Altitude (Feet)")

# show both plots
plt.show()
