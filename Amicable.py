from math import sqrt

def fact(n):
    s=1
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            s+=((n//i)+i)
            if(n//i==i):
                s-=i
    return s

a=int(input())
b=int(input())
if fact(a)==b and fact(b)==a:
    print('Amicable')
else:
    print('Not Amicable')
