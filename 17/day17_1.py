#!/usr/bin/python3
import re
source = "./input.txt"
#source = "./test.txt"

def read_data(file):
    result = { 'x' : [], 'y' : [] }
    with open(file,"r") as f:
            line = f.read().strip()
            area = re.findall("[xy]=-?\d+[.]{2}-?\d+",line)
            for a in area:
                result[a[0]] = list(map(lambda n: int(n),a[2:].split("..")))
    return result

target_area = read_data(source)
y = target_area['y'][0]*-1-1
result = y*(y+1)/2
print(int(result))
