#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./sample1.txt"
#source = "./sample2.txt"
#source = "./sample3.txt"

def read_lines(file):
    result = []
    with open(file,"r") as f:
        while True:
            line = f.readline().strip()
            
            if len(line)>0:

                result.append(line.split('-'))

            if not line:
                break
    return result

def create_path(path, links, result):
    for link in links:
        if path[-1] == link[0]:

            if link[1] != 'end' and link[1].islower():
                if link[1] in path[1:]:
                    continue

            if link[1] == 'end':
                path.append(link[1])
                result.append(path)
                return

            l = links.copy()
            l.remove(link)

            create_path(path + [ link[1] ], l, result)

nodes = read_lines(source)

starts = []
links = []
ends = []

for node in nodes:
    if 'start' in node[0]:
        starts.append([ node[0], node[1]])
    elif 'start' in node[1]:
        starts.append([ node[1], node[0]])
    elif 'end' in node[0]:
        ends.append([ node[1], node[0] ])
    elif 'end' in node[1]:
        ends.append([ node[0], node[1] ])
    else:
        links.append(node)
        links.append([node[1], node[0]])

links += ends
result = []

for start in starts:
    create_path(start,links.copy(), result)

print(len(result))
