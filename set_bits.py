t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    while(n!=0):
        r=n%2
        if(r==1):
            c+=1
        n//=2
    print(c)
