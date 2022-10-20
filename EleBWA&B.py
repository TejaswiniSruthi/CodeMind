n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=1
for i in arr:
    if((i>=a and i <=b) or (i<=a and i >=b)):
        c=0
        print(i,end=' ')
if(c):
    print(-1)
