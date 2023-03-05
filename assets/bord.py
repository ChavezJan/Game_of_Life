"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import os
import numpy as np

from copy import deepcopy
import time
from multiprocessing import Pool,Process 
from . import generateFile as GF
from . import patterns as PT



class Board():
    def __init__(self, width, height, fps):
        self._width = width+1
        self._height = height+1
        self._boardNP = np.zeros((self._height+1,self._width+1), dtype=int)
        self._aliveValues = []
        self._cellOn = 0
        self._fps = fps
        self._block = 0
        self._beehive = 0
        self._loaf = 0
        self._boat = 0
        self._tub = 0
        self._blinker = 0
        self._toad = 0
        self._beacon = 0
        self._glinder = 0
        self._lgShip = 0
        

    def restartCount(self):
        self._block = 0
        self._beehive = 0
        self._loaf = 0
        self._boat = 0
        self._tub = 0
        self._blinker = 0
        self._toad = 0
        self._beacon = 0
        self._glinder = 0
        self._lgShip = 0
    
      
    def applyCount(self,count):
        self._block = count[0]
        self._beehive = count[1]
        self._loaf = count[2]
        self._boat = count[3]
        self._tub = count[4]
        self._blinker = count[5]
        self._toad = count[6]
        self._beacon = count[7]
        self._glinder = count[8]
        self._lgShip = count[9]


    def getBoard(self):
        return self._boardNP

    def getPatt(self):
        return [self._block,self._beehive,self._loaf,self._boat,self._tub,self._blinker,self._toad,self._beacon,self._glinder,self._lgShip]
    


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
        Check Rules
    """
    def liveOnNS(self,cell):
        on = self._boardNP[cell[0],cell[1]] + self._boardNP[cell[0],cell[1] +1] +self._boardNP[cell[0],cell[1]+2]
        on += self._boardNP[cell[0]+1,cell[1]] + self._boardNP[cell[0]+1,cell[1] +1] +self._boardNP[cell[0]+1,cell[1]+2]
        on += self._boardNP[cell[0]+2,cell[1]] + self._boardNP[cell[0]+2,cell[1] +1] +self._boardNP[cell[0]+2,cell[1]+2]
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
        elif(self._boardNP[cell[0]+1, cell[1]+1] == 0 and (on == 3)):#check if its work
            return True
        else:
            return False

    def update(self,i):
        types = ["block","beehive","loaf","boat","tub","blinker","toad","beacon","glinder","lgShip"]
        numbers = [2,3,5]
        self._blinker += 1
        self.restartCount()
        boardState = deepcopy(self._boardNP)

        for x in range(self._width -1):
            for y in range(self._height-1):
                if (self.liveOnNS([x,y])):
                    if(self._boardNP[x+1, y+1] == 0):
                        self.reviveCell((x,y))
                    boardState[x+1, y+1] = 1
                else:
                    if(self._boardNP[x+1, y+1] == 1):
                        self.killCell((x,y))
                    boardState[x+1, y+1] = 0

        self._boardNP = deepcopy(boardState)
        #check status for the report
        
        PT.checkPat(types,self._boardNP,i)
        

        
       

    """
        Getter for the Cells count
    """
    @property
    def countCells(self):
        return self._cellOn

    """
        Updates the Console with the new values 
    """
    def draw(self,sleepTime):
        for i in range(self._fps):
            self.update(i)
            os.system("clear")
            for row in self._boardNP:
                print(row)
            # print("\n")
            # print(self.countCells)
            time.sleep(0)
    """
        This kills all the cells that value is 0
        Subtract from the live cell count
    """
    def killCell(self, cell):
        if(cell in self._aliveValues):
            self._aliveValues.remove(cell)
            self._cellOn -= 1

    def reviveCell(self, cell):
        self._aliveValues.append(cell)
        self._cellOn += 1
