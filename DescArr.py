def desc(arr,n):
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            return False
    return True

n=int(input())
arr=list(map(int,input().split()))
if desc(arr,n):
    print('yes')
else:
    print('no')
