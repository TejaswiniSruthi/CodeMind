n=int(input())
arr=list(map(int,input().split()))
arr=set(arr)
s=0
for i in arr:
    if (i%2==0):
        s+=1
print(s)
