from tetris import *
from random import *
import threading

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def rotate(m_array):
    size = len(m_array)
    r_array = [[0] * size for _ in range(size)]

    for y in range(size):
        for x in range(size):
            r_array[x][size-1-y] = m_array[y][x]

    return r_array

def initSetOfBlockArrays():
    arrayBlks = [  [ [ 0, 0, 1, 0 ],     # ㅁ
                    [ 0, 0, 1, 0 ],     # ㅁ
                    [ 0, 0, 1, 0 ],     # ㅁ
                    [ 0, 0, 1, 0 ] ],   # ㅁ
                  [ [0, 1, 0],              
                    [1, 1, 1],          # ㅗ
                    [0, 0, 0] ],
                  [ [1, 0, 0],
                    [1, 1, 1],          # ㄴ
                    [0, 0, 0] ],
                  [ [0, 0, 1],          #    ㅁ
                    [1, 1, 1],          # ㅁㅁㅁ 
                    [0, 0, 0] ],        #
                  [ [1, 1],             # ㅁ
                    [1, 1] ],           
                  [ [0, 1, 1],          #   ㅁㅁ
                    [1, 1, 0],          # ㅁㅁ 
                    [0, 0, 0] ],        #
                  [ [1, 1, 0],          # ㅁㅁ
                    [0, 1, 1],          #   ㅁㅁ
                    [0, 0, 0] ]         #
                ]

    nBlocks = len(arrayBlks)
    setOfBlockArrays = [[0] * 4 for _ in range(nBlocks)]

    for idxBlockType in range(nBlocks):
        temp_array = arrayBlks[idxBlockType]
        setOfBlockArrays[idxBlockType][0] = temp_array
        for idxBlockDegree in range(1,4):
            temp_array = rotate(temp_array)
            setOfBlockArrays[idxBlockType][idxBlockDegree] = temp_array

    return setOfBlockArrays
    
if __name__ == "__main__":
    #LED_init()
    setOfBlockArrays = initSetOfBlockArrays()

    Tetris.init(setOfBlockArrays)
    board = Tetris(32, 16)

    idxBlockType = randint(0, 6)
    key = '0' + str(idxBlockType)
    board.accept(key)
    board.printScreen()
      
    while True:
        key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
        
        if key != 'q':
          state = board.accept(key)
          board.printScreen()
          
          if state == TetrisState.NewBlock:
              idxBlockType = randint(0, 6)
              key = '0' + str(idxBlockType)
              state = board.accept(key)
              if state == TetrisState.Finished:
                  board.printScreen()
                  print('Game Over!!!')
                  break
              board.printScreen()
        else:
          print('Game aborted...')
          break
    
    print('Program terminated...')

### end of pytet.py
