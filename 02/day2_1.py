#!/usr/bin/python3
table = []

f = open("./input.txt","r")
while True:
    line = f.readline()

    if not line:
        break

    m = line.strip()
    table.append(m)

f.close()

horizontal = 0
depth = 0

for line in table:
    c = line.split(" ")
    if c[0] == "forward":
        horizontal += int(c[1])
    elif c[0] == "down":
        depth += int(c[1])
    elif c[0] == "up":
        depth -= int(c[1])

print(horizontal*depth)
