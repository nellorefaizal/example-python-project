
import time

def longSquare(n):
    time.sleep(2)
    print(n**2)
    return n**2


print([longSquare(n) for n in range(0,10)])



