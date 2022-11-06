t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j]) in arr:
                c+=1
    if c:
        print(c)
    else:
        print(-1)
