a,b=map(int,input().split())
ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
ar=set(ar1+ar2)
c=0
for i in ar:
    if i in ar2 and i in ar1:
        c+=1
print(c)
