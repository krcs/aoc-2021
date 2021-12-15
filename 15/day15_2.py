#!/usr/bin/python3
import sys
import numpy as np
from collections import defaultdict

source = "./input.txt"
#source = "./test.txt"
#source = "./sample.txt"


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

def generate_graph(a):
    height, width = a.shape
    
    d = defaultdict()
    
    for y in range(height):
        for x in range(width):
            v = y*height+x
            d[v] = {}
            if x-1 >= 0:
                vl = y*height+(x-1)
                d[v][vl] = a[y][x-1]
            if x+1 < width:
                vr = y*height+(x+1)
                d[v][vr] = a[y][x+1]
            if y-1 >= 0:
                vt = (y-1)*height+x
                d[v][vt] = a[y-1][x]
            if y+1 < height:
                vb = (y+1)*height+x
                d[v][vb] = a[y+1][x]
    return d


def arr_add_one(a, n):
    result = a + n
    height, width = result.shape
    for y in range(height):
        for x in range(width):
            if result[y][x] >= 10:
                result[y][x] = result[y][x] - 9
    return result

a = np.array(read_data(source))

ay = a
for i in range(1,5):
    ay = np.concatenate((ay, arr_add_one(a, i)), axis=0)

ax = ay
for i in range(1,5):
    ax = np.concatenate((ax, arr_add_one(ay, i)), axis=1)

a = ax

graph = generate_graph(a)

unvisited = dict.fromkeys(graph.keys(), sys.maxsize)
visited = {}
current = 0
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in graph[current].items():
        if neighbour not in unvisited: 
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: 
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited[a.size-1])
