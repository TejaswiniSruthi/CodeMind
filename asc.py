def asc(arr,n):
    for i in range(n-1):
        if(arr[i+1]-arr[i]<=0):
            return False
    return True
        

n=int(input())
arr=list(map(int,input().split()))
if asc(arr,n):
    print('yes')
else:
    print('no')
