n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(len(str(abs(i)))==k):
        c+=1
print(c)
