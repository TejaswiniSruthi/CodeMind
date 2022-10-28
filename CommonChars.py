s1=input().lower().replace(' ','')
s2=input().lower().replace(' ','')
s1=sorted(s1)
s2=sorted(s2)
arr=[]
for i in s1:
    if i in s2 and i not in arr:
        arr.append(i)
        print(i,end='')
if(len(arr)==0):
    print(-1)
