#!/usr/bin/python3
import re

#source = "./input.txt"
source = "./test.txt"

def read_data(file):
    with open(file,"r") as f:
            line = f.read().strip()
            area = re.findall("[xy]=-?\d+[.]{2}-?\d+",line)


target_area = read_data(source)
print(target_area)
