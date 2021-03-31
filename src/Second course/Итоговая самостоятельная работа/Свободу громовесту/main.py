import sys

lines = [e.strip() for e in sys.stdin.readlines()]
for line in lines:
    while "AAA" in line:
        line = line.replace("AAA", "BB", 1)
        line = line.replace("BBB", "AA", 1)

    print(line)