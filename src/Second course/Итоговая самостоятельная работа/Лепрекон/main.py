import argparse
import csv
import json

from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str)
    parser.add_argument("--port", type=int)
    parser.add_argument("--file", type=str)
    args = parser.parse_args()

    response = {}
    with open(args.file, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

        for creature in reader:
            specie = creature["creature_type"]
            if specie not in response:
                response[specie] = {
                    "habitats": set(),
                    "colors": set(),
                    "heights": set(),
                    "feeds": set()
                }

            response[specie]["habitats"].add(
                creature["habitat"]
            )
            response[specie]["colors"].add(
                creature["color"]
            )
            response[specie]["heights"].add(
                creature["height"]
            )
            response[specie]["feeds"].add(
                creature["feeds_on"]
            )

        for key in response:
            for subkey in response[key]:
                response[key][subkey] = sorted(list(
                    response[key][subkey]
                ))
        resp = json.dumps(response)

        @app.route("/types")
        def types():
            return resp

    app.run(port=args.port, host=args.host)
