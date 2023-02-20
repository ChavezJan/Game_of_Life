
#from tools.conway import *
from tools.fileManager import *

class coordinate:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def main()-> None:
    maxX = 0
    maxY = 0
    fps = 0
    coordinates = []

    maxX, maxY, fps, coordinates =fileReader(maxX,maxY,fps,coordinates)


# call main
if __name__ == '__main__':
    main()

