
import os
import PlayerOne as p1
import PlayerTwo as p2

from Defs import *

Board = []

def createBoard():
    for i in range(ROWS):
        NewRow = []
        for j in range(COLS):
            NewRow.append(NONE)
        Board.append(NewRow)

def printColor(color):
    if (color == BLK):
        print('*', end='')
    elif (color == WHI):
        print('0', end='')
    elif (color == NONE):
        print(' ', end='')

def printBoard():
    for i in range(ROWS):
        for j in range(COLS):
            printColor(Board[i][j])
        print()

def initBoard():
    for i in range(ROWS):
        for j in range(COLS):
            Board[i][j] = NONE
    Board[3][3] = BLK
    Board[4][4] = BLK
    Board[3][4] = WHI
    Board[4][3] = WHI

def getBoardColor(pos):
    return Board[pos[0]][pos[1]]

def isValidPosition(pos):
    return pos[0] < ROWS and pos[0] >= 0 and pos[1] < COLS and pos[1] >= 0

def hasEnoughDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) > 1 or abs(pos1[1] - pos2[1]) > 1

def getSameColorPosition(Move, Dline, Dcol):
    pos = (Move[1][0] + Dline, Move[1][1] + Dcol)
    while isValidPosition(pos):
        if (getBoardColor(pos) == Move[0] and hasEnoughDistance(pos, Move[1])):
            return pos
        elif (getBoardColor(pos) == Move[0] and not hasEnoughDistance(pos, Move[1])) or (getBoardColor(pos) == NONE):
            return Move[1]
        pos = (pos[0] + Dline, pos[1] + Dcol)
    return Move[1]

def flip(pos):
    color = Board[pos[0]][pos[1]]
    if (color == BLK):
        color = WHI
    else:
        color = BLK
    Board[pos[0]][pos[1]] = color

def flipFromMovToPosition(Move, pos, Dline, Dcol):
    src = Move[1]
    while src != pos:
        src = (src[0] + Dline, src[1] + Dcol)
        if src != pos:
            flip(src)

def flipForMove(Move):
    flipped = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j and i == 0:
                continue
            pos = getSameColorPosition(Move, i, j)
            flipFromMovToPosition(Move, pos, i, j)
            if (pos != Move[1]):
                flipped = True
    return flipped

def isValidMove(pos, color):
    if getBoardColor(pos) != NONE:
        return False
    Move = (color, pos)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j and i == 0:
                continue
            avail = getSameColorPosition(Move, i, j)
            if (avail != Move[1]):
                return True
    return False

def getAvailableMoves(color):
    AvailMoves = []
    for i in range(ROWS):
        for j in range(COLS):
            if (isValidMove((i, j), color)):
                AvailMoves.append((i, j))
    return AvailMoves


def place(pos, color):
    Move = (color, pos)
    if (flipForMove(Move)):
        Board[pos[0]][pos[1]] = color

def countBoard():
    Count = [0, 0]
    for i in range(ROWS):
        for j in range(COLS):
            if getBoardColor((i, j)) != NONE:
                Count[getBoardColor((i, j))-1] += 1
    return Count

def colorToString(color):
    if color == BLK:
        return "black"
    elif color == WHI:
        return "white"

def printHUD(P1, P2):
    Count = countBoard()
    print("%s(%s): %d" % (P1[0], colorToString(P1[1]), Count[P1[1]-1]))
    print("%s(%s): %d" % (P2[0], colorToString(P2[1]), Count[P2[1]-1]))
    print()
    

if __name__ == "__main__":
    os.system('clear')

    import random as r
    P1Color = r.randint(1, 2)
    P2Color = BLK
    if P1Color == BLK:
        P2Color = WHI

    p2.Color = P2Color

    NoMoves = False
    GameOver = False

    createBoard()
    initBoard()
    printHUD((p1.Name, P1Color), (p2.Name, P2Color))
    printBoard()

    while True:
        for i in range(1, 3):
            input()
            os.system('clear')

            dummyBoard = []
            for j in range(ROWS):
                dummyBoard.append(Board[j][:])

            Avail = getAvailableMoves(i)
            if len(Avail) == 0 and NoMoves:
                GameOver = True
                break
            elif len(Avail) == 0 and not NoMoves:
                NoMoves = True
                continue

            NoMoves = False

            Idx = 0
            if i == P1Color:
                Idx = p1.nextMove(dummyBoard, Avail)
            elif i == P2Color:
                Idx = p2.nextMove(dummyBoard, Avail)
            place(Avail[Idx], i)

            printHUD((p1.Name, P1Color), (p2.Name, P2Color))
            printBoard()

        if GameOver:
            break

    Count = countBoard()

    printBoard()

    print("White pieces: %d" % Count[WHI-1])
    print("Black pieces: %d" % Count[BLK-1])

    Winner = WHI
    if Count[BLK-1] > Count[WHI-1]:
        Winner = BLK
    elif Count[BLK-1] == Count[WHI-1]:
        print("Draw!")

    if P1Color == Winner:
        print("%s win!" % p1.Name)
    else:
        print("%s win!" % p2.Name)

