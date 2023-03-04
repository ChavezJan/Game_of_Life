from multiprocessing import Pool, Process
import os
import time
 
def mult(n):
    n +=1
    resultado = n**3
    print( resultado)

def test2(numero):
    print(os.getpid())
    for n in range(10):
        valor = n*n+n
        print(valor,"---->", numero)
        #

if __name__ == '__main__':
    #Pool().starmap(mult,[2,3,5])

    procesos=[]
    
    cores = os.cpu_count()
    print("CPU COURE: ", cores)
    # iniciar procesos en cores
    for n in range(cores):
        proceso = Process(target=test2,args=(n,))
        procesos.append(proceso)

    start = time.time()
    print("Ejecucion")
    for proceso in procesos:
        proceso.start()

    print("Esperando")
    for proceso in procesos:
        proceso.join()
         
    end=time.time()
    print("Time paralelo -> "+str(end - start))

    time.sleep(2)

    start2 = time.time()
    for i in range(cores):
        test2(i)
    end2 = time.time()

    print("Time Sin paralelo -> "+str(end2 - start2))