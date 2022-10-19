n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=1
for i in arr:
    if(i<min(a,b) or i>max(a,b)):
        print(i,end=' ')
        c=0
if(c):
    print(-1)
