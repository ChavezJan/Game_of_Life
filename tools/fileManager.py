import os
from main import coordinate

"""
    Reads and organize the:
    Max - x,y
    fps
    coordinates
"""

def fileReader(maxX,maxY,fps,coordinates):

    inputPath = "/Users/chavez/Documents/UP/Semestre 11/Simulacion Grafica/Parcial 1/GoL/input.txt"

    fileR = open(inputPath,"r")
    fileR = fileR.read().split("\n")
    lineCont = 0
    for i in fileR:
        lineCont += 1
        i = i.split(" ")
        print(i[0] + " " + i[1])
        if(lineCont == 1):
            maxX = int(i[0])
            maxY = int(i[1])
        elif(lineCont == 2):
            fps = int(i[0])
        elif(lineCont >=3):
            coordinates.append(coordinate(i[0],i[1]))
        # print(i + "-a")
    return maxX, maxY, fps, coordinates
