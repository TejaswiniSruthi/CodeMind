n=int(input())
s=''
while(n!=0):
    r=n%2
    if(r==0):
        r=1
    else:
        r=0
    s+=str(r)
    n//=2
s=s[::-1]
l=len(s)-1
r=0
for i in (s):
    r+=int(i)*(2**l)
    l-=1
print(r)
