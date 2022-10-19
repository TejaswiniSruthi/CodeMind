n=int(input())
l=n
arr=list(map(int,input().split()))
for i in range(0,n//2):
    print(arr[i],end=' ')
    print(arr[l-1],end=' ')
    l-=1
if(n%2!=0):
    print(arr[n//2],0)
