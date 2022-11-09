n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(k):
    arr=arr[n-1:n]+arr[0:n-1]
for i in range(q):
    print(arr[int(input())])
