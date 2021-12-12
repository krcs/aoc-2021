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

days = 80

for day in range(0, days):
    eights = 0
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 6
            eights += 1
        else:
            a[i] -= 1

    if eights > 0:
        a=np.append(a, [8] * eights)

print(len(a))
