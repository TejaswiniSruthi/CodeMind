s=input().replace(' ','')
dic={}
for i in s:
    if ord(i) not in dic:
        dic[ord(i)]=1
    else:
        dic[ord(i)]+=1
mink=min(dic.keys())
maxk=max(dic.keys())
print(chr(mink),dic[mink],chr(maxk),dic[maxk])
