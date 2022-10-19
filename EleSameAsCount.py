n=int(input())
arr=list(map(int,input().split()))
d={}
c=1
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ar=[]
for k,v in d.items():
    if(k==v):
        ar.append(k)
        c=0
if(c):
    print(-1)
else:
    for i in arr:
        if(i in ar):
            print(i,end=' ')
            ar.remove(i)
        if(ar==[]):
            break
        
