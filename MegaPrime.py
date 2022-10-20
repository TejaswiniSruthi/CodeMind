from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True
    
n=int(input())
b=False
if isPrime(n):
    b=True
    n=str(n)
    for i in n:
        i=int(i)
        if not(isPrime(i)):
            b=False
            break
if not(b):
    print('Not Mega Prime')
else:
    print('Mega Prime')
