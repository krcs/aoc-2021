#!/usr/bin/python3
table = []

f = open("./input.txt","r")
while True:
    line = f.readline()

    if not line:
        break

    m = int(line.strip())
    table.append(m)

f.close()

result = 0
previous = None

for i in range(len(table)-2):

    s = sum([ table[n] for n in range(i, i+3) ])

    if previous == None:
        previous = s
        continue

    if s > previous:
        result += 1

    previous = s

print(result)
