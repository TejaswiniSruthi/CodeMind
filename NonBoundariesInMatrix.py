m,n=map(int,input().split())
mat=[]
s=0
for i in range(m):
    lst=list(map(int,input().split()))
    mat.append(lst)
    for j in range(n):
        if (i!=0 and j!=0 and i!=(m-1) and j!=(n-1)):
            s+=mat[i][j]
print(s)
