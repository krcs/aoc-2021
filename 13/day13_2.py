#!/usr/bin/python3
import numpy as np
import re

source = "./input.txt"
#source = "./test.txt"

def read_data(file):
    result = []
    with open(file,"r") as f:
            lines = f.readlines()
    positions = []
    folds = []
    isFolds = False

    for line in lines:
        ls = line.strip()

        if len(ls) == 0:
            isFolds = True

        if not isFolds:
           positions.append([ int(n) for n in ls.split(',') ])
        else:
            r = re.findall("[xy]=\d+", line)
            if r:
                fold = r[0].split('=')
                folds.append( [ fold[0], int(fold[1]) ] )

    return [ positions, folds ]

positions, folds = read_data(source)

width = max([ pos[0] for pos in positions ]) + 1
height = max([ pos[1] for pos in positions ]) + 1

paper = np.zeros((height, width) , dtype=np.int32)

for pos in positions:
    paper[pos[1], pos[0]] = 1

for fold in folds:
    if fold[0] == 'y':
        f = fold[1]
        top = paper[:f,]
        f += 1
        bottom = paper[f:,]
        bottom = np.flipud(bottom)
        paper = top + bottom
    if fold[0] == 'x':
        f = fold[1]
        left = paper[:,:f]
        f += 1
        right = paper[:,f:]
        right = np.fliplr(right)
        paper = left + right

for y in range(len(paper)):
    for x in range(len(paper[y])):
          print('$' if paper[y][x] > 0 else ' ', end='')
    print()
