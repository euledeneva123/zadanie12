import requests

# API ключ для Яндекс.Карт
YANDEX_API_KEY = '05d9bbd4-d5ea-4269-85c4-2d6365537a74'

def get_coordinates(address, api_key):
    geocode_url = f"https://geocode-maps.yandex.ru/1.x/?geocode={address}&format=json&apikey={api_key}"
    response = requests.get(geocode_url)
    if response.status_code != 200:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None

    json_response = response.json()
    try:
        point = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        longitude, latitude = point.split(" ")
        return float(longitude), float(latitude)
    except (IndexError, KeyError):
        print("Не удалось получить координаты по данному адресу.")
        return None

def get_district(latitude, longitude, api_key):
    reverse_geocode_url = f"https://geocode-maps.yandex.ru/1.x/?geocode={longitude},{latitude}&kind=district&format=json&apikey={api_key}"
    response = requests.get(reverse_geocode_url)
    if response.status_code != 200:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None

    json_response = response.json()
    try:
        district = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
        return district
    except (IndexError, KeyError):
        print("Не удалось определить район по данным координатам.")
        return None

if __name__ == "__main__":
    address = input("Введите адрес: ")
    coordinates = get_coordinates(address, YANDEX_API_KEY)
    if coordinates:
        longitude, latitude = coordinates
        district = get_district(latitude, longitude, YANDEX_API_KEY)
        if district:
            print(f"Район для адреса '{address}': {district}")
        else:
            print(f"Район для адреса '{address}' не найден.")
    else:
        print(f"Не удалось получить координаты для адреса '{address}'.")
