#!/bin/sh

python plot.py hgt "Altitude (feet)"

python plot.py temp3 "Temperature (Celsius)"

python vert_speed.py

python vert_speed_hgt.py

python speed.py
