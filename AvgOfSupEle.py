n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
arr=[]
for k,v in d.items():
    if(k==v):
        arr.append(v)
if(len(arr)==0):
    print(-1)
else:
    avg=sum(arr)/len(arr)
    print('%.2f' %avg)
