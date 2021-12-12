#!/usr/bin/python3
table = []

with open("./input.txt","r") as f:
    while True:
        line = f.readline()

        if len(line) > 0:
            table.append(line.strip())
        if not line:
            break

gamma_ones = []
gamma_zeros = []
for element in table:
    bits = [int(d) for d in element]

    if len(gamma_ones) == 0:
        gamma_ones=[ 0 for n in range(len(bits))]
   
    if len(gamma_zeros) == 0:
        gamma_zeros=[ 0 for n in range(len(bits))]
 
    for idx in range(len(bits)):
        if bits[idx] == 1:
            gamma_ones[idx] += 1
        elif bits[idx] == 0:
            gamma_zeros[idx] += 1

gamma_bit = ""
epsilon_bit = ""

for idx in range(len(gamma_ones)):
    if gamma_ones[idx] > gamma_zeros[idx]:
        gamma_bit += "1"
        epsilon_bit += "0"
    else:
        gamma_bit += "0"
        epsilon_bit += "1"

gamma = int(gamma_bit,2)
epsilon = int(epsilon_bit,2)
print(gamma*epsilon)

