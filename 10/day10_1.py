#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./test.txt"

def read_lines(file):
    result = []
    with open(file,"r") as f:
        while True:
            line = f.readline().strip()
            
            if len(line)>0:
                result.append([ e for e in line ])

            if not line:
                break
    return result

lines = np.array(read_lines(source))

pairs = ( ('<','>' ), ('[',']' ), ('{','}' ), ('(',')' ) )

stack = []

score = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }

errors = []
for line in lines:
    for c in line:
        op = None
        cp = None
        for o in pairs:
            if o[0] == c:
                op = o
                break
            if o[1] == c:
                cp = o
                break

        if op != None:
            stack.append(c[0])
            continue

        if cp != None:
            if len(stack) == 0:
                break
            if stack[-1] == cp[0]:
                stack.pop()
            else:
                errors.append(c)
                break


print(sum([ score[e] for e in errors ]))
