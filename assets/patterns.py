"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import numpy as np
from . import bord as BD
from multiprocessing import Pool, Process
from . import generateFile as GF

ON = 1

def checkPat(typ,boardNP,fps):


    with Pool(10) as pool:
        args = [(ty,boardNP)for ty in typ]
        async_results = pool.starmap(switcher,args)
        pool.terminate()
    
        

    countPatOrder = []
    for i in typ:
        countPatOrder.append(0)

    for i in async_results:
        if i[1] == "block":
            countPatOrder[0]= i[0]
        elif i[1] == "beehive":
            countPatOrder[1]= i[0]
        elif i[1] == "loaf":
            countPatOrder[2]= i[0]
        elif i[1] == "boat":
            countPatOrder[3]= i[0]
        elif i[1] == "tub":
            countPatOrder[4]= i[0]
        elif i[1] == "blinker":
            countPatOrder[5]= i[0]
        elif i[1] == "toad":
            countPatOrder[6]= i[0]
        elif i[1] == "beacon":
            countPatOrder[7]= i[0]
        elif i[1] == "glinder":
            countPatOrder[8]= i[0]
        elif i[1] == "lgShip":
            countPatOrder[9]= i[0]

    Pool().apply_async(GF.generateReportToW,args=(fps,countPatOrder))
    
def switcher(ty,boardNP):
    if ty == "block":
        return checkBlock(boardNP),ty
    elif ty == "beehive":
        return checkBeehive(boardNP),ty
    elif ty == "loaf":
        return checkLoaf(boardNP),ty
    elif ty == "boat":
        return checkBoat(boardNP),ty
    elif ty == "tub":
        return checkTub(boardNP),ty
    elif ty == "blinker":
        return checkBlinker(boardNP),ty
    elif ty == "toad":
        return checkToad(boardNP),ty
    elif ty == "beacon":
        return checkBeacon(boardNP),ty
    elif ty == "glinder":
        return checkGlinder(boardNP),ty
    elif ty == "lgShip":
        return checkLGShip(boardNP),ty

block = np.array([[0, 0, 0, 0],
                [0, ON, ON, 0], 
                [0, ON, ON, 0], 
                [0, 0, 0, 0]])

def checkBlock(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-4):
        for j in range(y-4):
            checkArray = boardNP[i:i+4,j:j+4]
            if (np.array_equal(checkArray,block)):
                count += 1
    return count
    
beehive1 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, ON, ON, 0, 0],
                    [0, ON, 0, 0, ON, 0],
                    [0, 0, ON, ON, 0, 0],
                    [0, 0, 0, 0, 0, 0]])
beehive2 = np.array([
                    [0, 0, 0, 0, 0],
                    [0, 0, ON, 0, 0],
                    [0, ON, 0, ON, 0],
                    [0, ON, 0, ON, 0],
                    [0, 0,  ON, 0, 0],
                    [0, 0, 0, 0, 0]])
def checkBeehive(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-6):
        for j in range(y-5):
            checkArray = boardNP[i:i+5,j:j+6]
            if (np.array_equal(checkArray,beehive1)):
                count += 1
            checkArray = boardNP[j:j+6,i:i+5]
            if (np.array_equal(checkArray,beehive2)):
                count += 1
    return count

loaf = np.array([[0, 0, 0, 0, 0, 0],
                 [0, 0, ON, ON, 0, 0],
                 [0, ON, 0, 0, ON, 0],
                 [0, 0, ON, 0, ON, 0],
                 [0, 0,   0, ON,   0, 0],
                 [0, 0, 0, 0, 0, 0]])
def checkLoaf(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-6):
        for j in range(y-6):
            checkArray = boardNP[i:i+6,j:j+6]
            if (np.array_equal(checkArray,loaf)):
                count += 1
    return count

boat = np.array([[0, 0, 0, 0, 0],
                    [0, ON, ON, 0, 0], 
                    [0, ON, 0, ON, 0], 
                    [0, 0, ON, 0, 0],
                    [0, 0, 0, 0, 0]])
def checkBoat(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-5):
        for j in range(y-5):
            checkArray = boardNP[i:i+5,j:j+5]
            if (np.array_equal(checkArray,boat)):
                count += 1
    return count

tub = np.array([[0, 0, 0, 0, 0],
                [0, 0, ON, 0, 0], 
                [0, ON, 0, ON, 0], 
                [0, 0, ON, 0, 0],
                [0, 0, 0, 0, 0]])
def checkTub(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-5):
        for j in range(y-5):
            checkArray = boardNP[i:i+5,j:j+5]
            if (np.array_equal(checkArray,tub)):
                count += 1
    return count

blinker1 = np.array([[0, 0, 0],
                    [0, ON, 0], 
                    [0, ON, 0], 
                    [0, ON, 0],
                    [0, 0, 0]])

