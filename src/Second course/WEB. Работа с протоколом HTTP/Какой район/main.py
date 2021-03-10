import requests

geocode_api_server = "http://geocode-maps.yandex.ru/1.x/"
apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

address = input("Введите адрес: ")
response = requests.get(f"{geocode_api_server}?apikey={apikey}&geocode="
                        f"{address}&format=json")
data = response.json()
coord = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

response = requests.get(f"{geocode_api_server}?apikey={apikey}&geocode="
                        f"{', '.join(coord)}&kind=district&format=json")

obj = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]
obj = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
districts = list(filter(lambda e: e["kind"] == "district", obj))

for district in districts:
    print("Район:", district["name"])
