s=input().replace(' ','')
v=('a','e','i','o','u','A','E','I','O','U')
ar=[]
for i in s:
    if (i in v and i not in ar):
        ar.append(i)
for i in ar:
    print(i,end=' ')
