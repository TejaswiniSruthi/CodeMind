n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    print(i,end=' ')
if(n%2!=0):
    print(0)
