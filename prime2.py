
from mynumbers.factors import getFactors

#from mynumbers import factors

def isPrime(n, foundPrime=None):
    return len(getFactors(n))==2

print(isPrime(9))

print('in prime2.py the name is:',__name__)