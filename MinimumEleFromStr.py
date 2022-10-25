s=input().split()
n=len(s)
m=123
for i in s[n-1]:
    if ord(i)<m:
        m=ord(i)
        r=i
if(r.lower() in s[n-1]):
    print(r.lower())
else:
    print(r)
