#!/usr/bin/python3
import numpy as np

#source = "./input.txt"
source = "./test.txt"

def read_data(file):
    result = []
    with open(file,"r") as f:
            lines = f.readlines()

    result = []

    for line in lines:
        ls = line.strip()

        if len(ls) == 0:
            continue

        result.append([ int(n) for n in ls ])

    return result

shape = np.array(read_data(source))

print(shape)


