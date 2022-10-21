from math import sqrt

def isPrimePal(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    if(str(n)==str(n)[::-1]):
        return True
    else:
        return False

n=int(input())
while(True):
    n+=1
    if(isPrimePal(n)):
        print(n)
        break
