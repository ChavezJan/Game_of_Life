"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import time
import os
from datetime import date


def output(x,y):
    today = date.today()
    print("Simulation at: ",today)
    print("Universe size: ",x , " X ", y)
    fileCreate(x,y)

"""
    Create the new File.
"""
def fileCreate(x,y) -> None:
    if os.path.exists("Report.txt"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("Report.txt")
        fileCreate(x,y)
    else:
        print("The file does not exist.")
        print("Creating...\n")
        newFile = open("Report.txt","x")
        writeTitle(x,y)

def writeTitle(x,y):
    today = date.today()
    file = open("Report.txt","a")
    text = "Simulation at: "+str(today) + "\n"
    text += "Universe size: "+str(x) +  " X "+ str(y)+ "\n"
    file.write(text)
    file.close()