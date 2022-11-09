def ransom(rn,m):
    rn=list(rn)
    n=len(rn)
    m=list(m)
    i=0
    while(n):
        if rn[i] in m:
            m.remove(rn[i])
            rn.remove(rn[i])
        else:
            i+=1
        n-=1
        if rn==[]:
            return True
    return False

rn,m=input().split()
print(ransom(rn,m))
