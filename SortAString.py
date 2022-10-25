s=input()
res=sorted(s.strip('!@#$%^&*()').replace(' ',''))
r=''
for i in range(len(s)):
    if not(s[i].isalpha()):
        r+=s[i]
    else:
        r+=res[0]
        res.remove(res[0])
print(r)
