#!/usr/bin/python3
import re

numbers = []
boards = []

with open("./input.txt","r") as f:
    numbers = [ int(n.strip()) for n in f.readline().split(",") ]
    f.readline()

    board = []
    while True:
        line = f.readline()
        if not line:
            break

        line  = line.strip()
        if len(line) == 0:
            boards.append(board)
            board=[]
        else:
            row = [ [ int(n), False ]  for n in re.split("\s+",line.strip()) ]
            board.append(row)

    boards.append(board)

def get_rounds(numbers, col_count):
    rcount = len(numbers) // col_count
    rounds = []
    row = []
    for idx in range(len(numbers)):
        row.append(numbers[idx])

        if idx % 5 == 4:
            
            rounds.append(row)
            row=[]
    rounds.append(row)
    return rounds

def set_number(board, number):
    for row in board:
        for col in row:
            if col[0] == number:
               col[1] = True

def check_board(b): 
    
    for row in b:
        test = all([ col[1] for col in row ])
        if test:
            return True

    for cidx in range(len(b[0])):
        test = all([ row[cidx][1] for row in b ])
        if test:
            return True
    return False

def printb(board):
    for row in board:
        print(row)
    print()

def sun_unmarked(board): 
    return sum([ col[0] for row in board for col in row if not col[1]])

def play(boards, numbers):
    for n in numbers:
        for b in boards:
            set_number(b, n)
            if check_board(b):
                return [b, n]

n = play(boards, numbers)
s = sun_unmarked(n[0])

print(s*n[1])
