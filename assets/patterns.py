import numpy as np
from . import bord as BD
from multiprocessing import Pool ,Process
import os
import time
ON = 1

def checkPat(typ,boardNP):
    # print(typ)

    # coreNum = os.cpu_count()
    # nProcess = []
    # if(len(typ) <= coreNum):
    #     for ty in typ:
    #         uProcess = Process(target=typesOfPattern,args=(ty,boardNP,))
    #         nProcess.append(uProcess)
    # print("Iniciando Paralelismo")
    # for uProcess in nProcess:
    #     uProcess.start()
    # print("Terminando Paralelismo")
    # for uProcess in nProcess:
    #     uProcess.join()


    tStart = time.time()

    with Pool() as pool:
        args = [(ty,boardNP)for ty in typ]
        print(args)
        async_results = pool.starmap(switcher,args)
        print(async_results)

    tEnd = time.time()
    print("Time of Ex: " + str(tEnd-tStart))

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

    return countPatOrder

        
    time.sleep(5)
    #    [print(ar.get()) for ar in async_results]
    
    
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


def checkBlock(boardNP):
    x,y = np.shape(boardNP)
   
    print(x)
    print(y)
    return 0


    # for i in range(0, x):
    #     for j in range(0, y):
    #             if(np.array_equal(grid[i:i+4, j:j+4] , block, equal_nan=True) ):
    #                 countBlock+=1
    
def checkBeehive(board):
    print("m")
    return 1
    

def checkLoaf(board):
    print("L")
    return 2

def checkBoat(board):
    print("l")
    return 3
def checkTub(board):
    print("l")
    return 4

def checkBlinker(board):
    print("p")
    return 5

def checkToad(board):
    print("o")
    return 6

def checkBeacon(board):
    print("i")
    return 7

def checkGlinder(board):
    print("s")
    return 8

def checkLGShip(board):
    print(2)
    return 9

block = np.array([[0, 0, 0, 0],
                [0, ON, ON, 0], 
                [0, ON, ON, 0], 
                [0, 0, 0, 0]])
        
beehive = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, ON, ON, 0, 0],
                    [0, ON, 0, 0, ON, 0],
                    [0, 0, ON, ON, 0, 0],
                    [0, 0, 0, 0, 0, 0]])

loaf = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, ON, ON, 0, 0],
                    [0, ON, 0, 0, ON, 0],
                    [0, 0, ON, 0, ON, 0],
                    [0, 0,   0, ON,   0, 0],
                    [0, 0, 0, 0, 0, 0]])

boat = np.array([[0, 0, 0, 0, 0],
                    [0, ON, ON, 0, 0], 
                    [0, ON, 0, ON, 0], 
                    [0, 0, ON, 0, 0],
                    [0, 0, 0, 0, 0]])

tub = np.array([[0, 0, 0, 0, 0],
                [0, 0, ON, 0, 0], 
                [0, ON, 0, ON, 0], 
                [0, 0, ON, 0, 0],
                [0, 0, 0, 0, 0]])

blinker1 = np.array([[0, 0, 0],
                    [0, ON, 0], 
                    [0, ON, 0], 
                    [0, ON, 0],
                    [0, 0, 0]])

blinker2 = np.array([[0, 0, 0, 0, 0],
                    [0, ON, ON, ON, 0],
                    [0, 0, 0, 0, 0]])

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