n=int(input())
arr=list(map(int,input().split()))
m=-10
for i in range(n):
    for j in range(i,n):
        if(sum(arr[i:j+1])>m):
            m=sum(arr[i:j+1])
print(m)
