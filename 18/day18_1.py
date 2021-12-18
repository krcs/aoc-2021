#!/usr/bin/python3
import re
source = "./input.txt"
#source = "./test.txt"

def read_data(file):
    result = []
    with open(file,"r") as f:
            while True:
                line = f.readline().strip()

                if len(line)>0:
                    result.append(line)
                
                if not line:
                    break
    return result

lines = read_data(source)
print(lines)
