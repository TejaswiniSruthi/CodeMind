n=int(input())
arr=list(input().split())
s=0
for i in range(n):
    for j in arr[i]:
        s+=int(j)
print(s)
