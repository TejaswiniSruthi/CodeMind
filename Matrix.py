r,c=map(int,input().split())
os=es=0
for i in range(r):
    ar=[]
    ar=list(map(int,input().split()))
    if(i%2==0):
        es+=sum(ar)
    else:
        os+=sum(ar)
print(es,os)
