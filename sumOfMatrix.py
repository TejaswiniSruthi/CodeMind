r,c=map(int,input())
s=0
for i in range(r):
    ar=[]
    ar=list(map(int,input().split()))
    s+=sum(ar)
print(s)
