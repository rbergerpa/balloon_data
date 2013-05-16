from math import *

EARTH_RADIUS = 3959.0 # Statute miles

# Returns the distance in statute miles between to geographic locations
# given their latitudes and longitudes in degrees
def distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # from "The Satellite Experimenter's Handbook" by Martin R. Davidoff
    cosBeta = sin(lat1) * sin(lat2) + cos(lat1) *cos(lat2) * cos(lon1 - lon2)
    return EARTH_RADIUS * acos(cosBeta)


# Test application
if  __name__ == "__main__":
    print cos(radians(45))

    lat1 = float(raw_input("Latitude 1: "))
    lon1 = float(raw_input("Longitude 1: "))
    lat2 = float(raw_input("Latitude 2: "))
    lon2 = float(raw_input("Longitude 2: "))

    print "Distance is", distance(lat1, lon1, lat2, lon2)






