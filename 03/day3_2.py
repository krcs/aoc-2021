#!/usr/bin/python3
table = []

with open("./input.txt","r") as f:
    while True:
        line = f.readline()

        if len(line) > 0:
            table.append(line.strip())
        if not line:
            break

result = []
for element in table:
    bits = [int(d) for d in element]
    result.append(bits)

def calc(rows, idx):
    ones = [ 0 for n in range(len(rows[0]))]
    zeros = [ 0 for n in range(len(rows[0]))]
    
    for row in rows:
        if row[idx] >= 1:
            ones[idx] += 1
        else:
            zeros[idx] += 1
    
    result = []
    
    for row in rows:
        if ones[idx]>=zeros[idx]:
            if row[idx] == 1:
                result.append(row)
        else:
            if row[idx] == 0:
                result.append(row)
    return result

nbit = len(result[0])

r = result
for n in range(nbit):
    if len(r) == 1:
        break
    r = calc(r, n)

oxygen = int("".join([str(n) for n in r[0]]),2)

def calc_co(rows, idx):
    ones = [ 0 for n in range(len(rows[0]))]
    zeros = [ 0 for n in range(len(rows[0]))]
    
    for row in rows:
        if row[idx] >= 1:
            ones[idx] += 1
        else:
            zeros[idx] += 1
    
    result = []
    
    for row in rows:
        if ones[idx]>=zeros[idx]:
            if row[idx] == 0:
                result.append(row)
        else:
            if row[idx] == 1:
                result.append(row)
    return result

r = result

for n in range(nbit):
    if len(r) == 1:
        break
    r = calc_co(r, n)

co = int("".join([str(n) for n in r[0]]),2)
print(oxygen*co)
