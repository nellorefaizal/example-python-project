
from multiprocess import Process
import time
def longSquare(num,results):
    time.sleep(3)
    results[num]=num**2
    print(num**2)
    return num**2


if __name__=='__main__':
    results ={}

    processes=[]
    for n in range(10):
        processes.append(Process(target = longSquare,args=(n, results)))


    for p in processes:
        p.start()
        time.sleep(1)

    for p in processes:
        p.join()    
        

    print(results)