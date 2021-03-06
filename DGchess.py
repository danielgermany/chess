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
            elif y == 7:
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
            elif y == 6:
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

def draw_ci(cX, cY, size, color, win,circle):
    #circle = boardState[incX][incY]
    circle = Circle(Point(cX, cY), size)
    circle.setFill(color)
    circle.draw(win)
def draw_text(tX,tY,string,color,win):
    message = Text(Point(tX,tY ), string)
    message.setTextColor(color)
    message.draw(win)
def drawFirstSetPeices():
    for x in range (8):
        for y in range (8):
            if 0 <= y <= 1:
                draw_ci (squareSize * (1.5 + x), squareSize * (1.5 + y), pieceSize, color_rgb(255,255,255), chessWin, boardState[x][y])
                draw_text(squareSize * (1.5 + x), squareSize * (1.5 + y),boardState[x][y][1:],"black",chessWin)
            elif 6 <= y <= 8:
                draw_ci (squareSize * (1.5 + x), squareSize * (1.5 + y), pieceSize, color_rgb(0,0,0), chessWin, boardState[x][y])
                draw_text(squareSize * (1.5 + x), squareSize * (1.5 + y),boardState[x][y][1:],"white",chessWin)
def findPos(xPos,yPos):
    for x in range (8):
        if (squareSize * (x+1)) < xPos < (squareSize * (x+2)):
            for y in range(8):
                if (squareSize * (y+1)) < yPos < (squareSize * (y+2)):
                    return boardGrid[x][y]



def checkMouseStatus():
    (mouseX,mouseY) = chessWin.getMouse()
    print("Mouse is over: " + findPos(mouseX,mouseY))
    for x in range (8):
        for y in range(8):
            if boardGrid[x][y] == findPos(mouseX,mouseY):
                if boardState[x][y] != " ":
                    print("The peice residing here is: " + boardState[x][y])
                else:
                    print("There is no peice here")
                return boardState[x][y]
def movePiece(piece,size,sqSize):
    (mouseX,mouseY) = chessWin.getMouse()
    for x in range(8):
        for y in range(8):
            if piece == " ":
                break
            elif piece == boardState[x][y]:
                print(piece,x,y)
                gridPosY = (findPos(mouseX,mouseY))[:1]
                gridPosX = int((findPos(mouseX,mouseY))[1:])
                if gridPosY == "a":
                    gridPosY = 1
                elif gridPosY == "b":
                    gridPosY = 2
                elif gridPosY == "c":
                    gridPosY = 3
                elif gridPosY == "d":
                    gridPosY = 4
                elif gridPosY == "e":
                    gridPosY = 5
                elif gridPosY == "f":
                    gridPosY = 6
                elif gridPosY == "g":
                    gridPosY = 7
                elif gridPosY == "h":
                    gridPosY = 8
                print(gridPosX, " ", gridPosY)
                if piece[:1] == "B":
                    draw_ci (squareSize * (0.5 + gridPosX), squareSize * (0.5 + gridPosY), size, color_rgb(0,0,0), chessWin,boardState[x][y])
                    draw_text(squareSize * (0.5 + gridPosX), squareSize * (0.5 + gridPosY),boardState[x][y][1:],"white",chessWin)
                    print("Printing text")
                elif piece[:1] == "W":
                    draw_ci (squareSize * (0.5 + gridPosX), squareSize * (0.5 + gridPosY), size, color_rgb(255,255,255), chessWin,boardState[x][y])
                    draw_text(squareSize * (0.5 + gridPosX), squareSize * (0.5 + gridPosY),boardState[x][y][1:],"black",chessWin)
                    print("Printing text")

                chessRect = Rectangle(Point(squareSize * (x + 1),squareSize * (y + 1)),Point(squareSize * (x + 2),squareSize * (y + 2)))
                if ((y/2) % 1 == 0):
                    if ((x/2) % 1 == 0) == False:
                        chessRect.setFill(color_rgb(50,205,50))
                    else:
                        chessRect.setFill(color_rgb(245,245,220))
                else:
                    if ((x/2) % 1 == 0):
                        chessRect.setFill(color_rgb(50,205,50))
                    else:
                        chessRect.setFill(color_rgb(245,245,220))
                chessRect.draw(chessWin)

                #boardState[gridPosX - 1][gridPosY - 1] = boardState[x][y]

print("Size of window?(500 recommended)");windowSize = int(input())
squareSize = (windowSize/10)
pieceSize = squareSize - (windowSize/17)

chessWin = GraphWin("Chess", windowSize,windowSize);chessWin.setCoords(0,0, windowSize,windowSize)
drawBoard(squareSize,chessWin)
InitBoardState()
InitBoardGrid()
drawFirstSetPeices()

for x in range (8):
    for y in range (8):
        draw_ci (squareSize * (1.5 + x), squareSize * (1.5 +y), pieceSize, color_rgb(230,50,50), chessWin)

while True:
    movePiece(checkMouseStatus(),pieceSize,squareSize)
