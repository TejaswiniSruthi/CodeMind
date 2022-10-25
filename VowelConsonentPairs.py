s=input().split()
v=['a','e','i','o','u']
c=0
for i in s:
    l=len(i)
    n=(l//2)
    for j in range(n):
        if((i[j] in v and i[l-1] not in v) or (i[j] not in v and i[l-1] in v)):
            c+=1
        l-=1
print(c)
