s=input().lower()
v=['a','e','i','o','u']
m=c=0
for i in s:
    if(i==' '):
        c=0
    if i in v:
        c+=1
    if(c>m):
        m=c
print(m)
