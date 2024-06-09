import requests

# Вставьте ваш API-ключ для Geocoder API
GEOCODER_API_KEY = '05d9bbd4-d5ea-4269-85c4-2d6365537a74'

# Вставьте ваш API-ключ для Places API
PLACES_API_KEY = '0e3cc287-425f-4545-8c29-5c00c5cfccf8'


# Функция для получения координат по адресу с помощью API Яндекса
def get_coordinates_by_address(address):
    try:
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={GEOCODER_API_KEY}&geocode={address}&format=json'
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
            print(f"Координаты для адреса '{address}' не найдены.")
            return None, None
    except Exception as e:
        print(f"Ошибка при получении координат для адреса '{address}': {e}")
        return None, None


# Функция для поиска ближайших аптек с помощью Places API Яндекса
def get_nearest_pharmacy(lat, lon):
    try:
        url = f'https://search-maps.yandex.ru/v1/?apikey={PLACES_API_KEY}&text=аптека&ll={lon},{lat}&lang=ru_RU&type=biz&results=1'
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        data = response.json()

        if data['features']:
            pharmacy = data['features'][0]
            name = pharmacy['properties']['CompanyMetaData']['name']
            address = pharmacy['properties']['CompanyMetaData']['address']
            coordinates = pharmacy['geometry']['coordinates']
            return name, address, coordinates
        else:
            print("Рядом не найдено аптек.")
            return None, None, None
    except Exception as e:
        print(f"Ошибка при поиске ближайшей аптеки: {e}")
        return None, None, None


# Главная функция
def main():
    address = input("Введите адрес: ")

    lat, lon = get_coordinates_by_address(address)

    if lat is not None and lon is not None:
        name, pharmacy_address, coordinates = get_nearest_pharmacy(lat, lon)

        if name:
            print(f"Ближайшая аптека: {name}")
            print(f"Адрес: {pharmacy_address}")
            print(f"Координаты: {coordinates}")
        else:
            print("Не удалось найти ближайшую аптеку.")
    else:
        print("Не удалось определить координаты адреса.")


if __name__ == '__main__':
    main()
