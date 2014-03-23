#!/bin/sh

python plot.py hgt "Altitude (feet)"

python vert_speed.py

python vert_speed_hgt.py

python plot.py temp3 "Temperature (Celsius)"

python temp_vs_hgt.py

python speed.py
