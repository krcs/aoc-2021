#!/usr/bin/python3
import numpy as np

source = "./input.txt"
sample1 = "C200B40A82"
sample2 = "04005AC33890"
sample3 = "880086C3E88112"
sample4 = "CE00C43D881120"
sample5 = "D8005AC2A8F0"
sample6 = "F600BC2D8F"
sample7 = "9C005AC2F8F0"
sample8 = "9C0141080250320F1802104A08"

def read_data(file):
    with open(file,"r") as f:
            return f.read().strip()
    return result

def find_packets(binary, offset):
    V = int(binary[offset:offset+3],2)
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
        value = int(group,2)
        return [ offset, value ]
    # operator
    else:
        I = int(binary[offset])
        offset += 1
        values = []
        # 15-bit
        if I == 0:
            L = int(binary[offset:offset+15],2)
            offset += 15
            d = offset
            while offset-d != L:
                offset, value = find_packets(binary, offset)
                values.append(value)
        # 11-bit
        elif I == 1:
            L = int(binary[offset:offset+11],2)
            offset += 11
            for p in range(L):
                offset, value = find_packets(binary, offset)
                values.append(value)
        if T == 0:
            value = sum(values)
        elif T == 1:
            value = np.prod(values)
        elif T == 2:
            value  = min(values)
        elif T == 3:
            value = max(values)
        elif T == 5:
            value = 1 if values[0] > values[1] else 0
        elif T == 6:
            value = 1 if values[0] < values[1] else 0
        elif T == 7:
            value = 1 if values[0] == values[1] else 0
        return [ offset, value ]

number = read_data(source)

binary = "".join([ "{0:04b}".format(int(n,16)) for n in number ])

offset, value = find_packets(binary, 0)
print(value)
