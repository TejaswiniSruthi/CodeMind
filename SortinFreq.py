n=int(input())
arr=list(map(int,input().split()))
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
while(True):
    for k,v in dic.items():
        m=max(dic.values())
        if v==m:
            print(k,end=' ')
            dic[k]=-1
            break
    if max(dic.values())==-1:
        break
    
