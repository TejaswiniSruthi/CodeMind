s=input().split()
for i in s:
    ar=[]
    for j in i:
        ar.append(ord(j))
    print(chr(min(ar)),chr(max(ar)),end=' ')
