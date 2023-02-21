"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import os
import numpy as np
from copy import deepcopy
import time
# from GoL.Config.rules import *



class Board():
        
    def __init__(self, width, height, fps):
        self._width = width+1
        self._height = height+1
        self._boardNP = np.zeros((self._height+1,self._width+1), dtype=int)
        self._aliveValues = []
        self._cellOn = 0
        self._fps = fps

    def __str__(self) -> str:
        return str(self._boardNP)

    """
        it count the alive values 
    """
    def countValues(self):
        count = 0
        for i in self._aliveValues:
            count += 1

        return count

    """
        Getter for the size of the borad (x, y)
    """
    @property
    def boardSize(self):
        size = "Size: "
        size += str(self._width) + " " + str(self._height)
        return size
    """
        Getter for the list of coordinates that still alaive
    """
    @property
    def aliveValues(self):
        return self._aliveValues                           #return all the positions
        #return "Values Alive: %05d" % self.countValues()    #return the count of the values

    """
        Setter for the coordinates that are alive
    """
    @aliveValues.setter
    def aliveValues(self,values):
        for i in values:            
            self._aliveValues.append(i.position)
        self.setValuesOnBoard()


    """
        its sets all the coordinates on board
    """
    def setValuesOnBoard(self):
        for i in self.aliveValues:
            self._boardNP[i[0]+1, i[1]+1] = 1
            self._cellOn += 1
        print(self._boardNP)
        print("\n")


    """
        Check rules
    """
    def liveOn(self, cell):
        on = len(np.array(self.sub[cell[0]][cell[1]].nonzero()).transpose())
        # print(on)
        if(self._boardNP[cell[0]+1, cell[1]+1] == 1):
            on -= 1
        if(self._boardNP[cell[0]+1, cell[1]+1] == 1 and (on == 2 or on == 3)):
            return True
        elif(self._boardNP[cell[0]+1, cell[1]+1] == 1 and (on == 3)):
            return True
        elif(self._boardNP[cell[0]+1, cell[1]+1] == 1 and (on < 2)):
            return False
        elif(self._boardNP[cell[0]+1, cell[1]+1] == 1 and (on > 3)):
            return False
        elif(self._boardNP[cell[0]+1, cell[1]+1] == 0 and (on == 3)):
            return True
        else:
            return False

    def update(self):
        view = tuple(np.subtract(self._boardNP.shape, (3,3)) + 1)+(3,3) 
        stride= self._boardNP.strides + self._boardNP.strides
        self.sub = np.lib.stride_tricks.as_strided(self._boardNP, view,stride)

        boardState = deepcopy(self._boardNP)

        for x in range(self._width -1):
            for y in range(self._height-1):
                if (self.liveOn([x,y])):
                    self._boardNP[x+1, y+1] = 1
                else:
                    self._boardNP[x+1, y+1] = 0
                    self.killCell((x,y))

    @property
    def countCells(self):
        return self._cellOn

    def draw(self):
        for i in range(self._fps):
            #print(i)
            os.system("clear")
            self.update()
            for row in self._boardNP:
                print(row)
            print("\n")
            print(self.countCells)
            time.sleep(2)

    def killCell(self, cell):
        #print(cell)
        #print(self._aliveValues)
        if(cell in self._aliveValues):
            self._aliveValues.remove(cell)
            self._cellOn -= 1

