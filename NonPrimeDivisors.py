from math import sqrt

def isPrime(n):
    if n<=1:
        return True
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return True
    return False

b=int(input())
c=0
for i in range(1,b+1):
    if(isPrime(i) and b%i==0):
        c+=1
print(c)
