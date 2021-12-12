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
                entry = [ e.split(' ') for e in line.split(' | ') ]
                result.append(entry)

            if not line:
                break
    return result

digits = [ 
  (0, "abcefg"),
  (1, "cf"),
  (2, "acdeg"),
  (3, "acdfg"),
  (4, "bcdf"),
  (5, "abdfg"),
  (6, "abdefg"),
  (7, "acf"),
  (8, "abcdefg"),
  (9, "abcdfg")
]

outputs = [ e[1] for e in read_array(source) ]

uq, counts = np.unique(np.array([ len(d[1]) for d in digits]), return_counts=True)
unique = uq[np.where(counts == 1)]

result = 0
for output in outputs:
    for o in output:
        if len(o) in unique:
            result += 1
print(result)
