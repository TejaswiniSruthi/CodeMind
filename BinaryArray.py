def out(arr):
    for i in arr:
        if(i>1):
            return (False)
    return True

n=int(input())
arr=list(map(int,input().split()))
print(out(arr))
