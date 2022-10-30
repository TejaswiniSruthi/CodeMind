def lcm(arr,pr):
    m=max(arr)
    for i in range(m,pr,m):
        c=0
        for j in arr:
            if i%j!=0:
                break
            else:
                c+=1
        if c==len(arr):
            return i

n=int(input())
arr=list(map(int,input().split()))
pr=1
for i in arr:
    pr*=i
print(lcm(arr,pr))
