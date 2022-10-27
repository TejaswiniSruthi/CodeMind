n=int(input())
arr=list(map(int,input().split()))
m=min(arr)
T=True
for i in arr:
    if i%m!=0:
        print(1)
        T=False
        break
if T:
    print(m)
