from graphics import *

boardGrid = [[" " for x in range(8)]
                   for y in range(8)]
boardState = [[" " for x in range(8)]
               for y in range(8)]
def drawBoard(sZ,window):
    chessBackground = Rectangle(Point(sZ,sZ),Point(sZ * 9,sZ * 9))
    chessBackground.setFill(color_rgb(245,245,220));chessBackground.draw(chessWin)
    for y in range(8):
        for x in range(8):
            chessRect = Rectangle(Point(sZ * (x + 1),sZ * (y + 1)),
                                    Point(sZ * (x + 2),sZ * (y + 2)))
            if ((y/2) % 1 == 0):
                if ((x/2) % 1 == 0) == False: chessRect.setFill(color_rgb(50,205,50))
            else:
                if ((x/2) % 1 == 0): chessRect.setFill(color_rgb(50,205,50))
            chessRect.draw(window)

def InitBoardState():
    for y in range(8):
        for x in range(8):
            if y == 0:
                if x == 0:
                    boardState[x][y] = "WR1"
                elif x == 1:
                    boardState[x][y] = "WN1"
                elif x == 2:
                    boardState[x][y] = "WB1"
                elif x == 3:
                    boardState[x][y] = "WQ"
                elif x == 4:
                    boardState[x][y] = "WK"
                elif x == 5:
                    boardState[x][y] = "WB2"
                elif x == 6:
                    boardState[x][y] = "WN2"
                elif x == 7:
                    boardState[x][y] = "WR2"
            elif y == 1:
                boardState[x][y] = "WP" + str(x + 1)
            elif y == 6:
                if x == 0:
                    boardState[x][y] = "BR1"
                elif x == 1:
                    boardState[x][y] = "BN1"
                elif x == 2:
                    boardState[x][y] = "BB1"
                elif x == 3:
                    boardState[x][y] = "BQ"
                elif x == 4:
                    boardState[x][y] = "BK"
                elif x == 5:
                    boardState[x][y] = "BB2"
                elif x == 6:
                    boardState[x][y] = "BN2"
                elif x == 7:
                    boardState[x][y] = "BR2"
            elif y == 7:
                boardState[x][y] = "BP" + str(x + 1)
            print(boardState[x][y])

def InitBoardGrid():
    for x in range(8):
        for y in range(8):
            if y == 0:
                boardGrid[x][y] = "a" + str(x + 1)
            elif y == 1:
                boardGrid[x][y] = "b" + str(x + 1)
            elif y == 2:
                boardGrid[x][y] = "c" + str(x + 1)
            elif y == 3:
                boardGrid[x][y] = "d" + str(x + 1)
            elif y == 4:
                boardGrid[x][y] = "e" + str(x + 1)
            elif y == 5:
                boardGrid[x][y] = "f" + str(x + 1)
            elif y == 6:
                boardGrid[x][y] = "g" + str(x + 1)
            elif y == 7:
                boardGrid[x][y] = "h" + str(x + 1)
            print(boardGrid[x][y])

def draw_ci(cX, cY, size, color, win):
    circle = Circle(Point(cX, cY), size)
    circle.setFill(color)
    circle.draw(win)

def drawFirstSetPeices():
    for x in range (8):
        for y in range (8):
            if 0 <= y <= 1:
                draw_ci (squareSize * (1.5 + x), squareSize * (1.5 + y), pieceSize, color_rgb(255,255,255), chessWin)
            elif 6 <= y <= 8:
                draw_ci (squareSize * (1.5 + x), squareSize * (1.5 + y), pieceSize, color_rgb(0,0,0), chessWin)

def findPos(xPos,yPos):
    for x in range (8):
        if (squareSize * (x+1)) < xPos < (squareSize * (x+2)):
            for y in range(8):
                if (squareSize * (y+1)) < yPos < (squareSize * (y+2)):
                    return boardGrid[x][y]



def getMouseCoord():
    (mouseX,mouseY) = chessWin.getMouse()
    print("Mouse is over: " + findPos(mouseX,mouseY))
    for x in range (8):
        for y in range(8):
            if boardGrid[x][y] == findPos(mouseX,mouseY):
                if boardState[x][y] != " ":
                    print("The peice residing here is: " + boardState[x][y])
                else:
                    print("There is no peice here")



print("Size of window?(500 recommended)");windowSize = int(input())
squareSize = (windowSize/10)
pieceSize = squareSize - (windowSize/17)
chessWin = GraphWin("Chess", windowSize,windowSize);chessWin.setCoords(0,0, windowSize,windowSize)
q = 0
drawBoard(squareSize,chessWin)
InitBoardState()
InitBoardGrid()
drawFirstSetPeices()

while True:
    getMouseCoord()
