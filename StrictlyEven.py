def joy(arr,n):
    for i,ele in enumerate(arr):
        if(ele%2==0):
            if(i%2!=0):
                return False
    return True
        
n=int(input())
arr=list(map(int,input().split()))
print(joy(arr,n))
