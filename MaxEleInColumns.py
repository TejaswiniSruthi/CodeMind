m,n=map(int,input().split())
res=[0]*n
mat=[]
for i in range(m):
    arr=list(map(int,input().split()))
    mat.append(arr)
    for j in range(n):
        if mat[i][j]>res[j]:
            res[j]=mat[i][j]
print(*res,sep='\n')
