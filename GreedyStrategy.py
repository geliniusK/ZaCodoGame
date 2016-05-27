#! /bin/python

from Defs import *

Name = "Greedy"
Color = 0

def hasDistance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) > 1 or abs(Pos1[1] - Pos2[1]) > 1

def isValidPosition(Pos):
    return Pos[0] >= 0 and Pos[0] < ROWS and Pos[1] >= 0 and Pos[1] < COLS

def getNumberOfFlips(Board, Pos, Dline, Dcol):
    Count = 0
    Next = (Pos[0] + Dline, Pos[1] + Dcol)
    while isValidPosition(Next) and Board[Next[0]][Next[1]] != Color:
        if (Board[Next[0]][Next[1]] == NONE):
            return 0
        Next = (Next[0] + Dline, Next[1] + Dcol)
        Count += 1
    if hasDistance(Next, Pos):
        return Count
    return 0

def nextMove(Board, Avail):

    Ranking = []
    for Pos in Avail:
        Count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j and i == 0:
                    continue
                Count += getNumberOfFlips(Board, Pos, i, j)
        Ranking.append(Count)

    Max = max(Ranking)
    return Ranking.index(Max)


