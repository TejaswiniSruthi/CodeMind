n=input()
arr=list(map(int,input().split()))
x=(len(str(min(arr))))
c=0
for i in arr:
    if(len(str(i))==x):
        c+=1
print(c)
