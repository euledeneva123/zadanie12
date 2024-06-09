import random
import requests
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Список городов с координатами
cities = {
    "Moscow": "37.6176,55.7558",
    "Saint Petersburg": "30.3158,59.9398",
    "Novosibirsk": "82.9235,55.0282",
    "Yekaterinburg": "60.6122,56.8519",
    "Nizhny Novgorod": "44.0020,56.3269"
}

# API ключ для Яндекс.Карт
YANDEX_API_KEY = '4127ba63-b369-45aa-9967-8b0a0886845e'

# Перемешанный список городов
city_names = list(cities.keys())
random.shuffle(city_names)

# Индекс текущего города
current_index = 0

# Функция для получения случайного изображения города
def get_random_city_image(city, api_key):
    # Определение типа изображения (карта или спутник)
    map_types = ["map", "sat"]
    map_type = random.choice(map_types)

    # Установка высокого уровня зума, чтобы название города не отображалось
    zoom = random.randint(15, 17)

    # Создание URL для запроса
    city_coordinates = cities[city]
    url = f"https://static-maps.yandex.ru/1.x/?ll={city_coordinates}&z={zoom}&size=650,450&l={map_type}&apikey={api_key}"

    # Выполнение запроса к API и получение изображения
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        try:
            image = Image.open(BytesIO(response.content))
            return image
        except Exception as e:
            print(f"Ошибка при открытии изображения для города {city}: {e}")
    else:
        print(f"Не удалось получить изображение для города {city}. Код ответа: {response.status_code}")

    return None

# Функция для отображения текущего города
def show_current_city(event=None):
    global current_index
    city = city_names[current_index]
    image = get_random_city_image(city, YANDEX_API_KEY)
    if image:
        ax.imshow(image)
        ax.set_title("Угадайте город!")
        plt.draw()

# Функция для показа следующего города
def next_city(event):
    global current_index
    current_index = (current_index + 1) % len(city_names)
    show_current_city()

# Функция для показа предыдущего города
def prev_city(event):
    global current_index
    current_index = (current_index - 1) % len(city_names)
    show_current_city()

# Инициализация графического интерфейса
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

# Кнопка "Предыдущий"
axprev = plt.axes([0.1, 0.05, 0.1, 0.075])
bprev = Button(axprev, 'Предыдущий')
bprev.on_clicked(prev_city)

# Кнопка "Следующий"
axnext = plt.axes([0.8, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Следующий')
bnext.on_clicked(next_city)

# Показ первого города
show_current_city()

plt.show()
