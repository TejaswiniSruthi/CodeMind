n=int(input())
arr=list(map(int,input().split()))
p=int(input())
d={}
c=1
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if(v==p):
        print(k,end=' ')
        c=0
if(c):
    print(-1)
