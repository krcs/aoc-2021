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

result = []
for line in lines:
    stack = []
    isError = False
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
                isError = True
                break
    if isError:
        continue
    closing_stack = []
    for s in reversed(stack):
        for p in pairs:
            if p[0]==s:
                closing_stack.append(p[1])
    result.append(closing_stack)

score = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }

totals = []
for r in result:
    line_score = 0
    for c in r:
        line_score *= 5
        line_score += score[c]
    totals.append(line_score)

print(int(np.median(totals)))
