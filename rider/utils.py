import math

def calculate_pickup_distance(pickup_latitude, pickup_longitude, latitude, longitude):
    latitude_difference = pickup_latitude - latitude
    longitude_difference = pickup_longitude - longitude

    distance = math.sqrt(latitude_difference**2 + longitude_difference**2)

    return distance
