m,n=map(int,input().split())
arr=[0]*n
mat=[]
for i in range(m):
    lst=list(map(int,input().split()))
    mat.append(lst)
    for j in range(n):
        arr[j]+=mat[i][j]
print(*arr)
