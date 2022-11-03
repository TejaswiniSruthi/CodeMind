s=input()
p=c=0
v=['a','e','i','o','u']
for i in s:
    if i in v:
        c+=1
    else:
        c=0
    if c>p:
        p=c
print(p)
