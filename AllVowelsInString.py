def vow(s):
    v=['a','e','i','o','u']
    V=['A','E','I','O','U']
    for i in s:
        if i in v:
            v.remove(i)
        if i in V:
            V.remove(i)
        if len(v)==0 or len(V)==0:
            return True
    return False
s=input().replace(' ','')
print(vow(s))
