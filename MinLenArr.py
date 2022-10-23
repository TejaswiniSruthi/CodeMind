s=input()
s=s.split(' ')
m=len(s[0])
for i in s:
    if(len(i)<m):
        m=len(i)
print(m)
