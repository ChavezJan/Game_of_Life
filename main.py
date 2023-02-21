"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
from tools.conway import *
from tools.fileManager import *
from assets.coordinates import *
from assets.bord import *



def main()-> None:
    maxX = 0
    maxY = 0
    fps = 0
    coordinates = []

    maxX, maxY, fps, coordinates = fileReader(maxX,maxY,fps,coordinates)

    board = Board(maxX,maxY, fps)

    board.aliveValues = coordinates

    x = input()

    board.draw()

    
# call main
if __name__ == '__main__':
    main()

