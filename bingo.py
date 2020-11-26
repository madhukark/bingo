#!/usr/bin/python3

from random import randrange
from random import sample

bingo = []

# Min and Max in each column
col = [
    [1, 9], [10, 19], [20, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89],
    [1, 9], [10, 19], [20, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89],
    [1, 9], [10, 19], [20, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89],
]

# Randon number generator given a Min, Max
def myRand(min, max):
    n = randrange(min, max)
    return n

# Remove duplicates in a column
def removeDups(bingo):
    row = []
    for c in range(27):
        row = [bingo[0][c], bingo[1][c], bingo[2][c]]

        if (row[0] == row[1] and row[0] != 0):
            bingo[0][c] = myRand(col[c][0], col[c][1])

        if (row[1] == row[2] and row[1] != 0):
            bingo[1][c] = myRand(col[c][0], col[c][1])

        if (row[0] == row[2] and row[0] != 0):
            bingo[0][c] = myRand(col[c][0], col[c][1])

    return bingo

# Generate Bingo in the required format (3 sets of Bingo numbers)
def genBingo():
    bingo = [
        [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0],
    ]

    for r in [0, 1, 2]:
        # Set 1
        list = sample([0,1,2,3,4,5,6,7,8], k = 5)
        for c in list:
            n = myRand(col[c][0], col[c][1])
            bingo[r][c] = n

        # Set 2 
        list = sample([9,10,11,12,13,14,15,16,17], k = 5)
        for c in list:
            n = myRand(col[c][0], col[c][1])
            bingo[r][c] = n

        # Set 3 
        list = sample([18,19,20,21,22,23,24,25,26], k = 5)
        for c in list:
            n = myRand(col[c][0], col[c][1])
            bingo[r][c] = n

    # Magic num 5
    for i in range(5):
        bingo = removeDups(bingo)

    return bingo

# Pretty print Bingo numbers
def printBingo(bingo):
    for r in [0, 1, 2]:
        for c in range(27):
            if (c in [9, 18]):
                print ('|', end='')
            if (bingo[r][c] == 0):
                print('    ', end='')
            else:
                print(f' {bingo[r][c]:2d} ', end='')
        print ('')
    print('')


# Main
sets = 14*2 # A4 size, font = 9, min margin 
for i in range(sets):
    printBingo(genBingo())
    print('')
