#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./test.txt"

def read_data(file):
    result = []
    with open(file,"r") as f:
            lines = f.readlines()

    template = []
    insertions = {}
    nextSection  = False

    for line in lines:
        ls = line.strip()

        if len(ls) == 0:
            nextSection = True
            continue

        if not nextSection:
            template = [ c for c in ls ]
        else:
            pair = ls.split(' -> ')
            insertions[pair[0]] = pair[1]

    return [ template, insertions ]

template, insertions = read_data(source)

steps = 10

for step in range(steps):
    i = 0
    j = i+1

    while (i < len(template)-1):
        pair = template[i]+template[j]
        if pair in insertions:
            c = insertions[pair]
            template.insert(i+1,c)
            i+=2
            j+=2
        else:
            i+=1
            j+=1

h = dict.fromkeys(set(template),0)
for c in template:
    h[c] += 1

most_common = max(h, key=h.get)
least_common = min(h, key=h.get)
print(h[most_common]-h[least_common])
