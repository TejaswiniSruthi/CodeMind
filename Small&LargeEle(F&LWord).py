s=input().split()
x=0
j=0
while(j!=2):
    ar=[]
    for i in s[x]:
        ar.append(ord(i))
    if x==0:
        mi=chr(min(ar))
        x=-1
    ma=chr(max(ar))
    j+=1
print(mi,ma)
