#!/usr/bin/python3
import numpy as np

source = "./input.txt"
#source = "./test.txt"

class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def is_horizontal_to_point(self, point):
        return self.x == point.x

    def is_vertical_to_point(self, point):
        return self.y == point.y


def read_lines(file):
    lines = []
    with open(file,"r") as f:
        while True:
            line = f.readline().strip()
            
            if len(line)>0:
                sline = line.split(' -> ')
                p0 = [ int(p) for p in  sline[0].split(',')]
                p1 = [ int(p) for p in  sline[1].split(',')]
                lines.append([Point(p0[0], p0[1]), Point(p1[0], p1[1])])
    
            if not line:
                break
    return lines

def print_lines(points):
    for point in points:
        print("{0} -> {1}".format(point[0], point[1]))

def only_horizontal_and_vertical(lines):
    result = []
    for line in lines:
        if line[0].is_horizontal_to_point(line[1]) or line[0].is_vertical_to_point(line[1]):
            result.append(line)
    return result

def find_max_xy(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if max_x < line[0].x:
            max_x = line[0].x
        if max_x < line[1].x:
            max_x = line[1].x

        if max_y < line[0].y:
            max_y = line[0].y
        if max_y < line[1].y:
            max_y = line[1].y
    return [max_y, max_y]

def draw_line(table, line):
    if line[0].is_horizontal_to_point(line[1]) or line[0].is_vertical_to_point(line[1]):
        px = sorted([line[0].x, line[1].x])
        py = sorted([line[0].y, line[1].y])
        for x in range(px[0], px[1]+1):
            for y in range(py[0], py[1]+1):
                table[y,x] += 1
    else:
        dx = 1 if line[0].x < line[1].x else -1
        dy = 1 if line[0].y < line[1].y else -1

        y = line[0].y
        for x in range(line[0].x, line[1].x+dx, dx):
            table[y,x] += 1
            y+=dy

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=

lines = read_lines(source)
size = [ n + 1 for n in find_max_xy(lines)]

table = np.zeros((size[0],size[1]), dtype='int32')

for line in lines:
    draw_line(table, line)

count_go = 0

for row in table:
    for value in row:
        if value > 1:
            count_go+=1
print(count_go)
