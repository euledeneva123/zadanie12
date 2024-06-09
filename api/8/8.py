import math

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)

    return distance

home_lat, home_lon = map(float, input("Введите широту и долготу вашего дома через пробел: ").split())
uni_lat, uni_lon = map(float, input("Введите широту и долготу вашего университета через пробел: ").split())

distance = lonlat_distance((home_lon, home_lat), (uni_lon, uni_lat))
print(f"Расстояние между вашим домом и университетом примерно {distance:.2f} метров.")