s=input().lower().split()
v=['a','e','i','o','u']
m=5
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if(c<m):
        m=c
print(m)
