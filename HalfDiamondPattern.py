n=int(input())
if(n>=3 and n<=100):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()
    x=n-1
    for i in range(n):
        for j in range(n):
            if(j<x):
                print('*',end='')
        print()
        x-=1
        if(x==0):
            break
else:
    print('The pattern is not possible')
