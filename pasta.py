def task(a,b):
    for i in b:
        if i not in a:
            return False
        else:
            a.remove(i)
    return True

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if task(a,b):
    print('Yes')
else:
    print('No')
