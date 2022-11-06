n=int(input())
arr=list(map(int,input().split()))
ear=[]
oar=[]
for i in arr:
    if i%2==0:
        ear.append(i)
    else:
        oar.append(i)
while(True):
    if len(oar)!=0:
        print(oar[0],end=' ')
        oar.remove(oar[0])
    if len(ear)!=0:
        print(ear[0],end=' ')
        ear.remove(ear[0])
    if len(oar)==0 and len(ear)==0:
        break
if len(arr)%2:
    print(0)
