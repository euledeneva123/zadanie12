import folium
import requests
from geopy.distance import geodesic

# Ваш ключ API Яндекс
yandex_api_key = '05d9bbd4-d5ea-4269-85c4-2d6365537a74'

# Пример списка координат (последовательность точек)
path_coords = [
    [55.751244, 37.618423],  # Красная площадь
    [55.755826, 37.617300],  # ГУМ
    [55.758986, 37.610010]   # Александровский сад
]

# Создаем карту
map_with_path = folium.Map(location=[55.751244, 37.618423], zoom_start=13)

# Добавляем путь на карту
folium.PolyLine(path_coords, color="blue", weight=2.5, opacity=1).add_to(map_with_path)

# Вычисляем среднюю точку пути
mid_index = len(path_coords) // 2
mid_point = path_coords[mid_index]

# Добавляем метку в средней точке
folium.Marker(location=mid_point, popup="Mid Point").add_to(map_with_path)

# Сохраняем карту в HTML файл
map_with_path.save("moscow_path_map.html")

# Вычисляем длину пути
total_distance = 0
for i in range(len(path_coords) - 1):
    total_distance += geodesic(path_coords[i], path_coords[i + 1]).meters

print(f"Длина пути: {total_distance:.2f} метров")

# Получаем карту с помощью API Yandex и отмечаем путь
points = "~".join([f"{coords[1]},{coords[0]}" for coords in path_coords])
response = requests.get(
    f"https://static-maps.yandex.ru/1.x/?l=map&pl={points}",
    params={'apikey': yandex_api_key}
)
with open("path_map.png", "wb") as file:
    file.write(response.content)
