import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")

parsed, unknown = parser.parse_known_args()

arguments = {}
for arg in unknown:
    key, value = arg.split("=")
    arguments[key] = value
    parser.add_argument(key)
arguments = arguments.items()

args = parser.parse_args()
if args.sort:
    arguments = sorted(arguments, key=lambda e: e[0])

for key, value in arguments:
    print(f"Key: {key}\tValue: {value}")
