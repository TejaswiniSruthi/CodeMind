n=int(input())
arr=list(map(int,input().split()))
ar=[]
for i in arr:
    if i not in ar:
        ar.append(i)
for i in ar:
    print(i,end=' ')
