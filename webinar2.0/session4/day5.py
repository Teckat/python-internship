# Creating tic tac toe game

# create a board
# assign cross and zero for players
# play functon
# get user rows and column data
# place function
# check function -> row function, col function, diag function

import numpy as np


board = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])
# print(board)

p1 = 'x'
p2 = 'o'


def place(sym):

    while(1):
        print(board)
        r = int(input('enter 1 2 3 for row'))
        c = int(input('enter 1 2 3 for column'))

        if (r > 0 and r < 4 and c > 0 and c < 4 and board[r-1][c-1] == '_'):
            break
        else:
            print('invalid choice, enter again')
    board[r-1][c-1] = sym


def row(sym):
    for i in range(3):
        c = 0
        for j in range(3):
            if(board[i][j] == sym):
                c += 1
        if(c == 3):
            return True


def col(sym):

    for i in range(3):
        c = 0
        for j in range(3):
            if(board[j][i] == sym):
                c += 1
        if(c == 3):
            return True


def diag(sym):

    for i in range(3):
        c = 0
        d = 0
        for j in range(3):
            if(i == j):
                if(board[i][j] == sym):
                    c += 1
                elif(i+j == 2):
                    if(board[i][j] == sym):
                        d += 1
        if(c == 3):
            return True
        if(d == 3):
            return True


def check(sym):
    if(row(sym) or col(sym) or diag(sym)):
        return True


def play():
    for i in range(9):

        if(i % 2 == 0):
            print("x's turn")
            place(p1)
            if(check(p1)):
                print('x won')
                break

        else:
            print("o's turn")
            place(p2)
            if(check(p2)):
                print('o won')
                break

    if not(check(p1) and not(check(p2))):
        print('draw')


play()
