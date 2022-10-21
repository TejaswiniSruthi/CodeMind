from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=int(input())
d=0
for i in range(1,n+1):
    if((n%i==0) and (not(isPrime(i)))):
        d+=1
print(d)
