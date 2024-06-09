import requests

# Вставьте ваш API-ключ
API_KEY = '05d9bbd4-d5ea-4269-85c4-2d6365537a74'


# Функция для получения координат города с помощью API Яндекса
def get_city_coordinates(city_name):
    try:
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city_name}&format=json'
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        data = response.json()

        if data['response']['GeoObjectCollection']['featureMember']:
            geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
            coordinates = geo_object['Point']['pos'].split()
            longitude = float(coordinates[0])
            latitude = float(coordinates[1])
            return latitude, longitude
        else:
            raise Exception(f"Coordinates for {city_name} not found.")
    except Exception as e:
        print(f"Error fetching coordinates for {city_name}: {e}")
        return None, None


# Функция для определения южного города
def find_southernmost_city(cities):
    southernmost_city = None
    southernmost_latitude = float('inf')

    for city in cities:
        lat, lon = get_city_coordinates(city)
        if lat is not None and lon is not None:
            print(f"{city}: ({lat}, {lon})")  # вывод координат города
            if lat < southernmost_latitude:
                southernmost_latitude = lat
                southernmost_city = city

    return southernmost_city


# Главная функция
def main():
    city_list = input("Введите список городов через запятую: ").split(',')
    city_list = [city.strip() for city in city_list]

    southernmost_city = find_southernmost_city(city_list)

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить координаты городов.")


if __name__ == '__main__':
    main()
