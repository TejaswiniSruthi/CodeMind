n=int(input())-1
arr=list(map(int,input().split()))
f=l=0
if(n%2==0):
    x=(n//2)-1
else:
    x=n//2
for i in range(n+1):
    if(i<=x):
        f+=arr[i]
    else:
        l+=arr[i]
print(abs(f-l))
