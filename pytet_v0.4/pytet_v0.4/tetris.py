from matrix import *
from random import *
from enum import Enum
#import LED_display as LMD 

class TextColor():
    red    = "\033[31m"
    green  = "\033[32m"
    yellow = "\033[33m"
    blue   = "\033[34m"
    purple = "\033[35m"
    cyan   = "\033[36m"
    white  = "\033[37m"
    pink   = "\033[95m"
### end of class TextColor():

class TetrisState(Enum):
    Running = 0
    NewBlock = 1
    Finished = 2
### end of class TetrisState():

class Tetris():
    nBlockTypes = 0
    nBlockDegrees = 0
    setOfBlockObjects = 0
    iScreenDw = 0   # larget enough to cover the largest block

    def __init__(self, iScreenDy, iScreenDx):
        self.iScreenDy = iScreenDy
        self.iScreenDx = iScreenDx
        self.idxBlockType = -1
        self.idxBlockDegree = 0
        arrayScreen = self.createArrayScreen()
        self.iScreen = Matrix(arrayScreen)
        self.oScreen = Matrix(self.iScreen)
        self.justStarted = True
        return

    @classmethod
    def init(cls, setOfBlockArrays):
        Tetris.nBlockTypes = len(setOfBlockArrays)
        Tetris.nBlockDegrees = len(setOfBlockArrays[0])
        Tetris.setOfBlockObjects = [[0] * Tetris.nBlockDegrees for _ in range(Tetris.nBlockTypes)]
        arrayBlk_maxSize = 0
        for i in range(Tetris.nBlockTypes):
            if arrayBlk_maxSize <= len(setOfBlockArrays[i][0]):
                arrayBlk_maxSize = len(setOfBlockArrays[i][0])
        Tetris.iScreenDw = arrayBlk_maxSize     # larget enough to cover the largest block

        for i in range(Tetris.nBlockTypes):
            for j in range(Tetris.nBlockDegrees):
                mat = Matrix(setOfBlockArrays[i][j])
                mat.mulc(i+1)
                Tetris.setOfBlockObjects[i][j] = mat
        return

    def createArrayScreen(self):
        self.arrayScreenDx = Tetris.iScreenDw * 2 + self.iScreenDx
        self.arrayScreenDy = self.iScreenDy + Tetris.iScreenDw
        self.arrayScreen = [[0] * self.arrayScreenDx for _ in range(self.arrayScreenDy)]
        for y in range(self.iScreenDy):
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][x] = 1
            for x in range(self.iScreenDx):
                self.arrayScreen[y][Tetris.iScreenDw + x] = 0
            for x in range(Tetris.iScreenDw):
                self.arrayScreen[y][Tetris.iScreenDw + self.iScreenDx + x] = 1

        for y in range(Tetris.iScreenDw):
            for x in range(self.arrayScreenDx):
                self.arrayScreen[self.iScreenDy + y][x] = 1

        return self.arrayScreen

    def accept(self, key):
        self.state = TetrisState.NewBlock

        self.top = 0
        self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
        self.idxBlockType = (1 + self.idxBlockType) % Tetris.nBlockTypes
        self.idxBlockDegree = 0
        self.currBlk = Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree]
        self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
        self.tbinBlk = self.tempBlk.binary() + self.currBlk.binary()
        self.tempBlk = self.tempBlk + self.currBlk
        print()

        self.oScreen = Matrix(self.iScreen)
        self.oScreen.paste(self.tempBlk, self.top, self.left)

        return self.state

    def printScreen(self):
        array = self.oScreen.get_array()

        for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
            for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
                if array[y][x] == 0:
#                    LMD.set_pixel(y, 19-x, 0)
                    print(TextColor().white + "□", end='')
                elif array[y][x] == 1:
#                    LMD.set_pixel(y, 19-x, 1)
                    print(TextColor().white + "■", end='')
                elif array[y][x] == 2:
#                    LMD.set_pixel(y, 19-x, 2)
                    print(TextColor().pink + "■", end='')
                elif array[y][x] == 3:
#                    LMD.set_pixel(y, 19-x, 3)
                    print(TextColor().red + "■", end='')
                elif array[y][x] == 4:
#                    LMD.set_pixel(y, 19-x, 4)
                    print(TextColor().green + "■", end='')
                elif array[y][x] == 5:
#                    LMD.set_pixel(y, 19-x, 5)
                    print(TextColor().yellow + "■", end='')
                elif array[y][x] == 6:
#                    LMD.set_pixel(y, 19-x, 6)
                    print(TextColor().blue + "■", end='')
                elif array[y][x] == 7:
#                    LMD.set_pixel(y, 19-x, 7)
                    print(TextColor().cyan + "■", end='')
                elif array[y][x] == 8:
#                    LMD.set_pixel(y, 19-x, 2)
                    print(TextColor().purple + "■", end='')
                else:
                    print("XX", end='')
            print()

    def deleteFullLines(self):
        return

### end of class Tetris():
    
