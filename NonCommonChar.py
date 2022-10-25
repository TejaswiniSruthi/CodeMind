s1=sorted(input().lower().replace(' ',''))
s2=sorted(input().lower().replace(' ',''))
s3=[]
s3=list(set(s1))+list(set(s2))
s3=sorted(set(s3))
for i in s3:
    if i not in s1 or i not in s2:
        print(i,end='')
