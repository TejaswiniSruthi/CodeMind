from math import sqrt

def isPrime(n):
    if(n<1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=int(input())
b=True
for i in range(2,int(sqrt(n))+1):
    if(n%i==0):
        p1=i
        p2=n//i
        if(isPrime(p1) and isPrime(p2)):
            print(p1,p2)
            b=False
            break
if(b):
    print(-1)
