def joy(arr):
    for i in arr:
        if(i%2!=0):
            return False
    return True

n=int(input())
arr=list(map(int,input().split()))
print(joy(arr))
