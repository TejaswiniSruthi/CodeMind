n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i,n):
        if(sum(arr[i:j+1])==k):
            c+=1
print(c)
