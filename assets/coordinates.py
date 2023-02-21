"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import numpy as np

class coordinate:
    def __init__(self,x,y,id) -> None:
        self._x = int(x)
        self._y = int(y)
        self._id = id
        self._alive = True
    

    def __str__(self) -> str:
        return "ID %02d" % self._id

    @property
    def alive(self):
        return self._alive
    @property
    def position(self):
        return self._x, self._y

    
    @alive.setter
    def alive(self, value):
        self._alive = value 