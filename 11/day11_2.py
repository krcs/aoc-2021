#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./test.txt"
#source = "sample.txt"

def read_lines(file):
    result = []
    with open(file,"r") as f:
        while True:
            line = f.readline().strip()
            
            if len(line)>0:
                result.append([ int(e) for e in line ])

            if not line:
                break
    return result

offsets = ( (-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1) )

a = np.array(read_lines(source))
height, width = a.shape

def light(x,y, a):
    for o in offsets:
        dx = x + o[0]
        dy = y + o[1]
        if dx >=0 and dx < width and dy >=0 and dy < height:
            if a[dy][dx] == 10:
                continue

            a[dy][dx] += 1
            
            if a[dy][dx] == 10:
                light(dx,dy,a)

step = 0

while True:
    highs = []

    for y in range(height):
        for x in range(width):
            a[y][x] += 1
            if a[y][x] == 10:
                highs.append([x,y])

    for h in highs:
        light(h[0],h[1],a)

    for y in range(height):
        for x in range(width):
            if a[y][x] == 10:
                a[y][x] = 0

    step +=1

    if np.count_nonzero(a) == 0:
        break

print(step)
