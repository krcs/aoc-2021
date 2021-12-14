#!/usr/bin/python3
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

def count(l):
    h = dict.fromkeys(set(l),0)
    for c in l:
        h[c] += 1
    return h

def increment_dict(d, e, n):
    if e in d:
        d[e] += n
    else:
        d[e] = n

template, insertions = read_data(source)

steps = 40

result = count(template) 
pc = count([ template[i]+template[i+1] for i in range(len(template)-1) ])

for step in range(steps):
    counts = {}
    for p, v in pc.items():
        increment_dict(counts, p[0]+insertions[p], v)
        increment_dict(counts, insertions[p]+p[1], v)
        increment_dict(result, insertions[p], v)
    pc = counts 

most_common = max(result, key=result.get)
least_common = min(result, key=result.get)
print(result[most_common]-result[least_common])
