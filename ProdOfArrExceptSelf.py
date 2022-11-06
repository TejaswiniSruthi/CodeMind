def prod(ar):
    pr=1
    for i in ar:
        pr*=i
    return pr

n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if i==n-1:
        res=arr[0:n-1]
        print(prod(res),end=' ')
    else:
        res=arr[0:i]+arr[i+1:n]
        print(prod(res),end=' ')
