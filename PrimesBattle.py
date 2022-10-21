from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True
n1=int(input())
n2=int(input())
n3=n1+n2
i=1
while(True):
    if(isPrime(n3+i)):
        print(i)
        break
    i+=1
    
