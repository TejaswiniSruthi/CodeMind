n=int(input())
arr=list(map(int,input().split()))
ar2=[]
ar1=[]
for i in arr:
    if(i%2!=0):
        ar2.append(i)
    else:
        ar1.append(i)
arr=(ar1+ar2)
for i in arr:
    print(i,end=' ')
