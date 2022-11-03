s=input()
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=max(dic.values())
f=True
c=0
for v in dic.values():
    if m-v>0:
        c+=(m-v)
    if c>1:
        print('Not Valid')
        f=False
        break
if f:
    print('Valid String')
