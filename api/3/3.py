import requests
from PIL import Image
from io import BytesIO

# Вставьте ваш API-ключ
API_KEY = '4127ba63-b369-45aa-9967-8b0a0886845e'


def get_map_image(lat, lon, zoom=15, size=(650, 450), layer='map'):
    # URL для запроса снимка карты
    url = f'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={zoom}&size={size[0]},{size[1]}&l={layer}&apikey={API_KEY}'

    # Вывод URL для проверки
    print(f"Request URL: {url}")

    # Выполнение запроса
    response = requests.get(url)

    # Проверка статуса запроса
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception(f"Error: Unable to get image. Status code: {response.status_code}, Message: {response.text}")


def save_image(image, filename):
    # Сохранение изображения в файл
    image.save(filename, 'PNG')


if __name__ == '__main__':
    # Пример координат (Широта, Долгота)
    latitude = 55.751244
    longitude = 37.618423

    try:
        # Получение снимка карты
        image = get_map_image(latitude, longitude, layer='map')

        # Сохранение снимка в файл
        save_image(image, 'map_image.png')

        print("Снимок карты сохранён в 'map_image.png'")
    except Exception as e:
        print(e)
