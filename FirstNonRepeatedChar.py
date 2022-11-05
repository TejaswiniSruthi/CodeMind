t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s='*'+s+'*'
    n=n+2
    t=True
    for i in range(1,n-1):
        if (s[i] not in s[i+1:n-1]) and (s[i] not in s[0:i]):
            print(s[i])
            t=False
            break
    if t:
        print(-1)
