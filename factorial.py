
#def factorial(n):
 #   if type(n)!=int:
 
  #     return None
#   if n<0:
  #       return None
  #  fact=1
  #  count=1
  #  while count<=n:
  #      fact*=count
  #      count+=1
  #  return fact
def factorial(n):
    if type(n)!=int:
        return None
    if n<0:
        return None
    if n==0:
        return 1
    return n*factorial(n-1)
 
print ("factorial is" + str(factorial(6)))