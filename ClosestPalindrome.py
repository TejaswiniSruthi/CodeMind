def left(n):
    while(n!=0):
        if(str(n)==(str(n)[::-1])):
            return n
        n-=1
def right(n):
    while(n!=0):
        if(str(n)==(str(n)[::-1])):
            return n
        n+=1

n=int(input())
l=left(n-1)
r=right(n+1)
if(abs(n-l)<abs(n-r)):
    print(l)
elif(abs(n-l)>abs(n-r)):
    print(r)
else:
    print(l,' ',r)
