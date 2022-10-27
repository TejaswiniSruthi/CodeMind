def selfdiv(n):
    t=n
    n=str(n)
    for i in n:
        if(int(i)==0):
            return False
        if t%(int(i))!=0:
            return False
    return True

a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfdiv(i):
        print(i,end=' ')
