a,b=map(int,input().split())
ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
ar=(ar1+ar2)
for i in ar:
    if i not in ar2 or i not in ar1:
        print(i,end=' ')
