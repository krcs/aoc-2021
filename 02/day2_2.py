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
aim = 0

for line in table:
    c = line.split(" ")
    n = int(c[1])
    if c[0] == "forward":
        horizontal += n
        depth += aim * n
    elif c[0] == "down":
        aim += n
    elif c[0] == "up":
        aim -= n

print(horizontal*depth)
