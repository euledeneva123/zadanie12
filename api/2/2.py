import requests

def save_satellite_image(latitude, longitude, filename="satellite_image.png", api_key="YOUR_API_KEY"):
    # Формируем URL запроса к Yandex Static Maps API
    url = f"https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&z=15&l=sat&size=650,450&apikey={api_key}"

    # Отправляем GET-запрос и сохраняем изображение в файл
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Снимок спутника успешно сохранен в файле: {filename}")
    else:
        print("Ошибка при получении изображения спутника")

# Пример использования функции
latitude = input("Введите широту объекта: ")
longitude = input("Введите долготу объекта: ")
filename = input("Введите имя файла для сохранения: ")

save_satellite_image(latitude, longitude, filename=filename, api_key="YOUR_API_KEY")
