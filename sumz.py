import requests as req
import json
import math
import random

# Dependencies
from citipy import citipy

# Some random coordinates

cities = []
for coordinate_pair in range(0,10):

    latitude = math.acos(random.random() * 2 - 1)
    longitude = random.random() * math.pi * 2
    print(citipy.nearest_city(latitude, longitude).zipcode)


