s=input()
v=['a','e','i','o','u','A','E','I','O','U']
arr=[]

for i in range(len(s)):
    if s[i] in v:
        arr.append(i)
r=''
n=len(arr)
j=1
for i in range(len(s)):
    if i in arr:
        r+=s[arr[n-j]]
        j+=1
    else:
        r+=s[i]
print(r)
