#! /bin/python

from Defs import *

Name = "WeightRoullete"

def criticalLine(Pos):
    return Pos[0] < 2 or Pos[0] >= ROWS-2

def criticalColumn(Pos):
    return Pos[1] < 2 or Pos[1] >= COLS-2

def isUpCorner(Pos):
    return Pos[0] == 0 and (Pos[1] == 0 or Pos[1] == COLS-1)

def isDownCorner(Pos):
    return Pos[0] == ROWS-1 and (Pos[1] == 0 or Pos[1] == COLS-1)

def nextMove(Board, Avail):
    import random as r

    Ranking = []
    for Pos in Avail:
        Score = 0
        if criticalLine(Pos):
            Score += 20
        if criticalColumn(Pos):
            Score += 20
        if criticalColumn(Pos) and criticalLine(Pos):
            Score += 10
        if isUpCorner(Pos) or isDownCorner(Pos):
            Score -= 100
        Ranking.append(Score)

    for i in range(len(Ranking)):
        Ranking[i] = -1 * Ranking[i]

    Offset = abs(min(Ranking))
    for i in range(len(Ranking)):
        Ranking[i] += Offset + 1

    Sum = sum(Ranking)
    Dice = r.randint(1, Sum)
    for i in range(len(Ranking)):
        Dice -= Ranking[i]
        if Dice == 0:
            return i

    return r.randint(0, len(Avail)-1)

