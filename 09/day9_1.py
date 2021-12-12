#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./test.txt"

def read_array(file):
    result = []
    with open(file,"r") as f:
        while True:
            line = f.readline().strip()
            
            if len(line)>0:
                row = [ int(r) for r in line]
                
                result.append(row)

            if not line:
                break
    return result

a = np.array(read_array(source))

height, width = a.shape
result = []

for y in range(height):
    for x in range(width):
        s = []
        if x-1 >= 0:
            s.append(a[y][x-1])
        if x+1 < width:
            s.append(a[y][x+1])
        if y-1 >= 0:
            s.append(a[y-1][x])
        if y+1 < height:
            s.append(a[y+1][x])
        n = a[y][x]
        if n < min(s):
            result.append(n)

print(sum([ n + 1 for n in result ]))
