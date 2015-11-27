
import os

ROWI = 0
COLI = 1

ROWS = 8
COLS = 8

NONE = 0
WHI  = 1
BLK  = 2

Board = []

class Move:
    def init(self, color):
        self.pos   = (0,0)
        self.color = color 

def createBoard():
    for i in range(ROWS):
        NewRow = []
        for j in range(COLS):
            NewRow.append(NONE)
        Board.append(NewRow)
            
def initBoard():
    for i in range(ROWS):
        for j in range(COLS):
            Board[i][j] = NONE
    Board[3][3] = BLK
    Board[4][4] = BLK
    Board[3][4] = WHI
    Board[4][3] = WHI

def verifyMove(Mov):
    return True

def verifyVertical(Mov):
    pos   = Mov.pos
    color = Mov.color
    for i in range(ROWS):
        if (Board[i][col] == color and 
