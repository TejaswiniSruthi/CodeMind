s=input().lower().split()
v=['a','e','i','o','u']
ar=[]
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    ar.append(c)
c=0
m=min(ar)
for i in ar:
    if i==m:
        c+=1
print(c)
