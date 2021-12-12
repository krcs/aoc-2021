#!/usr/bin/python3
result = 0
previous = None

f = open("./input.txt","r")
while True:
    line = f.readline()

    if not line:
        break

    m = int(line.strip())

    if previous == None:
        previous = m
        continue

    if m > previous:
        result += 1

    previous = m

f.close()
print(result)
