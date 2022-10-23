s=input().replace(' ','')
v=['a','e','i','o','u']
for i in s:
    if i in v:
        v.remove(i)
        if(len(v)==0):
            print(0)
            break
for i in v:
    print(i,end=' ')