blinker2 = np.array([[0, 0, 0, 0, 0],
                    [0, ON, ON, ON, 0],
                    [0, 0, 0, 0, 0]])
def checkBlinker(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-3):
        for j in range(y-5):
            checkArray = boardNP[i:i+3,j:j+5]
            if (np.array_equal(checkArray,blinker2)):
                count += 1
            checkArray = boardNP[j:j+5,i:i+3]
            if (np.array_equal(checkArray,blinker1)):
                count += 1
            
    return count

toad1 = np.array([[0, 0, 0, 0, 0, 0],
                [0, 0, 0, ON, 0, 0],
                [0, ON, 0, 0, ON, 0],
                [0, ON, 0, 0, ON, 0],
                [0, 0, ON, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]])

toad2 = np.array([[0, 0, 0, 0, 0, 0],
                [0, 0, ON, ON, ON, 0],
                [0, ON, ON, ON, 0, 0],
                [0, 0, 0, 0, 0, 0]])
def checkToad(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-6):
        for j in range(y-6):
            checkArray = boardNP[i:i+6,j:j+6]
            if (np.array_equal(checkArray,toad1)):
                count += 1
            checkArray = boardNP[j:j+4,i:i+6]
            if (np.array_equal(checkArray,toad2)):
                count += 1
            
    return count

beacon1 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, ON, ON, 0, 0, 0],
                    [0, ON, ON, 0, 0, 0],
                    [0, 0, 0, ON, ON, 0],
                    [0, 0, 0, ON, ON, 0],
                    [0, 0, 0, 0, 0, 0]])

beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                    [0, ON, ON, 0, 0, 0],
                    [0, ON, 0, 0, 0, 0],
                    [0, 0, 0, 0, ON, 0],
                    [0, 0, 0, ON, ON, 0],
                    [0, 0, 0, 0, 0, 0]])
def checkBeacon(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-6):
        for j in range(y-6):
            checkArray = boardNP[i:i+6,j:j+6]
            if (np.array_equal(checkArray,beacon1)):
                count += 1
            elif (np.array_equal(checkArray,beacon2)):
                count +=1
            
    return count

glider1 = np.array([[0, 0, 0, 0, 0],
                    [0, 0, ON, 0, 0], 
                    [0, 0, 0, ON, 0], 
                    [0, ON, ON, ON, 0],
                    [0, 0, 0, 0, 0]])

glider2 = np.array([[0, 0, 0, 0, 0],
                    [0, ON, 0, ON, 0], 
                    [0, 0, ON, ON, 0], 
                    [0, 0, ON, 0, 0],
                    [0, 0, 0, 0, 0]])

glider3 = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, ON, 0], 
                    [0, ON, 0, ON, 0], 
                    [0, 0, ON, ON, 0],
                    [0, 0, 0, 0, 0]])

glider4 = np.array([[0, 0, 0, 0, 0],
                    [0, ON, 0, 0, 0], 
                    [0, 0, ON, ON, 0], 
                    [0, ON, ON, 0, 0],
                    [0, 0, 0, 0, 0]])
def checkGlinder(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-5):
        for j in range(y-5):
            checkArray = boardNP[i:i+5,j:j+5]
            if (np.array_equal(checkArray,glider1)):
                count += 1
            elif (np.array_equal(checkArray,glider2)):
                count +=1
            elif (np.array_equal(checkArray,glider3)):
                count +=1
            elif (np.array_equal(checkArray,glider4)):
                count +=1
            
    return count

lws1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, ON, 0, 0, ON, 0, 0], 
                [0, 0, 0, 0, 0, ON, 0], 
                [0, ON, 0, 0, 0, ON, 0],
                [0, 0, ON, ON, ON, ON, 0],
                [0, 0, 0, 0, 0, 0, 0]])

lws2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, ON, ON, 0, 0], 
                [0, ON, ON, 0, ON, ON, 0], 
                [0, ON, ON, ON, ON, 0, 0],
                [0, 0, ON, ON, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])

lws3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, ON, ON, ON, ON, 0], 
                [0, ON, 0, 0, 0, ON, 0], 
                [0, 0, 0, 0, 0, ON, 0],
                [0, ON, 0, 0, ON, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])

lws4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, ON, ON, 0, 0, 0], 
                [0, ON, ON, ON, ON, 0, 0], 
                [0, ON, ON, 0, ON, ON, 0],
                [0, 0, 0, ON, ON, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])
def checkLGShip(boardNP):
    x,y = np.shape(boardNP)
    count = 0

    for i in range(x-6):
        for j in range(y-7):
            checkArray = boardNP[i:i+6,j:j+7]
            if (np.array_equal(checkArray,glider1)):
                count += 1
            elif (np.array_equal(checkArray,glider2)):
                count +=1
            elif (np.array_equal(checkArray,glider3)):
                count +=1
            elif (np.array_equal(checkArray,glider4)):
                count +=1
            
    return count




