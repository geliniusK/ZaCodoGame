#! /bin/python

Name = "Jose"

def nextMove(Board, Avail):
    import random as r
    return r.randint(0, len(Avail)-1)
