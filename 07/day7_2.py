#!/usr/bin/python3
import math
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

mean = np.mean(a)
mf = math.floor(mean)
mc = math.ceil(mean)

abs_mf = np.abs(a-mf)
abs_mc = np.abs(a-mc)

result = min( sum([ np.arange(1,e+1).sum() for e in abs_mf ]),
              sum([ np.arange(1,e+1).sum() for e in abs_mc ]))

print(result)
