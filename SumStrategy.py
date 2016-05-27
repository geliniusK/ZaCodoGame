#! /bin/python

from Defs import *

import math

Name = "Sum"
Color = 0

def nextMove(Board, Avail):
    SumSet = []
    Count = 0
    for Pos in Avail:
        SumSet.append((Pos[0] + Pos[1], Count))
        Count += 1
    SumSet.sort()
    return SumSet[math.floor(len(SumSet)/2)][1]

