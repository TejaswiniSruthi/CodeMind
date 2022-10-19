n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
ar=[]
c=1
for i in arr:
    if(i<a or i>b):
        ar.append(i)
        c=0
if(c):
    print(-1)
else:
    print(max(ar))
