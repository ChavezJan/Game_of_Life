"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import os
from main import coordinate

"""
    Reads and organize the:
    Max - x,y
    fps
    coordinates
"""

def fileReader(maxX,maxY,fps,coordinates):

    inputPath = "/Users/chavez/Documents/UP/Semestre 11/Simulacion Grafica/Parcial 1/GoL/Config/inputs/input2.txt"

    fileR = open(inputPath,"r")
    fileR = fileR.read().split("\n")
    lineCont = 0
    for i in fileR:
        lineCont += 1
        i = i.split(" ")
        if(lineCont == 1):
            maxX = int(i[0])
            maxY = int(i[1])
        elif(lineCont == 2):
            fps = int(i[0])
        elif(lineCont >=3):
            try:
                assert(int(i[0])<= maxX and int(i[1]) <= maxY)
                coordinates.append(coordinate(i[0],i[1],(lineCont - 2)))
            except AssertionError:
                print("ERROR: one of the coordinates is exceeding board Size")
                exit()
        # print(i + "-a")
    return maxX, maxY, fps, coordinates
