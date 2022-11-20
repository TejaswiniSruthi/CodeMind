t=int(input())
for _ in range(t):
    b=False
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(n):
        if(b):
            break
        for j in range(i,n):
            if(sum(arr[i:j+1])==k):
                print(i+1,j+1)
                b=True
                break
    if not(b):
        print(-1)
