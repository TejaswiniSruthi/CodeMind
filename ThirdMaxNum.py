n=int(input())
arr=list(map(int,input().split()))
arr=sorted(set(arr))[::-1]
p=0
if len(arr)<3:
    print(max(arr))
else:
    while(p!=3):
        if len(arr)==0:
            break
        m=arr[0]
        arr.remove(m)
        p+=1
    print(m)
