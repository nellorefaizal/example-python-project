def getFactors(n):
    return[factor for factor in range(1,n+1) if n%factor==0]

print('in factors.py the name is: ',__name__)