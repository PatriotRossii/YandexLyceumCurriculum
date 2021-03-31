import json
import csv

json_file = open('something_else.json')
json_data = json.loads(json_file.read())
json_file.close()

json_data = reversed(sorted(
    json_data,
    key=lambda e: e["name"]
))

with open('bestiary.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["name", "looks_like", "numbers", "to_hunt"])

    for element in json_data:
        writer.writerow([element["name"], element["looks_like"][0],
                         len(element["looks_like"]), element["to_hunt"]])
