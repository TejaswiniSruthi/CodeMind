n=int(input())
arr=list(map(int,input().split()))
d={}
c=0
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
arr=[]
for k,v in d.items():
    if(k==v):
        c+=1
print(c)
