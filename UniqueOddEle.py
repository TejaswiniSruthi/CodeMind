n=int(input())
arr=list(map(int,input().split()))
arr=set(arr)
c=0
for i in arr:
    if(i%2!=0):
        c+=1
print(c)
