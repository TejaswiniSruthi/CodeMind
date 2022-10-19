n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in arr:
    if(i<min(a,b) or i>max(a,b)):
        c+=i
print(c)
