from math import sqrt

def isPerfectSqr(n):
    sq=int(sqrt(n))
    return sq*sq==n

def isFib(n):
    return isPerfectSqr(5*n*n+4) or isPerfectSqr(5*n*n-4)

n=int(input())
i=0
while(True):
    if(isFib(n-i) and isFib(n+i)):
        print(n-i,n+i)
        break
    if isFib(n-i):
        print(n-i)
        break
    elif isFib(n+i):
        print(n+i)
        break
    i+=1
