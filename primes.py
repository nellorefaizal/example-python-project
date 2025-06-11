
def isprime(n, foundprime=None):
    foundprime=range(2,int(n**0.5)) if foundprime is None else foundprime
    for factor in foundprime:
        if n% factor == 0:
            return False
        return True
    
def listPrime(max):
    foundprime=[]
    for n in range(2,max):
        if isprime(n,foundprime):
            foundprime.append(n)

    return foundprime