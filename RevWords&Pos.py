s=input().split()
n=len(s)-1
for i in range(0,len(s)):
    s[i]=s[i][::-1]
for i in range(n,-1,-1):
    print(s[i],end=' ')
