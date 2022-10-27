n=int(input())
arr=list(map(int,input().split()))
m=min(arr)
for i in range(m,0,-1):
    c=0
    for j in arr:
        if(j%i==0):
            c+=1
            res=i
    if(c==len(arr)):
        print(res)
        break
