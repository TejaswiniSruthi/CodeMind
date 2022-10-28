def sor(s):
    ns=''
    for i in s:
        if ord(i)>64:
            ns+=i
    ns=sorted(ns)
    j=0
    res=''
    for i in s:
        if(ord(i)<65):
            res+=i
        else:
            res+=ns[j]
            j+=1
    return(res)
    
s=input()
arr=[]
arr=s.split()
nlist=[]
for i in arr:
    print(sor(i),end=' ')
