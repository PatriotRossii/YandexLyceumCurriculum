import random
from io import BytesIO

import psutil as psutil
import requests
from PIL import Image
import time

from utils import get_spn

view = ["map", "sat"]
towns = ["Тверь", "Канберра", "Торонто", "Монреаль",
         "Пхеньян", "Сеул", "Токио", "Хошимин", "Ханой",
         "Нью-Йорк", "Феникс", "Лос-Анджелес", "Остин"]
random.shuffle(towns)

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
for town in towns:
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": town,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    entropy = [random.uniform(0, float(e) - float(e) / 4) for e in get_spn(toponym)]
    map_params = {
        "ll": ",".join([str(float(toponym_longitude) + entropy[1]), str(float(toponym_lattitude) + entropy[0])]),
        "l": random.sample(view, 1)[0],
        "z": 16
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    image = Image.open(BytesIO(response.content))
    image.show()

    time.sleep(5)