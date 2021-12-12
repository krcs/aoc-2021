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
    last_win = []
    win_idx = []
    win_num = []
    for n in numbers:
        for bidx in range(len(boards)):
            if bidx in win_idx:
                continue
            set_number(boards[bidx], n)
            if check_board(boards[bidx]):
                win_idx.append(bidx)
                win_num.append(n)
    s = sun_unmarked(boards[win_idx[-1]])
    print(s*win_num[-1])

play(boards,numbers)
