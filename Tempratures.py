n=int(input())
arr=list(map(int,input().split()))
j=1
res=[]
i=0
while(True):
    if i==n-1:
        res.append(0)
        break
    if arr[i]<arr[i+j]:
        res.append(j)
        j=1
        i+=1
    else:
        j+=1
        if i+j==n:
            res.append(0)
            i+=1
            j=1
print(*res)
