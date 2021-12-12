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
median = np.median(a)
result = np.sum(np.abs(a-median), dtype=int)

print(result)
