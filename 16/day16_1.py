#!/usr/bin/python3
import sys
import numpy as np
from collections import defaultdict

source = "./input.txt"
#source = "./sample7.txt"


def read_data(file):
    with open(file,"r") as f:
            return f.read().strip()
    return result

def find_packets(binary, offset, versions):
    V = int(binary[offset:offset+3],2)
    versions.append(V)
    offset += 3
    T = int(binary[offset:offset+3],2)
    offset += 3
    # literal value
    if T == 4:
        group = ""
        not_last = 1
        while not_last != 0:
            not_last = int(binary[offset])
            offset += 1
            group += binary[offset:offset+4]
            offset += 4
        return offset
    # operator
    else:
        I = int(binary[offset])
        offset += 1
        # 15-bit
        if I == 0:
            L = int(binary[offset:offset+15],2)
            offset += 15
            d = offset
            while offset-d != L:
                offset = find_packets(binary, offset, versions)
            return offset
        # 11-bit
        elif I == 1:
            L = int(binary[offset:offset+11],2)
            offset += 11
            for p in range(L):
                offset = find_packets(binary, offset, versions)
            return offset


number = read_data(source)
binary = "".join([ "{0:04b}".format(int(n,16)) for n in number ])
versions = []

find_packets(binary, 0, versions)

print(sum(versions))
