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
                result = [ int(n) for n in line.split(',')]
                break
    return result

a = np.array(read_array(source))
c = np.zeros(9, dtype=int)

for n in a:
    c[n] += 1

result = np.sum(c)

for d in range(256):
    c = np.roll(c, -1)
    if c[-1] > 0:
        c[6] += c[-1]
    result = np.sum(c)

print(result)
