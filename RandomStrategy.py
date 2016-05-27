#! /bin/python

from Defs import *

Name = "Randomic"
Color = 0

def nextMove(Board, Avail):
    import random as r
    return r.randint(0, len(Avail)-1)

