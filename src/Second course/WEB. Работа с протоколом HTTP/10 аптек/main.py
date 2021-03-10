import shutil

import requests


search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address = input("Введите адрес: ")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode="
                        f"{address}&format=json")
data = response.json()
coord = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": ",".join(coord),
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass
json_response = response.json()

points = []
for element in json_response["features"]:
    point = element["geometry"]["coordinates"]
    org_point = "{0},{1},pm".format(point[0], point[1])

    if "CompanyMetaData" not in element["properties"]\
        or "Hours" not in element["properties"]["CompanyMetaData"]\
            or "Availabilities" not in element["properties"]["CompanyMetaData"]["Hours"]\
                or "Everyday" not in element["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]:
        org_point += "gr"
    elif element["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]["Everyday"]:
        org_point += "gn"
    else:
        org_point += "bl"

    points.append(org_point + "m")

map_params = {
    "l": "map",
    "pt": "~".join(points),
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params, stream=True)
with open("image.png", "wb") as out_file:
    shutil.copyfileobj(response.raw, out_file)
