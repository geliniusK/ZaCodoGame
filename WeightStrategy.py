#! /bin/python

from Defs import *

Name = "Weight"

def criticalLine(Pos):
    return Pos[0] < 2 or Pos[0] >= ROWS-2

def criticalColumn(Pos):
    return Pos[1] < 2 or Pos[1] >= COLS-2

def isUpCorner(Pos):
    return Pos[0] == 0 and (Pos[1] == 0 or Pos[1] == COLS-1)

def isDownCorner(Pos):
    return Pos[0] == ROWS-1 and (Pos[1] == 0 or Pos[1] == COLS-1)

def nextMove(Board, Avail):

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

    Min = min(Ranking)
    return Ranking.index(Min)
