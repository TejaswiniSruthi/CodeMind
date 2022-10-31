s=input()
v=['a','e','i','o','u']
arr=[]
for i in range(len(s)-1):
    if (s[i] not in v and s[i+1] in v):
        print('C',end='')
        arr.append('C')
    if (s[i] in v and s[i+1] not in v):
        print('V',end='')
        arr.append('V')
if arr[-1]=='V' and s[-1] not in v:
    print('C')
elif arr[-1]=='C' and s[-1] in v:
    print('V')
