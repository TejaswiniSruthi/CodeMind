s=input().split()
mas=mis=0
for i in s:
    ar=[]
    for j in i:
        ar.append(ord(j))
    mas+=max(ar)
    mis+=min(ar)
print(abs(mis-mas))
