"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
from tools.conway import *
from tools.fileManager import *
from assets.coordinates import *
from assets.bord import *
from tools.outputManager import *



def main()-> None:

    
    maxX = 0
    maxY = 0
    fps = 0
    coordinates = []
    

    maxX, maxY, fps, coordinates = fileReader(maxX,maxY,fps,coordinates)
    output(maxX,maxY)

    board = Board(maxX,maxY, fps)

    board.aliveValues = coordinates
    print(board.countCells)

    print("Enter the sleep time")
    try:
        sleepTime = float(input())
    except:
        sleepTime = 1.0

    board.draw(sleepTime)

    
# call main
if __name__ == '__main__':
    main()